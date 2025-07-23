from src.models.user import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 3), nullable=False)
    total_price = db.Column(db.Numeric(10, 3), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    coupon_code = db.Column(db.String(50))
    subscribe_newsletter = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='pending')  # pending, completed, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    product = db.relationship('Product', backref='orders')
    vendor = db.relationship('Vendor', backref='orders')
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'vendor_id': self.vendor_id,
            'email': self.customer_email,  # Frontend expects 'email'
            'customer_email': self.customer_email,
            'quantity': self.quantity,
            'unit_price': float(self.unit_price) if self.unit_price else 0,
            'total_price': float(self.total_price) if self.total_price else 0,
            'payment_method': self.payment_method,
            'coupon_code': self.coupon_code,
            'subscribe_newsletter': self.subscribe_newsletter,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'product': self.product.to_dict() if self.product else None,
            'vendor': self.vendor.to_dict() if self.vendor else None,
            'product_name': self.product.name if self.product else None,
            'vendor_name': self.vendor.name if self.vendor else f"Partner #{self.vendor_id}"
        }

