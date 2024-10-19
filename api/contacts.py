from flask import Blueprint, jsonify, request
from db.config import mongo

contacts_blueprint = Blueprint("contacts", __name__)

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@contacts_blueprint.route("/api/contacts", methods=["GET"])
def get_contacts():
    try:
        contacts = mongo.db.contacts.find()
        return jsonify([serialize_doc(contact) for contact in contacts])
    except :
        return jsonify({"error fetching contacts"}), 500