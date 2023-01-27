from app import create_app, db
from models import User
from flask_migrate import init,upgrade,migrate,stamp

def deploy():
    app = create_app()
    app.app_context().push()
    db.create_all()

    init()
    upgrade()
    migrate()
    stamp()

deploy()
