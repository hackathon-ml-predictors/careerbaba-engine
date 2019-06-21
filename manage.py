from flask_script import Manager
from app import create_app


manager = Manager(create_app)

@manager.command
def run_debug():

    app = create_app()

    app.run(debug=True,host='127.0.0.1')

if __name__ == "__main__":
    manager.run()
