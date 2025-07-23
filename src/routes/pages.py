from flask import Blueprint, jsonify
from src.models.settings import Page

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/pages/<slug>", methods=["GET"])
def get_page_by_slug(slug):
    """Get page content by slug"""
    try:
        page = Page.query.filter_by(slug=slug, is_active=True).first()
        if not page:
            return jsonify({"success": False, "message": "Page not found"}), 404
        
        return jsonify({
            "success": True,
            "data": page.to_dict()
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


