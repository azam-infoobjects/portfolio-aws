from flask import Blueprint, jsonify
from flask_pymongo import PyMongo
from db.config import mongo


header_blueprint = Blueprint('header', __name__)

@header_blueprint.route('/api/header', methods=['GET'])
def get_header():
    try:
        header = mongo.db.header.find_one()
        return jsonify(header) if header else jsonify({"error": "Header not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
