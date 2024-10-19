from flask import Blueprint, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId
from db.config import mongo

projects_blueprint = Blueprint('projects', __name__)


def serialize_doc(doc):
    doc["_id"] = str(doc["_id"]) 
    return doc

@projects_blueprint.route('/api/projects', methods=['GET'])
def get_projects():
    try:
        projects = mongo.db.projects.find()
        return jsonify([serialize_doc(project) for project in projects])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@projects_blueprint.route('/api/projects/<project_id>', methods=['GET'])
def get_project_by_id(project_id):
    try:
        project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
        return jsonify(serialize_doc(project)) if project else jsonify({"error": "Project not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@projects_blueprint.route('/api/projects', methods=['POST'])
def add_project():
    try:
        new_project = request.json
        mongo.db.projects.insert_one(new_project)
        return jsonify({"message": "Project added!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
