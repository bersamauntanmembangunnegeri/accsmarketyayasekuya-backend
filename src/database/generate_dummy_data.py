#!/usr/bin/env python3
"""
Script untuk generate data dummy untuk database AccsMarket
"""

import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def connect_db():
    """Connect to SQLite database"""
    return sqlite3.connect('app.db')

def clear_tables(conn):
    """Clear all tables for fresh dummy data"""
    cursor = conn.cursor()
    
    # Disable foreign key constraints temporarily
    cursor.execute("PRAGMA foreign_keys = OFF")
    
    # Clear tables in correct order (respecting foreign keys)
    tables = ["orders", "product_vendors", "products", "vendors", "categories", "user", "footer_settings", "site_settings", "pages"]
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")
    # Re-enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON")
    conn.commit()

def generate_categories(conn):
    """Generate dummy categories"""
    cursor = conn.cursor()
    
    categories = [
        ('Facebook', 'facebook', 'Facebook accounts and pages', None),
        ('Instagram', 'instagram', 'Instagram accounts and followers', None),
        ('Twitter', 'twitter', 'Twitter accounts and followers', None),
        ('TikTok', 'tiktok', 'TikTok accounts and followers', None),
        ('YouTube', 'youtube', 'YouTube channels and subscribers', None),
        ('LinkedIn', 'linkedin', 'LinkedIn profiles and connections', None),
        ('Telegram', 'telegram', 'Telegram channels and groups', None),
        ('Discord', 'discord', 'Discord servers and members', None),
        ('Reddit', 'reddit', 'Reddit accounts and karma', None),
        ('Pinterest', 'pinterest', 'Pinterest accounts and boards', None),
    ]
    
    for name, slug, description, parent_id in categories:
        cursor.execute("""
            INSERT INTO categories (name, slug, description, parent_id, is_active, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, slug, description, parent_id, True, datetime.now()))
    
    conn.commit()
    print("✓ Generated categories")

def generate_vendors(conn):
    """Generate dummy vendors"""
    cursor = conn.cursor()
    
    vendor_names = [
        'SocialBoost Pro', 'DigitalGrowth', 'AccountMaster', 'SocialHub',
        'GrowthExperts', 'ViralBoost', 'SocialPower', 'AccountFactory',
        'BoostMeUp', 'SocialKing', 'DigitalBoost', 'AccountPro',
        'SocialGenie', 'GrowthMachine', 'ViralExperts'
    ]
    
    for name in vendor_names:
        rating = round(random.uniform(3.5, 5.0), 1)
        total_sales = random.randint(100, 5000)
        created_at = fake.date_time_between(start_date='-2y', end_date='now')
        
        cursor.execute("""
            INSERT INTO vendors (name, rating, total_sales, is_active, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (name, rating, total_sales, True, created_at))
    
    conn.commit()
    print("✓ Generated vendors")

def generate_products(conn):
    """Generate dummy products"""
    cursor = conn.cursor()
    
    # Get category IDs
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    
    product_templates = {
        'Facebook': [
            'Facebook Page with {} Likes',
            'Facebook Account - {} Friends',
            'Facebook Group with {} Members',
            'Facebook Business Page - {} Followers'
        ],
        'Instagram': [
            'Instagram Account - {} Followers',
            'Instagram Business Account - {} Followers',
            'Instagram Influencer Account - {} Followers',
            'Instagram Theme Page - {} Followers'
        ],
        'Twitter': [
            'Twitter Account - {} Followers',
            'Twitter Verified Account - {} Followers',
            'Twitter Business Account - {} Followers',
            'Twitter Influencer Account - {} Followers'
        ],
        'TikTok': [
            'TikTok Account - {} Followers',
            'TikTok Creator Account - {} Followers',
            'TikTok Viral Account - {} Followers',
            'TikTok Business Account - {} Followers'
        ],
        'YouTube': [
            'YouTube Channel - {} Subscribers',
            'YouTube Gaming Channel - {} Subscribers',
            'YouTube Educational Channel - {} Subscribers',
            'YouTube Music Channel - {} Subscribers'
        ],
        'LinkedIn': [
            'LinkedIn Profile - {} Connections',
            'LinkedIn Business Page - {} Followers',
            'LinkedIn Company Page - {} Followers',
            'LinkedIn Personal Brand - {} Connections'
        ],
        'Telegram': [
            'Telegram Channel - {} Members',
            'Telegram Group - {} Members',
            'Telegram Bot - {} Users',
            'Telegram News Channel - {} Subscribers'
        ],
        'Discord': [
            'Discord Server - {} Members',
            'Discord Gaming Server - {} Members',
            'Discord Community - {} Members',
            'Discord Bot - {} Servers'
        ],
        'Reddit': [
            'Reddit Account - {} Karma',
            'Reddit Account - {} Post Karma',
            'Reddit Account - {} Comment Karma',
            'Reddit Aged Account - {} Karma'
        ],
        'Pinterest': [
            'Pinterest Account - {} Followers',
            'Pinterest Business Account - {} Followers',
            'Pinterest Board - {} Followers',
            'Pinterest Niche Account - {} Followers'
        ]
    }
    
    follower_ranges = [
        (1000, 5000), (5000, 10000), (10000, 25000), (25000, 50000),
        (50000, 100000), (100000, 250000), (250000, 500000), (500000, 1000000)
    ]
    
    for category_id, category_name in categories:
        if category_name in product_templates:
            templates = product_templates[category_name]
            
            for template in templates:
                for _ in range(3):  # 3 products per template
                    followers = random.choice(follower_ranges)
                    follower_count = random.randint(followers[0], followers[1])
                    
                    name = template.format(f"{follower_count:,}")
                    description = f"High quality {category_name.lower()} account with real and active followers. Perfect for marketing and business growth."
                    
                    # Price based on follower count
                    base_price = round((follower_count / 1000) * random.uniform(0.5, 2.0), 2)
                    if base_price < 5:
                        base_price = round(random.uniform(5, 15), 2)
                    
                    stock_quantity = random.randint(1, 20)
                    rating = round(random.uniform(4.0, 5.0), 1)
                    return_rate = round(random.uniform(0.1, 2.0), 1)
                    delivery_time = random.choice(['1-24 hours', '24-48 hours', '2-3 days', 'Instant'])
                    created_at = fake.date_time_between(start_date='-1y', end_date='now')
                    
                    cursor.execute("""
                        INSERT INTO products (category_id, name, description, base_price, stock_quantity, 
                                            rating, return_rate, delivery_time, is_active, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (category_id, name, description, base_price, stock_quantity, 
                          rating, return_rate, delivery_time, True, created_at))
    
    conn.commit()
    print("✓ Generated products")

def generate_product_vendors(conn):
    """Generate product-vendor relationships"""
    cursor = conn.cursor()
    
    # Get all products and vendors
    cursor.execute("SELECT id FROM products")
    product_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM vendors")
    vendor_ids = [row[0] for row in cursor.fetchall()]
    
    for product_id in product_ids:
        # Each product has 1-3 vendors
        num_vendors = random.randint(1, 3)
        selected_vendors = random.sample(vendor_ids, min(num_vendors, len(vendor_ids)))
        
        # Get base price for this product
        cursor.execute("SELECT base_price FROM products WHERE id = ?", (product_id,))
        base_price = cursor.fetchone()[0]
        
        for vendor_id in selected_vendors:
            # Vendor price varies from base price
            price_variation = random.uniform(0.8, 1.2)
            vendor_price = round(base_price * price_variation, 2)
            stock = random.randint(1, 10)
            created_at = fake.date_time_between(start_date='-6m', end_date='now')
            
            cursor.execute("""
                INSERT INTO product_vendors (product_id, vendor_id, price, stock, is_active, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (product_id, vendor_id, vendor_price, stock, True, created_at))
    
    conn.commit()
    print("✓ Generated product-vendor relationships")

def generate_users(conn):
    """Generate dummy users"""
    cursor = conn.cursor()
    
    for _ in range(50):
        username = fake.user_name()
        email = fake.email()
        
        cursor.execute("""
            INSERT INTO user (username, email)
            VALUES (?, ?)
        """, (username, email))
    
    conn.commit()
    print("✓ Generated users")

def generate_orders(conn):
    """Generate dummy orders"""
    cursor = conn.cursor()
    
    # Get product-vendor combinations
    cursor.execute("""
        SELECT pv.product_id, pv.vendor_id, pv.price, p.name
        FROM product_vendors pv
        JOIN products p ON pv.product_id = p.id
    """)
    product_vendors = cursor.fetchall()
    
    payment_methods = ['Bitcoin', 'USDT', 'Ethereum', 'PayPal', 'Credit Card']
    statuses = ['pending', 'processing', 'completed', 'cancelled']
    
    for _ in range(100):
        product_id, vendor_id, unit_price, product_name = random.choice(product_vendors)
        
        customer_email = fake.email()
        quantity = random.randint(1, 5)
        total_price = round(unit_price * quantity, 2)
        payment_method = random.choice(payment_methods)
        coupon_code = fake.word().upper() if random.random() < 0.3 else None
        subscribe_newsletter = random.choice([True, False])
        status = random.choice(statuses)
        created_at = fake.date_time_between(start_date='-3m', end_date='now')
        
        cursor.execute("""
            INSERT INTO orders (product_id, vendor_id, customer_email, quantity, unit_price, 
                              total_price, payment_method, coupon_code, subscribe_newsletter, 
                              status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (product_id, vendor_id, customer_email, quantity, unit_price, total_price,
              payment_method, coupon_code, subscribe_newsletter, status, created_at))
    
    conn.commit()
    print("✓ Generated orders")

def generate_footer_settings(conn):
    """Generate dummy footer settings"""
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO footer_settings (
            company_name, company_description, logo_text, logo_suffix,
            social_link_1, social_link_1_icon, social_link_2, social_link_2_icon,
            social_link_3, social_link_3_icon, quick_links, support_links,
            contact_email, contact_website, support_text, security_text,
            copyright_text, payment_methods, background_color, text_color,
            created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        'ACCS market.com',
        'Buy or Sell Social Media Accounts (PVA & Cheap). Your trusted marketplace for social media accounts.',
        'ACCS',
        'market.com',
        'https://accsmarket.news',
        'Globe',
        'mailto:support@accsmarket.com',
        'Mail',
        'https://t.me/accsmarket',
        'MessageCircle',
        '[{"label": "Home", "url": "/"}, {"label": "Categories", "url": "/categories"}, {"label": "Search Accounts", "url": "/search"}, {"label": "Become a Seller", "url": "/seller"}]',
        '[{"label": "FAQ", "url": "/faq"}, {"label": "Terms of Use", "url": "/terms"}, {"label": "Privacy Policy", "url": "/privacy"}, {"label": "Contact Support", "url": "/support"}]',
        'support@accsmarket.com',
        'accsmarket.news',
        '24/7 Support Available',
        'Secure Transactions',
        '© 2024 AccsMarket. All rights reserved.',
        '[{"name": "Bitcoin", "code": "BTC"}, {"name": "USDT", "code": "USDT"}, {"name": "Ethereum", "code": "ETH"}, {"name": "PayPal", "code": "PAYPAL"}]',
        '#1a1a1a',
        '#ffffff',
        datetime.now(),
        datetime.now()
    ))
    
    conn.commit()
    print("✓ Generated footer settings")

def generate_site_settings(conn):
    """Generate dummy site settings"""
    cursor = conn.cursor()
    
    settings = [
        ('site_name', 'AccsMarket', 'Website name'),
        ('site_description', 'Buy or Sell Social Media Accounts', 'Website description'),
        ('header_logo_url', '/logo.png', 'Header logo URL'),
        ('header_logo_alt', 'AccsMarket', 'Header logo alt text'),
        ('search_enabled', 'true', 'Enable search functionality'),
        ('search_placeholder', 'Search for accounts', 'Search input placeholder'),
        ('navigation_menu', '[{"label": "Home", "url": "/", "active": true}, {"label": "Categories", "url": "/categories", "active": true}, {"label": "Search", "url": "/search", "active": true}, {"label": "Become a Seller", "url": "/seller", "active": true}]', 'Navigation menu items'),
    ]
    
    for key, value, description in settings:
        cursor.execute("""
            INSERT INTO site_settings (key, value, description, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
        """, (key, value, description, datetime.now(), datetime.now()))
    
    conn.commit()
    print("✓ Generated site settings")

def generate_pages(conn):
    """Generate dummy pages"""
    cursor = conn.cursor()
    
    pages = [
        ('FAQ', 'faq', 'Frequently Asked Questions content here...'),
        ('Terms of Use', 'terms', 'Terms of Use content here...'),
        ('Privacy Policy', 'privacy', 'Privacy Policy content here...'),
        ('Contact Support', 'support', 'Contact Support information here...'),
        ('About Us', 'about', 'About Us content here...'),
    ]
    
    for title, slug, content in pages:
        cursor.execute("""
            INSERT INTO pages (title, slug, content, is_active, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, slug, content, True, datetime.now(), datetime.now()))
    
    conn.commit()
    print("✓ Generated pages")

def main():
    """Main function to generate all dummy data"""
    print("🚀 Starting dummy data generation...")
    
    # Install faker if not available
    try:
        from faker import Faker
    except ImportError:
        print("Installing faker...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'faker'])
        from faker import Faker
    
    conn = connect_db()
    
    try:
        print("🗑️  Clearing existing data...")
        clear_tables(conn)
        
        print("📊 Generating dummy data...")
        generate_categories(conn)
        generate_vendors(conn)
        generate_products(conn)
        generate_product_vendors(conn)
        generate_users(conn)
        generate_orders(conn)
        generate_footer_settings(conn)
        generate_site_settings(conn)
        generate_pages(conn)
        
        print("✅ Dummy data generation completed successfully!")
        print("\n📈 Summary:")
        
        # Show counts
        cursor = conn.cursor()
        tables = ['categories', 'vendors', 'products', 'product_vendors', 'user', 'orders', 'footer_settings', 'site_settings', 'pages']
        
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"   {table}: {count} records")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()

