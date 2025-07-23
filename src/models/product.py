from src.models.user import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    base_price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    return_rate = db.Column(db.Float, default=0.0)
    delivery_time = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    category = db.relationship('Category', backref='products')
    
    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description,
            'base_price': self.base_price,
            'stock_quantity': self.stock_quantity,
            'rating': self.rating,
            'return_rate': self.return_rate,
            'delivery_time': self.delivery_time,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'category': self.category.to_dict() if self.category else None
        }
