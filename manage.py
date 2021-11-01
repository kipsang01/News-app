from app import create_app
from flask_script import Manager,Server
from .config import Config

SECRET_KEY =Config.SECRET_KEY
app = create_app('development')
app.config['SECRET_KEY'] = SECRET_KEY

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()