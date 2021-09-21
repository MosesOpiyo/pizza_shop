from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

from app.models import Pizza, Roles, User
from app import app,db

manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Roles = Roles,Pizza = Pizza)

if __name__ == '__main__':
    manager.run()