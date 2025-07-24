#!/usr/bin/env python3.11
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Set the DATABASE_URL environment variable to force PostgreSQL usage
os.environ['DATABASE_URL'] = "postgresql://neondb_owner:npg_qk0XFbKCBAu5@ep-proud-meadow-ad220bo9-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

from main import app

if __name__ == '__main__':
    with app.app_context():
        # Ensure database is created and seeded on first run in deployment
        from src.models.category import Category
        from src.models.user import db
        
        print("Using PostgreSQL database...")
        print(f"Database URL: {os.environ.get('DATABASE_URL', 'Not set')}")
        
        try:
            # Create all tables
            db.create_all()
            print("Database tables created successfully.")
            
            # Check if we need to seed data
            if Category.query.count() == 0:
                print("Seeding initial data...")
                # Import and run the seed_data function from main.py
                from main import seed_data
                seed_data()
            else:
                print("Database already contains data. Skipping seeding.")
        except Exception as e:
            print(f"Database setup error: {e}")
    
    print("Starting Flask server on port 5002...")
    app.run(host='0.0.0.0', port=5002, debug=False)

