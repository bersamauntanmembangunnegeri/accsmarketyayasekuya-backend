from flask import Blueprint, jsonify, request
from src.models.user import db
from src.models.order import Order
from src.models.product import Product
from src.models.vendor import ProductVendor
from decimal import Decimal
import re

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    """Create a new order"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['email', 'product_id', 'vendor_id', 'quantity', 'payment_method']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Validate email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, data['email']):
            return jsonify({
                'success': False,
                'message': 'Invalid email format'
            }), 400
        
        # Validate quantity
        if data['quantity'] <= 0:
            return jsonify({
                'success': False,
                'message': 'Quantity must be greater than 0'
            }), 400
        
        # Check if product exists and is active
        product = Product.query.filter_by(id=data['product_id'], is_active=True).first()
        if not product:
            return jsonify({
                'success': False,
                'message': 'Product not found or inactive'
            }), 404
        
        # Check if vendor has this product
        product_vendor = ProductVendor.query.filter_by(
            product_id=data['product_id'],
            vendor_id=data['vendor_id'],
            is_active=True
        ).first()
        
        if not product_vendor:
            return jsonify({
                'success': False,
                'message': 'Vendor does not have this product'
            }), 404
        
        # Check stock availability
        if product_vendor.stock < data['quantity']:
            return jsonify({
                'success': False,
                'message': 'Insufficient stock'
            }), 400
        
        # Calculate prices
        unit_price = product_vendor.price
        total_price = unit_price * data['quantity']
        
        # Apply coupon if provided
        coupon_code = data.get('coupon_code')
        if coupon_code:
            # Simple coupon logic - you can expand this
            if coupon_code.lower() == 'news':
                total_price = total_price * Decimal('0.91')  # 9% discount
        
        # Create order
        order = Order(
            customer_email=data['email'],
            product_id=data['product_id'],
            vendor_id=data['vendor_id'],
            quantity=data['quantity'],
            unit_price=unit_price,
            total_price=total_price,
            payment_method=data['payment_method'],
            coupon_code=coupon_code,
            subscribe_newsletter=data.get('subscribe_newsletter', False),
            status='pending'
        )
        
        db.session.add(order)
        
        # Update stock
        product_vendor.stock -= data['quantity']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Order created successfully',
            'data': order.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get order by ID"""
    try:
        order = Order.query.get_or_404(order_id)
        
        return jsonify({
            'success': True,
            'data': order.to_dict()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500


@orders_bp.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    """Update order status"""
    try:
        data = request.get_json()
        
        if 'status' not in data:
            return jsonify({
                'success': False,
                'message': 'Status is required'
            }), 400
        
        # Validate status
        valid_statuses = ['pending', 'processing', 'completed', 'cancelled', 'failed']
        if data['status'] not in valid_statuses:
            return jsonify({
                'success': False,
                'message': f'Invalid status. Must be one of: {", ".join(valid_statuses)}'
            }), 400
        
        order = Order.query.get_or_404(order_id)
        order.status = data['status']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Order status updated successfully',
            'data': order.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders with optional filtering"""
    try:
        # Get query parameters
        status = request.args.get('status')
        email = request.args.get('email')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        # Build query
        query = Order.query
        
        if status:
            query = query.filter(Order.status == status)
        
        if email:
            query = query.filter(Order.customer_email.ilike(f'%{email}%'))
        
        # Order by creation date (newest first)
        query = query.order_by(Order.created_at.desc())
        
        # Paginate
        orders = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        
        return jsonify({
            'success': True,
            'data': [order.to_dict() for order in orders.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': orders.total,
                'pages': orders.pages,
                'has_next': orders.has_next,
                'has_prev': orders.has_prev
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

