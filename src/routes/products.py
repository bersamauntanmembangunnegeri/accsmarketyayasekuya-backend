from flask import Blueprint, jsonify, request
from src.models.user import db
from src.models.product import Product
from src.models.vendor import ProductVendor

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    """Get all products with optional filtering"""
    try:
        # Get query parameters
        category_id = request.args.get('category_id', type=int)
        search = request.args.get('search', '')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # Build query
        query = Product.query.filter_by(is_active=True)
        
        if category_id:
            query = query.filter_by(category_id=category_id)
        
        if search:
            query = query.filter(Product.name.contains(search))
        
        # Paginate results
        products = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        products_data = [product.to_dict() for product in products.items]
        
        return jsonify({
            'success': True,
            'data': products_data,
            'pagination': {
                'page': products.page,
                'pages': products.pages,
                'per_page': products.per_page,
                'total': products.total
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get single product by ID"""
    try:
        product = Product.query.get_or_404(product_id)
        
        return jsonify({
            'success': True,
            'data': product.to_dict()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@products_bp.route('/products/<int:product_id>/vendors', methods=['GET'])
def get_product_vendors(product_id):
    """Get vendors for a specific product"""
    try:
        product = Product.query.get_or_404(product_id)
        
        vendors = ProductVendor.query.filter_by(
            product_id=product_id,
            is_active=True
        ).all()
        
        vendors_data = [vendor.to_dict() for vendor in vendors]
        
        return jsonify({
            'success': True,
            'data': {
                'product': product.to_dict(),
                'vendors': vendors_data
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@products_bp.route('/search', methods=['GET'])
def search_products():
    """Search products by name or description"""
    try:
        query = request.args.get('q', '')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        if not query:
            return jsonify({
                'success': False,
                'message': 'Search query is required'
            }), 400
        
        # Search in name and description
        products = Product.query.filter(
            db.or_(
                Product.name.contains(query),
                Product.description.contains(query)
            ),
            Product.is_active == True
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        
        products_data = [product.to_dict() for product in products.items]
        
        return jsonify({
            'success': True,
            'data': products_data,
            'pagination': {
                'page': products.page,
                'pages': products.pages,
                'per_page': products.per_page,
                'total': products.total
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

