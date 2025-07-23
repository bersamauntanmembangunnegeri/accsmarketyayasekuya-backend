#!/usr/bin/env python3
"""
Database initialization script
Creates all tables based on SQLAlchemy models
"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import app, db
from models.category import Category
from models.product import Product
from models.vendor import Vendor
from models.order import Order
from models.settings import SiteSetting, Page

def init_database():
    """Initialize database and create all tables"""
    print("Initializing database...")
    
    with app.app_context():
        try:
            # Drop all tables first (for clean slate)
            print("Dropping existing tables...")
            db.drop_all()
            
            # Create all tables
            print("Creating tables...")
            db.create_all()
            
            # Verify tables were created
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Created tables: {tables}")
            
            print("Database initialization completed successfully!")
            return True
            
        except Exception as e:
            print(f"Error initializing database: {e}")
            return False

if __name__ == "__main__":
    success = init_database()
    if success:
        print("✅ Database ready for seeding!")
        sys.exit(0)
    else:
        print("❌ Database initialization failed!")
        sys.exit(1)

