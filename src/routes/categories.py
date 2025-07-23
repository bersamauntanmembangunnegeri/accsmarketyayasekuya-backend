from flask import Blueprint, jsonify, request
from src.models.user import db
from src.models.category import Category

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories', methods=['GET'])
def get_categories():
    """Get all categories with hierarchical structure"""
    try:
        # Get only parent categories (no parent_id)
        parent_categories = Category.query.filter_by(parent_id=None, is_active=True).all()
        
        categories_data = []
        for category in parent_categories:
            category_dict = category.to_dict()
            categories_data.append(category_dict)
        
        return jsonify({
            'success': True,
            'data': categories_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@categories_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Get single category by ID"""
    try:
        category = Category.query.get_or_404(category_id)
        
        return jsonify({
            'success': True,
            'data': category.to_dict()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@categories_bp.route('/categories/<int:category_id>/products', methods=['GET'])
def get_category_products(category_id):
    """Get products by category"""
    try:
        from src.models.product import Product
        
        category = Category.query.get_or_404(category_id)
        
        # Get all child category IDs
        category_ids = [category_id]
        for child in category.children:
            category_ids.append(child.id)
        
        products = Product.query.filter(
            Product.category_id.in_(category_ids),
            Product.is_active == True
        ).all()
        
        products_data = [product.to_dict() for product in products]
        
        return jsonify({
            'success': True,
            'data': {
                'category': category.to_dict(),
                'products': products_data
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

