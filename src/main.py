import os
import sys
import json
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.category import Category
from src.models.product import Product
from src.models.vendor import Vendor, ProductVendor
from src.models.order import Order
from src.models.settings import SiteSetting, Page

from src.routes.user import user_bp
from src.routes.categories import categories_bp
from src.routes.products import products_bp
from src.routes.orders import orders_bp
from src.routes.admin import admin_bp
from src.routes.pages import pages_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(categories_bp, url_prefix='/api')
app.register_blueprint(products_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(pages_bp, url_prefix="/api")

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Function to seed initial data
def seed_data():
    with app.app_context():
        # Check if categories already exist
        if Category.query.count() == 0:
            print("Seeding initial data from JSON files...")
            
            data_dir = os.path.join(os.path.dirname(__file__), 'data')

            # Create categories
            with open(os.path.join(data_dir, 'categories.json'), 'r') as f:
                categories_data = json.load(f)
            
            category_map = {}
            for cat_data in categories_data:
                category = Category(name=cat_data['name'], slug=cat_data['slug'], description=cat_data['description'])
                db.session.add(category)
                db.session.flush() # To get the ID for parent_id
                category_map[cat_data['slug']] = category
            db.session.commit()

            # Create sub-categories
            with open(os.path.join(data_dir, 'subcategories.json'), 'r') as f:
                subcategories_data = json.load(f)
            
            for sub_cat_data in subcategories_data:
                parent_category = category_map.get(sub_cat_data['parent_slug'])
                if parent_category:
                    subcategory = Category(
                        name=sub_cat_data['name'],
                        slug=sub_cat_data['slug'],
                        description=sub_cat_data['description'],
                        parent_id=parent_category.id
                    )
                    db.session.add(subcategory)
                    category_map[sub_cat_data['slug']] = subcategory # Add subcategory to map as well
            db.session.commit()

            # Create products
            with open(os.path.join(data_dir, 'products.json'), 'r') as f:
                products_data = json.load(f)
            
            for prod_data in products_data:
                category = category_map.get(prod_data['category_slug'])
                if category:
                    product = Product(
                        category_id=category.id,
                        name=prod_data['name'],
                        description=prod_data['description'],
                        base_price=prod_data['base_price'],
                        stock_quantity=prod_data['stock_quantity'],
                        rating=prod_data['rating'],
                        return_rate=prod_data['return_rate'],
                        delivery_time=prod_data['delivery_time'],
                        is_active=prod_data['is_active']
                    )
                    db.session.add(product)
            db.session.commit()

            # Create vendors
            with open(os.path.join(data_dir, 'vendors.json'), 'r') as f:
                vendors_data = json.load(f)
            
            for vend_data in vendors_data:
                vendor = Vendor(name=vend_data['name'], rating=vend_data['rating'])
                db.session.add(vendor)
            db.session.commit()

            # Product-vendor relationships are not directly in JSON, as they depend on product/vendor IDs
            # For simplicity, we can skip seeding product-vendor relationships from JSON for now,
            # or add a more complex structure to products.json if needed.
            # For now, we'll assume products are directly linked to categories.

            print("Initial data seeded from JSON files successfully.")
        else:
            print("Database already contains data. Skipping seeding.")

@app.route("/admin", defaults={
    "path": ""
})
@app.route("/admin/<path:path>")
def serve_admin(path):
    admin_folder_path = os.path.join(app.static_folder, "admin")
    if path != "" and os.path.exists(os.path.join(admin_folder_path, path)):
        return send_from_directory(admin_folder_path, path)
    else:
        admin_index_path = os.path.join(admin_folder_path, "index.html")
        if os.path.exists(admin_index_path):
            return send_from_directory(admin_folder_path, "index.html")
        else:
            return "Admin interface not found", 404

@app.route("/admin-panel")
def serve_admin_panel():
    # Serve the main React app for admin panel
    index_path = os.path.join(app.static_folder, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(app.static_folder, "index.html")
    else:
        return "Admin panel not found", 404

@app.route("/", defaults={
    "path": ""
})
@app.route("/<path:path>")
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, "index.html")
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, "index.html")
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_data()
    app.run(host='0.0.0.0', port=5000, debug=True)