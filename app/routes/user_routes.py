from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models.user_model import UserModel

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = UserModel.get_all_users()
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users), 200

@user_bp.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserModel.get_user(user_id)
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if not all(k in data for k in ('name', 'email', 'password')):
        return jsonify({'error': 'Missing fields'}), 400
    result = UserModel.create_user(data)
    return jsonify({'message': 'User created', 'id': str(result.inserted_id)}), 201

@user_bp.route('/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    result = UserModel.update_user(user_id, data)
    if result.matched_count:
        return jsonify({'message': 'User updated'}), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = UserModel.delete_user(user_id)
    if result.deleted_count:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404
