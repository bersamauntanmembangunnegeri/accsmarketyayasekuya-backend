import os
import sys
# DON\"T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from src.models.user import db
from src.models.category import Category
from src.models.product import Product

# Configure Flask app for database access
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(os.path.dirname(__file__), r'database', r'app.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    print("Verifikasi data setelah penghapusan...")
    
    total_categories = Category.query.filter(Category.parent_id == None).count()
    total_subcategories = Category.query.filter(Category.parent_id != None).count()
    total_products = Product.query.count()

    print(f"Jumlah Kategori Utama: {total_categories}")
    print(f"Jumlah Subkategori: {total_subcategories}")
    print(f"Jumlah Produk: {total_products}")

    if total_categories == 0 and total_subcategories == 0 and total_products == 0:
        print("Verifikasi berhasil: Semua data kategori, subkategori, dan produk telah dihapus.")
    else:
        print("Verifikasi gagal: Masih ada data yang tersisa.")


