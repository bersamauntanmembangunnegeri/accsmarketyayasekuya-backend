#!/usr/bin/env python3
"""
Simple script to create database tables
"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import app, db

def create_tables():
    """Create all database tables"""
    print("Creating database tables...")
    
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            
            # Verify tables were created
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Created tables: {tables}")
            
            print("✅ Database tables created successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error creating tables: {e}")
            return False

if __name__ == "__main__":
    success = create_tables()
    if success:
        print("Database ready for seeding!")
        sys.exit(0)
    else:
        print("Database creation failed!")
        sys.exit(1)

