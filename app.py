from flask import Flask
from api.skills import skills_blueprint
from api.projects import projects_blueprint
from api.experience import experience_blueprint
from api.header import header_blueprint
from api.contacts import contacts_blueprint
from db.config import Config
from db.config import mongo
from flask_cors import CORS

app = Flask(__name__, static_folder='./dist', static_url_path='/')

CORS(app)

app.config.from_object(Config)

mongo.init_app(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

app.register_blueprint(header_blueprint)
app.register_blueprint(skills_blueprint)
app.register_blueprint(projects_blueprint)
app.register_blueprint(experience_blueprint)
app.register_blueprint(contacts_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
