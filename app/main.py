from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
import resources
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)


app = Flask(__name__)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

api = Api(app)

# user endpoints
api.add_resource(resources.UserRegistration,'/user/register')
api.add_resource(resources.UserLogin,'/user/login')
api.add_resource(resources.UserLogout,'/user/logout')
api.add_resource(resources.AllUsers,'/user/logout')

# income endpoints
api.add_resource(resources.Income,'/income/income<int:id>')
api.add_resource(resources.Incomes,'/income/income')
api.add_resource(resources.Barcode,'/income/barcode/<int:id>')
api.add_resource(resources.Barcodes,'/income/barcode')
api.add_resource(resources.Category,'/income/category/<string:name>')
api.add_resource(resources.Categories,'/income/category')
