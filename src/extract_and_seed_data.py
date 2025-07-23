import os
import sys
from flask import Flask

# DON\"T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models.user import db
from src.models.category import Category
from src.models.product import Product

# Configure Flask app for database access
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(os.path.dirname(__file__), r'database', r'app.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Data kategori dan subkategori dari AccsMarket.com (diperbarui)
categories_data = [
    {
        "name": "Facebook Accounts",
        "slug": "facebook-accounts",
        "description": "Facebook social media accounts",
        "subcategories": [
            {"name": "Facebook Softregs", "slug": "facebook-softregs", "description": "Facebook soft-registered accounts"},
            {"name": "Facebook With friends", "slug": "facebook-with-friends", "description": "Facebook accounts with friends"},
            {"name": "Facebook Aged", "slug": "facebook-aged", "description": "Facebook aged accounts"},
            {"name": "Facebook With friends and age", "slug": "facebook-with-friends-and-age", "description": "Facebook accounts with friends and age"},
            {"name": "Facebook For advertising", "slug": "facebook-for-advertising", "description": "Facebook accounts for advertising"}
        ]
    },
    {
        "name": "Instagram Accounts",
        "slug": "instagram-accounts",
        "description": "Instagram social media accounts",
        "subcategories": [
            {"name": "Instagram Softreg", "slug": "instagram-softreg", "description": "Instagram soft-registered accounts"},
            {"name": "Instagram Aged", "slug": "instagram-aged", "description": "Instagram aged accounts"},
            {"name": "Instagram With Followers", "slug": "instagram-with-followers", "description": "Instagram accounts with followers"},
            {"name": "Instagram Boost followers", "slug": "instagram-boost-followers", "description": "Instagram follower boost services"},
            {"name": "Instagram Boost likes", "slug": "instagram-boost-likes", "description": "Instagram like boost services"},
            {"name": "Instagram Boost comments", "slug": "instagram-boost-comments", "description": "Instagram comment boost services"},
            {"name": "Instagram Boost video views", "slug": "instagram-boost-video-views", "description": "Instagram video view boost services"}
        ]
    },
    {
        "name": "VKontakte Accounts",
        "slug": "vkontakte-accounts",
        "description": "VKontakte social media accounts",
        "subcategories": [
            {"name": "VKontakte Softreg", "slug": "vkontakte-softreg", "description": "VKontakte soft-registered accounts"},
            {"name": "VKontakte Boosted", "slug": "vkontakte-boosted", "description": "VKontakte boosted accounts"}
        ]
    },
    {
        "name": "GMail Accounts",
        "slug": "gmail-accounts",
        "description": "Gmail email accounts",
        "subcategories": [
            {"name": "GMail Softreg", "slug": "gmail-softreg", "description": "Gmail soft-registered accounts"},
            {"name": "GMail Aged", "slug": "gmail-aged", "description": "Gmail aged accounts"}
        ]
    },
    {
        "name": "Twitter Accounts",
        "slug": "twitter-accounts",
        "description": "Twitter social media accounts",
        "subcategories": [
            {"name": "Twitter Softreg", "slug": "twitter-softreg", "description": "Twitter soft-registered accounts"},
            {"name": "Twitter Aged", "slug": "twitter-aged", "description": "Twitter aged accounts"},
            {"name": "Twitter Boosted", "slug": "twitter-boosted", "description": "Twitter boosted accounts"},
            {"name": "Twitter Boost subscribers", "slug": "twitter-boost-subscribers", "description": "Twitter subscriber boost services"},
            {"name": "Twitter Boost likes", "slug": "twitter-boost-likes", "description": "Twitter like boost services"},
            {"name": "Twitter Boost Retweets", "slug": "twitter-boost-retweets", "description": "Twitter retweet boost services"}
        ]
    },
    {
        "name": "TikTok Accounts",
        "slug": "tiktok-accounts",
        "description": "TikTok social media accounts",
        "subcategories": [
            {"name": "TikTok Softreg", "slug": "tiktok-softreg", "description": "TikTok soft-registered accounts"},
            {"name": "TikTok Aged", "slug": "tiktok-aged", "description": "TikTok aged accounts"},
            {"name": "TikTok With Followers", "slug": "tiktok-with-followers", "description": "TikTok accounts with followers"}
        ]
    },
    {
        "name": "Social Networks",
        "slug": "social-networks",
        "description": "Other social network accounts",
        "subcategories": [
            {"name": "Social Networks AI accounts", "slug": "social-networks-ai-accounts", "description": "AI-related social network accounts"},
            {"name": "Social Networks Marketplace", "slug": "social-networks-marketplace", "description": "Marketplace social network accounts"},
            {"name": "Social Networks Snapchat", "slug": "social-networks-snapchat", "description": "Snapchat social network accounts"},
            {"name": "Social Networks Twitch", "slug": "social-networks-twitch", "description": "Twitch social network accounts"},
            {"name": "Social Networks Yelp", "slug": "social-networks-yelp", "description": "Yelp social network accounts"},
            {"name": "Social Networks Quora", "slug": "social-networks-quora", "description": "Quora social network accounts"}
        ]
    }
]

def seed_accsmarket_data():
    with app.app_context():
        print("Seeding AccsMarket data...")
        
        # Clear existing data
        Category.query.delete()
        Product.query.delete()
        db.session.commit()
        
        # Add categories and subcategories
        for cat_data in categories_data:
            # Create main category
            category = Category(
                name=cat_data["name"],
                slug=cat_data["slug"],
                description=cat_data["description"],
                parent_id=None,
                is_active=True
            )
            db.session.add(category)
            db.session.flush()  # Get the ID
            
            # Create subcategories
            for subcat_data in cat_data["subcategories"]:
                subcategory = Category(
                    name=subcat_data["name"],
                    slug=subcat_data["slug"],
                    description=subcat_data["description"],
                    parent_id=category.id,
                    is_active=True
                )
                db.session.add(subcategory)
        
        db.session.commit()
        
        # Count results
        total_categories = Category.query.filter(Category.parent_id == None).count()
        total_subcategories = Category.query.filter(Category.parent_id != None).count()
        total_products = Product.query.count()
        
        print(f"Data seeding completed!")
        print(f"Total Categories: {total_categories}")
        print(f"Total Subcategories: {total_subcategories}")
        print(f"Total Products: {total_products}")

if __name__ == "__main__":
    seed_accsmarket_data()

