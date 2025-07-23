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
    """Get header settings (news bar, logo, navigation menu, search settings)"""
    try:
        # Get header-related settings
        header_keys = [
            'header_newsbar_enabled', 'header_newsbar_text', 'header_newsbar_bg_color', 
            'header_newsbar_text_color', 'header_newsbar_url',
            'header_logo_url', 'header_logo_alt', 'header_logo_text', 'header_logo_suffix',
            'navigation_menu', 'search_placeholder', 'search_enabled', 'search_advanced_enabled'
        ]
        header_settings = {}
        
        for key in header_keys:
            setting = SiteSetting.query.filter_by(key=key).first()
            if setting:
                header_settings[key] = setting.value
            else:
                # Default values
                defaults = {
                    'header_newsbar_enabled': 'true',
                    'header_newsbar_text': 'News, promotions, coupons, announcements are published on our news site - accsmarket.news',
                    'header_newsbar_bg_color': '#22c55e',
                    'header_newsbar_text_color': '#ffffff',
                    'header_newsbar_url': 'accsmarket.news',
                    'header_logo_url': '',
                    'header_logo_alt': 'AccsMarket',
                    'header_logo_text': 'ACCS',
                    'header_logo_suffix': 'market.com',
                    'navigation_menu': '[{"id": 1, "label": "Home", "url": "/", "active": true}, {"id": 2, "label": "News", "url": "/news", "active": true}, {"id": 3, "label": "FAQ", "url": "/faq", "active": true}, {"id": 4, "label": "Terms of use", "url": "/terms", "active": true}]',
                    'search_placeholder': 'Search for accounts',
                    'search_enabled': 'true',
                    'search_advanced_enabled': 'true'
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
        
        # List of allowed header setting keys
        allowed_keys = [
            'header_newsbar_enabled', 'header_newsbar_text', 'header_newsbar_bg_color', 
            'header_newsbar_text_color', 'header_newsbar_url',
            'header_logo_url', 'header_logo_alt', 'header_logo_text', 'header_logo_suffix',
            'navigation_menu', 'search_placeholder', 'search_enabled', 'search_advanced_enabled'
        ]
        
        # Update or create header settings
        for key, value in data.items():
            if key in allowed_keys:
                setting = SiteSetting.query.filter_by(key=key).first()
                if setting:
                    setting.value = str(value)
                    setting.updated_at = datetime.utcnow()
                else:
                    # Create new setting
                    descriptions = {
                        'header_newsbar_enabled': 'Whether news bar is enabled (true/false)',
                        'header_newsbar_text': 'Text displayed in the news bar',
                        'header_newsbar_bg_color': 'Background color of the news bar',
                        'header_newsbar_text_color': 'Text color of the news bar',
                        'header_newsbar_url': 'URL for the news site',
                        'header_logo_url': 'URL of the header logo image',
                        'header_logo_alt': 'Alt text for the header logo',
                        'header_logo_text': 'Text part of the logo',
                        'header_logo_suffix': 'Suffix part of the logo',
                        'navigation_menu': 'JSON array of navigation menu items',
                        'search_placeholder': 'Placeholder text for search input',
                        'search_enabled': 'Whether search functionality is enabled (true/false)',
                        'search_advanced_enabled': 'Whether advanced search is enabled (true/false)'
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


# Footer Settings Endpoints
@admin_bp.route('/footer', methods=['GET'])
def admin_get_footer_settings():
    """Get footer settings (company info, links, contact info)"""
    try:
        # Get footer-related settings
        footer_keys = [
            'footer_logo_text', 'footer_logo_suffix', 'footer_company_name', 
            'footer_company_description', 'footer_social_link_1', 'footer_social_link_2', 
            'footer_social_link_3', 'footer_quick_links', 'footer_support_links', 
            'footer_contact_email', 'footer_contact_website', 'footer_contact_support_text',
            'footer_contact_security_text', 'footer_copyright_text', 'footer_payment_methods'
        ]
        footer_settings = {}
        
        for key in footer_keys:
            setting = SiteSetting.query.filter_by(key=key).first()
            if setting:
                footer_settings[key] = setting.value
            else:
                # Default values
                defaults = {
                    'footer_logo_text': 'ACCS',
                    'footer_logo_suffix': 'market.com',
                    'footer_company_name': 'ACCS market.com',
                    'footer_company_description': 'Buy or Sell Social Media Accounts (PVA & Cheap). Your trusted marketplace for social media accounts.',
                    'footer_social_link_1': '',
                    'footer_social_link_2': '',
                    'footer_social_link_3': '',
                    'footer_quick_links': '[]',
                    'footer_support_links': '[]',
                    'footer_contact_email': 'support@accsmarket.com',
                    'footer_contact_website': 'accsmarket.news',
                    'footer_contact_support_text': '24/7 Support Available',
                    'footer_contact_security_text': 'Secure Transactions',
                    'footer_copyright_text': '© 2024 AccsMarket.com. All rights reserved.',
                    'footer_payment_methods': '["BTC", "USDT", "ETH", "PayPal"]'
                }
                footer_settings[key] = defaults.get(key, '')
        
        return jsonify({
            'success': True,
            'data': footer_settings
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/footer', methods=['PUT'])
def admin_update_footer_settings():
    """Update footer settings"""
    try:
        data = request.get_json()
        
        # Update or create footer settings
        valid_keys = [
            'footer_logo_text', 'footer_logo_suffix', 'footer_company_name', 
            'footer_company_description', 'footer_social_link_1', 'footer_social_link_2', 
            'footer_social_link_3', 'footer_quick_links', 'footer_support_links', 
            'footer_contact_email', 'footer_contact_website', 'footer_contact_support_text',
            'footer_contact_security_text', 'footer_copyright_text', 'footer_payment_methods'
        ]
        
        for key, value in data.items():
            if key in valid_keys:
                setting = SiteSetting.query.filter_by(key=key).first()
                if setting:
                    setting.value = str(value)
                    setting.updated_at = datetime.utcnow()
                else:
                    # Create new setting
                    descriptions = {
                        'footer_logo_text': 'Footer logo text (e.g., ACCS)',
                        'footer_logo_suffix': 'Footer logo suffix (e.g., market.com)',
                        'footer_company_name': 'Company name displayed in footer',
                        'footer_company_description': 'Company description in footer',
                        'footer_social_link_1': 'First social media link',
                        'footer_social_link_2': 'Second social media link',
                        'footer_social_link_3': 'Third social media link',
                        'footer_quick_links': 'Quick links in footer (JSON array)',
                        'footer_support_links': 'Support links in footer (JSON array)',
                        'footer_contact_email': 'Contact email address',
                        'footer_contact_website': 'Contact website URL',
                        'footer_contact_support_text': 'Support availability text',
                        'footer_contact_security_text': 'Security information text',
                        'footer_copyright_text': 'Copyright text',
                        'footer_payment_methods': 'Payment methods (JSON array)'
                    }
                    setting = SiteSetting(
                        key=key,
                        value=str(value),
                        description=descriptions.get(key, f'Footer setting: {key}')
                    )
                    db.session.add(setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Footer settings updated successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/footer/company', methods=['PUT'])
def admin_update_footer_company():
    """Update footer company information"""
    try:
        data = request.get_json()
        
        company_fields = {
            'footer_logo_text': data.get('logo_text', ''),
            'footer_logo_suffix': data.get('logo_suffix', ''),
            'footer_company_name': data.get('company_name', ''),
            'footer_company_description': data.get('company_description', ''),
            'footer_social_link_1': data.get('social_link_1', ''),
            'footer_social_link_2': data.get('social_link_2', ''),
            'footer_social_link_3': data.get('social_link_3', '')
        }
        
        for key, value in company_fields.items():
            setting = SiteSetting.query.filter_by(key=key).first()
            if setting:
                setting.value = str(value)
                setting.updated_at = datetime.utcnow()
            else:
                descriptions = {
                    'footer_logo_text': 'Footer logo text',
                    'footer_logo_suffix': 'Footer logo suffix',
                    'footer_company_name': 'Company name',
                    'footer_company_description': 'Company description',
                    'footer_social_link_1': 'First social media link',
                    'footer_social_link_2': 'Second social media link',
                    'footer_social_link_3': 'Third social media link'
                }
                setting = SiteSetting(
                    key=key,
                    value=str(value),
                    description=descriptions[key]
                )
                db.session.add(setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Footer company information updated successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/footer/links', methods=['PUT'])
def admin_update_footer_links():
    """Update footer links (quick links and support links)"""
    try:
        data = request.get_json()
        
        # Handle quick links
        if 'quick_links' in data:
            quick_links_setting = SiteSetting.query.filter_by(key='footer_quick_links').first()
            if quick_links_setting:
                quick_links_setting.value = str(data['quick_links'])
                quick_links_setting.updated_at = datetime.utcnow()
            else:
                quick_links_setting = SiteSetting(
                    key='footer_quick_links',
                    value=str(data['quick_links']),
                    description='Quick links in footer (JSON array)'
                )
                db.session.add(quick_links_setting)
        
        # Handle support links
        if 'support_links' in data:
            support_links_setting = SiteSetting.query.filter_by(key='footer_support_links').first()
            if support_links_setting:
                support_links_setting.value = str(data['support_links'])
                support_links_setting.updated_at = datetime.utcnow()
            else:
                support_links_setting = SiteSetting(
                    key='footer_support_links',
                    value=str(data['support_links']),
                    description='Support links in footer (JSON array)'
                )
                db.session.add(support_links_setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Footer links updated successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/footer/contact', methods=['PUT'])
def admin_update_footer_contact():
    """Update footer contact information"""
    try:
        data = request.get_json()
        
        contact_fields = {
            'footer_contact_email': data.get('contact_email', ''),
            'footer_contact_website': data.get('contact_website', ''),
            'footer_contact_support_text': data.get('support_text', ''),
            'footer_contact_security_text': data.get('security_text', '')
        }
        
        for key, value in contact_fields.items():
            setting = SiteSetting.query.filter_by(key=key).first()
            if setting:
                setting.value = str(value)
                setting.updated_at = datetime.utcnow()
            else:
                descriptions = {
                    'footer_contact_email': 'Contact email address',
                    'footer_contact_website': 'Contact website URL',
                    'footer_contact_support_text': 'Support availability text',
                    'footer_contact_security_text': 'Security information text'
                }
                setting = SiteSetting(
                    key=key,
                    value=str(value),
                    description=descriptions[key]
                )
                db.session.add(setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Footer contact information updated successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@admin_bp.route('/footer/bottom', methods=['PUT'])
def admin_update_footer_bottom():
    """Update footer bottom section (copyright and payment methods)"""
    try:
        data = request.get_json()
        
        bottom_fields = {
            'footer_copyright_text': data.get('copyright_text', ''),
            'footer_payment_methods': data.get('payment_methods', '[]')
        }
        
        for key, value in bottom_fields.items():
            setting = SiteSetting.query.filter_by(key=key).first()
            if setting:
                setting.value = str(value)
                setting.updated_at = datetime.utcnow()
            else:
                descriptions = {
                    'footer_copyright_text': 'Copyright text',
                    'footer_payment_methods': 'Payment methods (JSON array)'
                }
                setting = SiteSetting(
                    key=key,
                    value=str(value),
                    description=descriptions[key]
                )
                db.session.add(setting)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Footer bottom section updated successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

