from src.models.user import db
from datetime import datetime

class Vendor(db.Model):
    __tablename__ = 'vendors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Numeric(3, 1), default=0.0)
    total_sales = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': float(self.rating) if self.rating else 0,
            'total_sales': self.total_sales,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class ProductVendor(db.Model):
    __tablename__ = 'product_vendors'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    price = db.Column(db.Numeric(10, 3), nullable=False)
    stock = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    product = db.relationship('Product', backref='vendors')
    vendor = db.relationship('Vendor', backref='products')
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'vendor_id': self.vendor_id,
            'price': float(self.price) if self.price else 0,
            'stock': self.stock,
            'is_active': self.is_active,
            'vendor': self.vendor.to_dict() if self.vendor else None
        }

