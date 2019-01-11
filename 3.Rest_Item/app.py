import os

from flask import Flask
from flask_restful import Api

from resources.item import Item, ItemList

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
api = Api(app)

api.add_resource(Item, '/item/<string:name>')






if __name__ == '__main__':
    from db import db

    db.init_app(app)
    
    port = int(os.environ.get('PORT', 5000))
    
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(host='0.0.0.0', port=port, debug=True)
