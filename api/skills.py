from flask import Blueprint, jsonify, request
from bson import ObjectId
from db.config import mongo

skills_blueprint = Blueprint('skills', __name__)

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"]) 
    return doc

@skills_blueprint.route('/api/skills', methods=['GET'])
def get_skills():
    try:
        skills = mongo.db.skills.find()
        skills = list(skills)
        return jsonify([serialize_doc(skill) for skill in skills])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@skills_blueprint.route('/api/skills/<skill_id>', methods=['GET'])
def get_skill_by_id(skill_id):
    try:
        skill = mongo.db.skills.find_one({"_id": ObjectId(skill_id)})
        return jsonify(serialize_doc(skill)) if skill else jsonify({"error": "Skill not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@skills_blueprint.route('/api/skills', methods=['POST'])
def add_skill():
    try:
        new_skill = request.json
        mongo.db.skills.insert_one(new_skill)
        return jsonify({"message": "Skill added!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
