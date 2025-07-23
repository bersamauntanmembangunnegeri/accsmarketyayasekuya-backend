from flask import Blueprint, jsonify, request
from src.models.user import db
from src.models.category import Category
from src.models.product import Product
from src.models.vendor import Vendor, ProductVendor
from src.models.order import Order
from src.models.settings import SiteSetting, Page

admin_bp = Blueprint('admin', __name__)

# Categories CRUD
@admin_bp.route('/categories', methods=['GET'])
def admin_get_categories():
    """Get all categories for admin"""
    try:
        categories = Category.query.all()
        return jsonify({
            'success': True,
            'data': [category.to_dict() for category in categories]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/categories', methods=['POST'])
def admin_create_category():
    """Create new category"""
    try:
        data = request.get_json()
        
        category = Category(
            name=data['name'],
            slug=data['slug'],
            description=data.get('description'),
            parent_id=data.get('parent_id'),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(category)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Category created successfully',
            'data': category.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/categories/<int:category_id>', methods=['PUT'])
def admin_update_category(category_id):
    """Update category"""
    try:
        category = Category.query.get_or_404(category_id)
        data = request.get_json()
        
        category.name = data.get('name', category.name)
        category.slug = data.get('slug', category.slug)
        category.description = data.get('description', category.description)
        category.parent_id = data.get('parent_id', category.parent_id)
        category.is_active = data.get('is_active', category.is_active)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Category updated successfully',
            'data': category.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def admin_delete_category(category_id):
    """Delete category"""
    try:
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Category deleted successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

# Products CRUD
@admin_bp.route('/products', methods=['GET'])
def admin_get_products():
    """Get all products for admin"""
    try:
        products = Product.query.all()
        return jsonify({
            'success': True,
            'data': [product.to_dict() for product in products]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/products', methods=['POST'])
def admin_create_product():
    """Create new product"""
    try:
        data = request.get_json()
        
        product = Product(
            category_id=data['category_id'],
            name=data['name'],
            description=data.get('description'),
            base_price=data['base_price'],
            stock_quantity=data.get('stock_quantity', 0),
            rating=data.get('rating', 0),
            return_rate=data.get('return_rate', 0),
            delivery_time=data.get('delivery_time', '48h'),
            image_url=data.get('image_url'),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Product created successfully',
            'data': product.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/products/<int:product_id>', methods=['PUT'])
def admin_update_product(product_id):
    """Update product"""
    try:
        product = Product.query.get_or_404(product_id)
        data = request.get_json()
        
        product.category_id = data.get('category_id', product.category_id)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.base_price = data.get('base_price', product.base_price)
        product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
        product.rating = data.get('rating', product.rating)
        product.return_rate = data.get('return_rate', product.return_rate)
        product.delivery_time = data.get('delivery_time', product.delivery_time)
        product.image_url = data.get('image_url', product.image_url)
        product.is_active = data.get('is_active', product.is_active)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Product updated successfully',
            'data': product.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/products/<int:product_id>', methods=['DELETE'])
def admin_delete_product(product_id):
    """Delete product"""
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Product deleted successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

# Orders management
@admin_bp.route('/orders', methods=['GET'])
def admin_get_orders():
    """Get all orders for admin"""
    try:
        orders = Order.query.order_by(Order.created_at.desc()).all()
        return jsonify({
            'success': True,
            'data': [order.to_dict() for order in orders]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# Dashboard stats
@admin_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    """Get dashboard statistics"""
    try:
        total_products = Product.query.count()
        total_orders = Order.query.count()
        total_categories = Category.query.count()
        
        recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
        
        return jsonify({
            'success': True,
            'data': {
                'stats': {
                    'total_products': total_products,
                    'total_orders': total_orders,
                    'total_categories': total_categories
                },
                'recent_orders': [order.to_dict() for order in recent_orders]
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

