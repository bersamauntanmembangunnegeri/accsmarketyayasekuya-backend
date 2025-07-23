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

def display_results():
    with app.app_context():
        print("=" * 80)
        print("HASIL EKSTRAKSI KATEGORI DAN SUBKATEGORI DARI ACCSMARKET.COM")
        print("=" * 80)
        
        # Get all main categories
        main_categories = Category.query.filter(Category.parent_id == None).all()
        
        print(f"\\nJUMLAH TOTAL:")
        print(f"- Kategori Utama: {len(main_categories)}")
        
        total_subcategories = 0
        
        print(f"\\nDETAIL KATEGORI DAN SUBKATEGORI:")
        print("-" * 80)
        
        for i, category in enumerate(main_categories, 1):
            subcategories = Category.query.filter(Category.parent_id == category.id).all()
            total_subcategories += len(subcategories)
            
            print(f"\\n{i}. {category.name}")
            print(f"   Slug: {category.slug}")
            print(f"   Deskripsi: {category.description}")
            print(f"   Jumlah Subkategori: {len(subcategories)}")
            
            if subcategories:
                print(f"   Subkategori:")
                for j, subcat in enumerate(subcategories, 1):
                    print(f"      {i}.{j}. {subcat.name}")
                    print(f"           Slug: {subcat.slug}")
                    print(f"           Deskripsi: {subcat.description}")
        
        print(f"\\n" + "=" * 80)
        print(f"RINGKASAN AKHIR:")
        print(f"- Total Kategori Utama: {len(main_categories)}")
        print(f"- Total Subkategori: {total_subcategories}")
        print(f"- Total Produk: {Product.query.count()}")
        print("=" * 80)

if __name__ == "__main__":
    display_results()

