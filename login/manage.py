def deploy():
    from app import create_app, db
    from models import User
    from flask_migrate import init,upgrade,migrate,stamp

    app = create_app()
    app.app_context().push()
    db.create_all()

    init()
    stamp()
    migrate()
    upgrade()
    
    

deploy()
