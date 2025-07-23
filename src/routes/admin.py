from flask import Blueprint, jsonify, request
from datetime import datetime
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


# Site Settings CRUD
@admin_bp.route('/settings', methods=['GET'])
def admin_get_settings():
    """Get all site settings"""
    try:
        settings = SiteSetting.query.all()
        return jsonify({
            'success': True,
            'data': [setting.to_dict() for setting in settings]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/settings', methods=['POST'])
def admin_create_setting():
    """Create new site setting"""
    try:
        data = request.get_json()
        
        setting = SiteSetting(
            key=data['key'],
            value=data['value'],
            description=data.get('description')
        )
        
        db.session.add(setting)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Setting created successfully',
            'data': setting.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/settings/<int:setting_id>', methods=['PUT'])
def admin_update_setting(setting_id):
    """Update site setting"""
    try:
        setting = SiteSetting.query.get_or_404(setting_id)
        data = request.get_json()
        
        setting.key = data.get('key', setting.key)
        setting.value = data.get('value', setting.value)
        setting.description = data.get('description', setting.description)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Setting updated successfully',
            'data': setting.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/settings/<int:setting_id>', methods=['DELETE'])
def admin_delete_setting(setting_id):
    """Delete site setting"""
    try:
        setting = SiteSetting.query.get_or_404(setting_id)
        db.session.delete(setting)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Setting deleted successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

# Pages CRUD
@admin_bp.route('/pages', methods=['GET'])
def admin_get_pages():
    """Get all pages"""
    try:
        pages = Page.query.all()
        return jsonify({
            'success': True,
            'data': [page.to_dict() for page in pages]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/pages', methods=['POST'])
def admin_create_page():
    """Create new page"""
    try:
        data = request.get_json()
        
        page = Page(
            title=data['title'],
            slug=data['slug'],
            content=data.get('content'),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(page)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Page created successfully',
            'data': page.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/pages/<int:page_id>', methods=['PUT'])
def admin_update_page(page_id):
    """Update page"""
    try:
        page = Page.query.get_or_404(page_id)
        data = request.get_json()
        
        page.title = data.get('title', page.title)
        page.slug = data.get('slug', page.slug)
        page.content = data.get('content', page.content)
        page.is_active = data.get('is_active', page.is_active)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Page updated successfully',
            'data': page.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/pages/<int:page_id>', methods=['DELETE'])
def admin_delete_page(page_id):
    """Delete page"""
    try:
        page = Page.query.get_or_404(page_id)
        db.session.delete(page)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Page deleted successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500



# Header Management APIs
@admin_bp.route('/header', methods=['GET'])
def admin_get_header_settings():
    """Get header settings (logo, navigation menu, search settings)"""
    try:
        # Get header-related settings
        header_keys = ['header_logo_url', 'header_logo_alt', 'navigation_menu', 'search_placeholder', 'search_enabled']
        header_settings = {}
        
        for key in header_keys:
            setting = SiteSetting.query.filter_by(key=key).first()
            if setting:
                header_settings[key] = setting.value
            else:
                # Default values
                defaults = {
                    'header_logo_url': '',
                    'header_logo_alt': 'AccsMarket',
                    'navigation_menu': '[{"label": "Home", "url": "/", "active": true}, {"label": "News", "url": "/news", "active": true}, {"label": "FAQ", "url": "/faq", "active": true}, {"label": "Terms of use", "url": "/terms", "active": true}]',
                    'search_placeholder': 'Search for accounts',
                    'search_enabled': 'true'
                }
                header_settings[key] = defaults.get(key, '')
        
        return jsonify({
            'success': True,
            'data': header_settings
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/header', methods=['PUT'])
def admin_update_header_settings():
    """Update header settings"""
    try:
        data = request.get_json()
        
        # Update or create header settings
        for key, value in data.items():
            if key in ['header_logo_url', 'header_logo_alt', 'navigation_menu', 'search_placeholder', 'search_enabled']:
                setting = SiteSetting.query.filter_by(key=key).first()
                if setting:
                    setting.value = str(value)
                    setting.updated_at = datetime.utcnow()
                else:
                    # Create new setting
                    descriptions = {
                        'header_logo_url': 'URL of the header logo image',
                        'header_logo_alt': 'Alt text for the header logo',
                        'navigation_menu': 'JSON array of navigation menu items',
                        'search_placeholder': 'Placeholder text for search input',
                        'search_enabled': 'Whether search functionality is enabled (true/false)'
                    }
                    setting = SiteSetting(
                        key=key,
                        value=str(value),
                        description=descriptions.get(key, f'Header setting: {key}')
                    )
                    db.session.add(setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Header settings updated successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/header/logo', methods=['POST'])
def admin_upload_logo():
    """Upload header logo (placeholder for file upload)"""
    try:
        # This is a placeholder for file upload functionality
        # In a real implementation, you would handle file upload here
        data = request.get_json()
        logo_url = data.get('logo_url', '')
        logo_alt = data.get('logo_alt', 'AccsMarket')
        
        # Update logo settings
        logo_url_setting = SiteSetting.query.filter_by(key='header_logo_url').first()
        if logo_url_setting:
            logo_url_setting.value = logo_url
            logo_url_setting.updated_at = datetime.utcnow()
        else:
            logo_url_setting = SiteSetting(
                key='header_logo_url',
                value=logo_url,
                description='URL of the header logo image'
            )
            db.session.add(logo_url_setting)
        
        logo_alt_setting = SiteSetting.query.filter_by(key='header_logo_alt').first()
        if logo_alt_setting:
            logo_alt_setting.value = logo_alt
            logo_alt_setting.updated_at = datetime.utcnow()
        else:
            logo_alt_setting = SiteSetting(
                key='header_logo_alt',
                value=logo_alt,
                description='Alt text for the header logo'
            )
            db.session.add(logo_alt_setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Logo updated successfully',
            'data': {
                'logo_url': logo_url,
                'logo_alt': logo_alt
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/header/navigation', methods=['PUT'])
def admin_update_navigation():
    """Update navigation menu"""
    try:
        data = request.get_json()
        menu_items = data.get('menu_items', [])
        
        # Validate menu items structure
        for item in menu_items:
            if not all(key in item for key in ['label', 'url']):
                return jsonify({
                    'success': False,
                    'message': 'Each menu item must have label and url'
                }), 400
        
        # Convert to JSON string
        import json
        menu_json = json.dumps(menu_items)
        
        # Update navigation menu setting
        nav_setting = SiteSetting.query.filter_by(key='navigation_menu').first()
        if nav_setting:
            nav_setting.value = menu_json
            nav_setting.updated_at = datetime.utcnow()
        else:
            nav_setting = SiteSetting(
                key='navigation_menu',
                value=menu_json,
                description='JSON array of navigation menu items'
            )
            db.session.add(nav_setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Navigation menu updated successfully',
            'data': menu_items
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/header/search', methods=['PUT'])
def admin_update_search_settings():
    """Update search settings"""
    try:
        data = request.get_json()
        search_enabled = data.get('search_enabled', True)
        search_placeholder = data.get('search_placeholder', 'Search for accounts')
        
        # Update search enabled setting
        enabled_setting = SiteSetting.query.filter_by(key='search_enabled').first()
        if enabled_setting:
            enabled_setting.value = str(search_enabled).lower()
            enabled_setting.updated_at = datetime.utcnow()
        else:
            enabled_setting = SiteSetting(
                key='search_enabled',
                value=str(search_enabled).lower(),
                description='Whether search functionality is enabled (true/false)'
            )
            db.session.add(enabled_setting)
        
        # Update search placeholder setting
        placeholder_setting = SiteSetting.query.filter_by(key='search_placeholder').first()
        if placeholder_setting:
            placeholder_setting.value = search_placeholder
            placeholder_setting.updated_at = datetime.utcnow()
        else:
            placeholder_setting = SiteSetting(
                key='search_placeholder',
                value=search_placeholder,
                description='Placeholder text for search input'
            )
            db.session.add(placeholder_setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Search settings updated successfully',
            'data': {
                'search_enabled': search_enabled,
                'search_placeholder': search_placeholder
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

