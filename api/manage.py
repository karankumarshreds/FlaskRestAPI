"""
Migrations is a way of updating our db with the changes we made to our 
models. 
Since we had already set up our models, now we need to migrate our models 
changes to the db.
"""

import os 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 

from src.app import create_app
from src.models import db 

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
  
"""
What we did?
We set up a migration script that will help in the maintenance of our migrations.
The Manager class keeps track of all the commands and handles how they are called 
from the command line. The MigrateCommand contains a set of migration commands 
such as init, migrate, upgrade etc.

$ python manage.py db init

This will create a new migration sub-folder in the project directory

Now, run this script which will populate our migrations files and generate users 
and blogposts tables with our model changes


$ python manage.py db migrate

"""

