import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models.user import db
from src.models.category import Category
from src.models.product import Product
from src.models.vendor import Vendor, ProductVendor
from src.models.order import Order
from src.models.settings import SiteSetting, Page
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def seed_data():
    app = create_app()
    
    with app.app_context():
        # Import all models to ensure they are registered
        from src.models.category import Category
        from src.models.product import Product
        from src.models.vendor import Vendor, ProductVendor
        from src.models.order import Order
        from src.models.settings import SiteSetting, Page
        
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create categories
        facebook_accounts = Category(
            name="Facebook Accounts",
            slug="facebook-accounts",
            description="Facebook account categories"
        )
        db.session.add(facebook_accounts)
        db.session.flush()
        
        # Facebook subcategories
        fb_softregs = Category(
            name="Facebook Softregs",
            slug="facebook-softregs",
            description="Facebook soft registered accounts",
            parent_id=facebook_accounts.id
        )
        
        fb_with_friends = Category(
            name="Facebook With friends",
            slug="facebook-with-friends",
            description="Facebook accounts with friends",
            parent_id=facebook_accounts.id
        )
        
        fb_aged = Category(
            name="Facebook Aged",
            slug="facebook-aged",
            description="Aged Facebook accounts",
            parent_id=facebook_accounts.id
        )
        
        fb_for_ads = Category(
            name="Facebook For advertising",
            slug="facebook-for-advertising",
            description="Facebook accounts for advertising",
            parent_id=facebook_accounts.id
        )
        
        # Instagram categories
        instagram_accounts = Category(
            name="Instagram Accounts",
            slug="instagram-accounts",
            description="Instagram account categories"
        )
        
        db.session.add_all([fb_softregs, fb_with_friends, fb_aged, fb_for_ads, instagram_accounts])
        db.session.flush()
        
        # Instagram subcategories
        ig_softregs = Category(
            name="Instagram Softreg",
            slug="instagram-softreg",
            description="Instagram soft registered accounts",
            parent_id=instagram_accounts.id
        )
        
        ig_aged = Category(
            name="Instagram Aged",
            slug="instagram-aged",
            description="Aged Instagram accounts",
            parent_id=instagram_accounts.id
        )
        
        ig_with_followers = Category(
            name="Instagram With Followers",
            slug="instagram-with-followers",
            description="Instagram accounts with followers",
            parent_id=instagram_accounts.id
        )
        
        db.session.add_all([ig_softregs, ig_aged, ig_with_followers])
        db.session.flush()
        
        # Create vendors
        vendors_data = [
            {"name": "Partner #2401", "rating": 4.6, "total_sales": 345},
            {"name": "Partner #1892", "rating": 4.8, "total_sales": 1648},
            {"name": "Partner #3456", "rating": 4.9, "total_sales": 1175},
            {"name": "Partner #7890", "rating": 5.0, "total_sales": 54},
        ]
        
        vendors = []
        for vendor_data in vendors_data:
            vendor = Vendor(**vendor_data)
            vendors.append(vendor)
            db.session.add(vendor)
        
        db.session.flush()
        
        # Create products
        products_data = [
            {
                "category_id": fb_softregs.id,
                "name": "FB Accounts | Verified by e-mail, there is no email in the set. Male or female. The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Cookies are included. Accounts are registered in United Kingdom IP.",
                "description": "High quality Facebook accounts verified by email",
                "base_price": 0.278,
                "stock_quantity": 345,
                "rating": 4.6,
                "return_rate": 2.1,
                "delivery_time": "48h"
            },
            {
                "category_id": fb_softregs.id,
                "name": "FB Accounts | Verified by email (email not included). Male or female. The account profiles may be empty or have limited entries such as photos and other information. 2FA included. Registered from USA IP.",
                "description": "USA registered Facebook accounts",
                "base_price": 0.296,
                "stock_quantity": 1648,
                "rating": 4.8,
                "return_rate": 2.7,
                "delivery_time": "48h"
            },
            {
                "category_id": fb_with_friends.id,
                "name": "FB Accounts | The number of subscribers is 50+. Verified by e-mail, there is no email in the set. Male and female. The account profiles may be empty or have limited entries such as photos and other information. 2FA in the set. Token are included in the package. Accounts are registered in Bangladesh IP.",
                "description": "Facebook accounts with 50+ friends",
                "base_price": 0.999,
                "stock_quantity": 27,
                "rating": 4.6,
                "return_rate": 0.7,
                "delivery_time": "48h"
            },
            {
                "category_id": ig_softregs.id,
                "name": "IG Accounts | Verified by email, email NOT included. Male or female. The profiles information is partially filled. 2FA included. UserAgent, cookies included. Registered from USA IP.",
                "description": "Instagram soft registered accounts from USA",
                "base_price": 0.183,
                "stock_quantity": 99,
                "rating": 4.9,
                "return_rate": 1.6,
                "delivery_time": "48h"
            },
            {
                "category_id": ig_aged.id,
                "name": "IG Accounts | Aged accounts 2019-2021. Verified by email, email NOT included. Male or female. The profiles information is partially filled. 2FA included. UserAgent, cookies included. Registered from USA IP.",
                "description": "Aged Instagram accounts 2019-2021",
                "base_price": 0.699,
                "stock_quantity": 524,
                "rating": 4.9,
                "return_rate": 2.0,
                "delivery_time": "48h"
            }
        ]
        
        products = []
        for product_data in products_data:
            product = Product(**product_data)
            products.append(product)
            db.session.add(product)
        
        db.session.flush()
        
        # Create product-vendor relationships
        for i, product in enumerate(products):
            # Each product has 1-3 vendors
            vendor_count = min(len(vendors), (i % 3) + 1)
            for j in range(vendor_count):
                vendor = vendors[j]
                price_variation = 1 + (j * 0.05)  # Small price variation per vendor
                
                product_vendor = ProductVendor(
                    product_id=product.id,
                    vendor_id=vendor.id,
                    price=product.base_price * price_variation,
                    stock=product.stock_quantity // vendor_count
                )
                db.session.add(product_vendor)
        
        # Create site settings
        settings_data = [
            {"key": "site_title", "value": "AccsMarket - Social Media Accounts Store", "description": "Site title"},
            {"key": "site_description", "value": "Buy or Sell Social Media Accounts (PVA & Cheap)", "description": "Site description"},
            {"key": "contact_email", "value": "support@accsmarket.com", "description": "Contact email"},
            {"key": "news_url", "value": "https://accsmarket.news", "description": "News website URL"},
        ]
        
        for setting_data in settings_data:
            setting = SiteSetting(**setting_data)
            db.session.add(setting)
        
        # Create pages
        pages_data = [
            {
                "title": "Terms of Use",
                "slug": "terms-of-use",
                "content": "Terms of use content here..."
            },
            {
                "title": "FAQ",
                "slug": "faq",
                "content": "Frequently asked questions content here..."
            },
            {
                "title": "Privacy Policy",
                "slug": "privacy-policy",
                "content": "Privacy policy content here..."
            }
        ]
        
        for page_data in pages_data:
            page = Page(**page_data)
            db.session.add(page)
        
        db.session.commit()
        print("Seed data created successfully!")

if __name__ == '__main__':
    seed_data()

