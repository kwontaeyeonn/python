from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# 메모장 역할을 할 간단한 데이터 저장소 (메모리)
posts = []
post_id_counter = 1

# 게시글 목록 조회 (GET /posts)
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# 게시글 생성 (POST /posts)
@app.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "title and content required"}), 400
    
    post = {
        "id": post_id_counter,
        "title": data['title'],
        "content": data['content']
    }
    posts.append(post)
    post_id_counter += 1
    return jsonify(post), 201

# 특정 게시글 조회 (GET /posts/<id>)
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    return jsonify(post)

# 게시글 수정 (PUT /posts/<id>)
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data"}), 400

    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    
    post['title'] = data.get('title', post['title'])
    post['content'] = data.get('content', post['content'])
    return jsonify(post)

# 게시글 삭제 (DELETE /posts/<id>)
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    posts = [p for p in posts if p['id'] != post_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
