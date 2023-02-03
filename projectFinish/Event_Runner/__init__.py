from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from Event_Runner import routes
