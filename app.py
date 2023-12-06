from flask import Flask
from flask_migrate import Migrate
from db.database import db
from config import ApplicationConfig
from flask_session import Session
from main.events_routes import dept_event
from main.user_events_routes import ue
from main.users_routes import user
from main.events_user_routes import eu
from main.attendece_route import attendence
from main.image_route import image
from main.club_routes import club
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(ApplicationConfig)


# blueprints for different routes
app.register_blueprint(dept_event)
app.register_blueprint(user)
app.register_blueprint(ue)
app.register_blueprint(attendence)
app.register_blueprint(eu)
app.register_blueprint(image)
app.register_blueprint(club)


server_session = Session(app)
db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000)
