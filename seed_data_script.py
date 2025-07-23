#!/usr/bin/env python3
"""
Seed data script for AccsMarket database
Run this script to populate the database with initial data
"""
import os
import sys
import json

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.main import app, db
from src.models.category import Category
from src.models.product import Product
from src.models.vendor import Vendor

def seed_data():
    """Seed the database with initial data from JSON files"""
    with app.app_context():
        # Check if categories already exist
        if Category.query.count() == 0:
            print("Seeding initial data from JSON files...")
            
            data_dir = os.path.join(os.path.dirname(__file__), 'src', 'data')

            # Create categories
            with open(os.path.join(data_dir, 'categories.json'), 'r') as f:
                categories_data = json.load(f)
            
            category_map = {}
            for cat_data in categories_data:
                category = Category(name=cat_data['name'], slug=cat_data['slug'], description=cat_data['description'])
                db.session.add(category)
                db.session.flush()  # To get the ID for parent_id
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
                    category_map[sub_cat_data['slug']] = subcategory  # Add subcategory to map as well
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

            print("Initial data seeded from JSON files successfully.")
        else:
            print("Database already contains data. Skipping seeding.")

if __name__ == '__main__':
    seed_data()

