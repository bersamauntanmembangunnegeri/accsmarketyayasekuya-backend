from flask import Blueprint, jsonify, request
from src.models.settings import Page
from src.models.user import db
import re

pages_bp = Blueprint("pages", __name__)

def create_slug(title):
    """Create a URL-friendly slug from title"""
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

@pages_bp.route("/pages", methods=["GET"])
def get_all_pages():
    """Get all pages for admin management"""
    try:
        pages = Page.query.order_by(Page.created_at.desc()).all()
        return jsonify({
            "success": True,
            "data": [page.to_dict() for page in pages]
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@pages_bp.route("/pages", methods=["POST"])
def create_page():
    """Create a new page"""
    try:
        data = request.get_json()
        
        if not data or not data.get('title'):
            return jsonify({"success": False, "message": "Title is required"}), 400
        
        title = data.get('title')
        slug = data.get('slug') or create_slug(title)
        content = data.get('content', '')
        is_active = data.get('is_active', True)
        
        # Check if slug already exists
        existing_page = Page.query.filter_by(slug=slug).first()
        if existing_page:
            return jsonify({"success": False, "message": "Page with this slug already exists"}), 400
        
        new_page = Page(
            title=title,
            slug=slug,
            content=content,
            is_active=is_active
        )
        
        db.session.add(new_page)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Page created successfully",
            "data": new_page.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@pages_bp.route("/pages/<int:page_id>", methods=["GET"])
def get_page_by_id(page_id):
    """Get page by ID"""
    try:
        page = Page.query.get(page_id)
        if not page:
            return jsonify({"success": False, "message": "Page not found"}), 404
        
        return jsonify({
            "success": True,
            "data": page.to_dict()
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

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

@pages_bp.route("/pages/<int:page_id>", methods=["PUT"])
def update_page(page_id):
    """Update an existing page"""
    try:
        page = Page.query.get(page_id)
        if not page:
            return jsonify({"success": False, "message": "Page not found"}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400
        
        # Update fields if provided
        if 'title' in data:
            page.title = data['title']
        
        if 'slug' in data:
            # Check if new slug conflicts with existing pages (excluding current page)
            existing_page = Page.query.filter(Page.slug == data['slug'], Page.id != page_id).first()
            if existing_page:
                return jsonify({"success": False, "message": "Page with this slug already exists"}), 400
            page.slug = data['slug']
        
        if 'content' in data:
            page.content = data['content']
        
        if 'is_active' in data:
            page.is_active = data['is_active']
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Page updated successfully",
            "data": page.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@pages_bp.route("/pages/<int:page_id>", methods=["DELETE"])
def delete_page(page_id):
    """Delete a page"""
    try:
        page = Page.query.get(page_id)
        if not page:
            return jsonify({"success": False, "message": "Page not found"}), 404
        
        db.session.delete(page)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Page deleted successfully"
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@pages_bp.route("/pages/active", methods=["GET"])
def get_active_pages():
    """Get all active pages for frontend navigation"""
    try:
        pages = Page.query.filter_by(is_active=True).order_by(Page.title).all()
        return jsonify({
            "success": True,
            "data": [{"id": page.id, "title": page.title, "slug": page.slug} for page in pages]
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


