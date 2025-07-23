import os
import sys
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
            print("Seeding initial data...")
            
            # Create categories
            fb_category = Category(name="Facebook Accounts", slug="facebook-accounts", description="High-quality Facebook accounts for various purposes")
            ig_category = Category(name="Instagram Accounts", slug="instagram-accounts", description="Premium Instagram accounts with various features")
            
            db.session.add_all([fb_category, ig_category])
            db.session.commit()

            # Create sub-categories
            fb_softregs = Category(name="Facebook Softregs", slug="facebook-softregs", description="Facebook accounts registered with software", parent_id=fb_category.id)
            fb_friends = Category(name="Facebook With friends", slug="facebook-with-friends", description="Facebook accounts with existing friends", parent_id=fb_category.id)
            ig_softreg = Category(name="Instagram Softreg", slug="instagram-softreg", description="Instagram accounts registered with software", parent_id=ig_category.id)
            ig_aged = Category(name="Instagram Aged", slug="instagram-aged", description="Aged Instagram accounts", parent_id=ig_category.id)

            db.session.add_all([fb_softregs, fb_friends, ig_softreg, ig_aged])
            db.session.commit()

            # Create products
            product1 = Product(
                category_id=fb_softregs.id,
                name="FB Accounts | Verified by e-mail, there is no email in the set. Male or female. The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Cookies are included. Accounts are registered in United Kingdom IP.",
                description="High quality Facebook accounts verified by email",
                base_price=0.278,
                stock_quantity=345,
                rating=4.6,
                return_rate=2.1,
                delivery_time="48h",
                is_active=True
            )
            product2 = Product(
                category_id=fb_softregs.id,
                name="FB Accounts | Verified by email (email not included). Male or female. The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Registered from USA IP.",
                description="Facebook soft registered accounts from USA",
                base_price=0.296,
                stock_quantity=1648,
                rating=4.8,
                return_rate=2.7,
                delivery_time="48h",
                is_active=True
            )
            product3 = Product(
                category_id=fb_friends.id,
                name="FB Accounts | The number of subscribers is 50+. Verified by e-mail, there is no email in the set. Male and female. The account profiles may be empty or have limited entries such as photos and other information. 2FA in the set. Token are included in the package. Accounts are registered in Bangladesh IP.",
                description="Facebook accounts with 50+ subscribers",
                base_price=0.999,
                stock_quantity=27,
                rating=4.6,
                return_rate=0.7,
                delivery_time="48h",
                is_active=True
            )
            product4 = Product(
                category_id=ig_softreg.id,
                name="IG Accounts | Verified by email, email NOT included. Male or female. The profiles information is partially filled. 2FA included. UserAgent, cookies included. Registered from USA IP.",
                description="Instagram soft registered accounts from USA",
                base_price=0.183,
                stock_quantity=99,
                rating=4.9,
                return_rate=1.6,
                delivery_time="48h",
                is_active=True
            )
            product5 = Product(
                category_id=ig_aged.id,
                name="IG Accounts | Aged accounts 2019-2021. Verified by email, email NOT included. Male or female. The profiles information is partially filled. 2FA included. UserAgent, cookies included. Registered from USA IP.",
                description="Aged Instagram accounts from USA",
                base_price=0.699,
                stock_quantity=524,
                rating=4.9,
                return_rate=2.0,
                delivery_time="48h",
                is_active=True
            )

            db.session.add_all([product1, product2, product3, product4, product5])
            db.session.commit()

            # Create vendors and product-vendor relationships
            vendor1 = Vendor(name="Vendor A", rating=4.5)
            vendor2 = Vendor(name="Vendor B", rating=4.7)
            db.session.add_all([vendor1, vendor2])
            db.session.commit()

            product_vendor1 = ProductVendor(product_id=product1.id, vendor_id=vendor1.id, price=product1.base_price, stock=product1.stock_quantity, is_active=True)
            product_vendor2 = ProductVendor(product_id=product2.id, vendor_id=vendor1.id, price=product2.base_price, stock=product2.stock_quantity, is_active=True)
            product_vendor3 = ProductVendor(product_id=product3.id, vendor_id=vendor2.id, price=product3.base_price, stock=product3.stock_quantity, is_active=True)
            product_vendor4 = ProductVendor(product_id=product4.id, vendor_id=vendor1.id, price=product4.base_price, stock=product4.stock_quantity, is_active=True)
            product_vendor5 = ProductVendor(product_id=product5.id, vendor_id=vendor2.id, price=product5.base_price, stock=product5.stock_quantity, is_active=True)

            db.session.add_all([product_vendor1, product_vendor2, product_vendor3, product_vendor4, product_vendor5])
            db.session.commit()
            print("Initial data seeded successfully.")
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