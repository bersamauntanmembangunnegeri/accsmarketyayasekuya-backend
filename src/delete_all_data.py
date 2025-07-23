import os
import sys
# DON\"T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from src.models.user import db
from src.models.category import Category
from src.models.product import Product
from src.models.vendor import Vendor, ProductVendor
from src.models.order import Order
from src.models.settings import SiteSetting, Page

# Configure Flask app for database access
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(os.path.dirname(__file__), r'database', r'app.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    print("Menghapus semua data dari database...")
    
    # Hapus data dari tabel ProductVendor terlebih dahulu karena ada foreign key ke Product dan Vendor
    ProductVendor.query.delete()
    print("Data ProductVendor dihapus.")

    # Hapus data dari tabel Order
    Order.query.delete()
    print("Data Order dihapus.")

    # Hapus data dari tabel Product
    Product.query.delete()
    print("Data Product dihapus.")

    # Hapus data dari tabel Category (termasuk subkategori)
    Category.query.delete()
    print("Data Category dan Subcategory dihapus.")

    # Hapus data dari tabel Vendor
    Vendor.query.delete()
    print("Data Vendor dihapus.")

    # Hapus data dari tabel SiteSetting
    SiteSetting.query.delete()
    print("Data SiteSetting dihapus.")

    # Hapus data dari tabel Page
    Page.query.delete()
    print("Data Page dihapus.")

    db.session.commit()
    print("Semua data berhasil dihapus dari database.")


