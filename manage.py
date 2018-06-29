#importing the db instance from app/__init__
from app.models import User
from app import create_app, db
from flask_script import Manager,Server

#Creating app instance
app = create_app('development')

manager =Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db , User=User)

if __name__ == '__main__':
    manager.run()