from flask import Blueprint, jsonify, request
import datetime

bp = Blueprint('blog', __name__)

posts = [
    {"id": 1, 
     "title": "First Article", 
     "content": "This is the first article.", 
     "author": "John Doe", "created_at": "2024-06-01T12:00:00",
     "updated_at": "2024-06-01T12:00:00"},
    {"id": 2, 
     "title": "Second Article", 
     "content": "This is the second article.", 
     "author": "Jane Smith", "created_at": "2024-06-02T12:00:00",
     "updated_at": "2024-06-02T12:00:00"},
    {"id": 3, 
     "title": "Third Article", 
     "content": "This is the third article.", 
     "author": "Alice Johnson", "created_at": "2024-06-03T12:00:00",
     "updated_at": "2024-06-03T12:00:00"}
]
next_post_id = 4
# Blog Simple (CRUD Complet)
@bp.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = next((p for p in posts if p['id'] == id), None)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post)

@bp.route('/posts', methods=['POST'])
def create_post():
    global next_post_id
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data or 'author' not in data:
        return jsonify({"error": "Missing required fields: title, content, author"}), 400

    new_post = {
        "id": next_post_id,
        "title": data['title'],
        "content": data['content'],
        "author": data['author'],
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat()
    }
    posts.append(new_post)
    next_post_id += 1
    return jsonify(new_post), 201

@bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = next((p for p in posts if p['id'] == id), None)
    if post is None:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    post['title'] = data.get('title', post['title'])
    post['content'] = data.get('content', post['content'])
    post['author'] = data.get('author', post['author'])
    post['updated_at'] = datetime.datetime.now().isoformat()
    
    return jsonify(post)
@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    global posts
    post = next((p for p in posts if p['id'] == id), None)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    
    posts = [p for p in posts if p['id'] != id]
    return jsonify({"message": "Post deleted successfully"}), 200