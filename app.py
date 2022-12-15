import os   #added

from flask import Flask
from flask import Flask
from flask_smorest import Api

from db import db    
import models #instead of import models.__init__    #added


from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

#added
#We put all instructions inside a function
def create_app(db_url=None):
    #when calling this function, we can pass in a database URL that we want to connect to.
    app = Flask(__name__, instance_path=os.getcwd())
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
            "OPENAPI_SWAGGER_UI_URL"
        ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    #We often use environment variables when we deploy our Flask apps, because
    #it's an easy way to store arbitrary secrets or information in our server
    #without having to store it in our code.
    #You don't wanna store secrets like database connection strings in your code,
    #because if you ever wanna open source your code or share it with other people, then
    #they will have access to your database.
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

#And what this does, is it initializes the Flask SQLAlchemy extension,
#giving it our Flask app so that it can connect the Flask app to SQLAlchemy
    
    
    api = Api(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    


    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app