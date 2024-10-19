from flask import Blueprint, jsonify, request
from db.config import mongo

experience_blueprint = Blueprint('experience', __name__)


def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@experience_blueprint.route('/api/experience', methods=['GET'])
def get_experience():
    try:
        experience = mongo.db.experiences.find()
        return jsonify([serialize_doc(exp) for exp in experience])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@experience_blueprint.route('/api/experience/<experience_id>', methods=['GET'])
def get_experience_by_id(experience_id):
    try:
        experience = mongo.db.experience.find_one({"_id": experience_id})
        return jsonify(serialize_doc(experience)) if experience else jsonify({"error": "Experience not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@experience_blueprint.route('/api/experience', methods=['POST'])
def add_experience():
    try:
        new_experience = request.json
        mongo.db.experience.insert_one(new_experience)
        return jsonify({"message": "Experience added!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
