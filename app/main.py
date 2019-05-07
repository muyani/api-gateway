from flask import Flask,make_response,jsonify,request
import requests
from flask_restplus import Api,Resource
from flask_jwt_extended import JWTManager
from config import codeChecker
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
import urls


app = Flask(__name__)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
app.config['JWT_SECRET_KEY'] = ''
jwt = JWTManager(app)

api = Api(app)
ns = api.namespace('api/v1',description='Bizweb Api Gateway.')

import parsers
import fields

@app.errorhandler(400)
def badRequest(e):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def notFound(e):
    return make_response(jsonify({'error': 'Resource not found'}), 404)

@app.errorhandler(405)
def notAllowed(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 405)

@app.errorhandler(500)
def internalServer(e):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@ns.route('/users/register')
@ns.expect(parsers.registerParser)
class UserRegistration(Resource):
    def post(self):
        body = parsers.registerParser.parse_args()
        res = requests.post(urls.USER_SERVICE + u'/register', json = body)
        # print(res.json())
        if res.status_code == 201 or res.status_code == 200:
            id = res.json()['id']
            fullname = res.json()['fullname']
            access_token = create_access_token(identity=id)
            return {'message': 'User {} was created'.format(fullname),
                    'access_token': access_token
                    }, 201
        return codeChecker(res.status_code)

@ns.route('/users/login')
@ns.expect(parsers.loginParser)
class UserLogin(Resource):
    def post(self):
        body = parsers.loginParser.parse_args()
        print(body)
        res = requests.post(urls.USER_SERVICE + '/login', json=body)
        if res.status_code == 201 or res.status_code == 200:
            id = res.json()['id']
            fullname = res.json()['fullName']
            access_token = create_access_token(identity=id)
            return {'message': '{} logged in success'.format(fullname),
                    'access_token': access_token
                    }, 200
        return codeChecker(res.status_code)


# income routes
@ns.route('/incomes/<int:id>')
class Income(Resource):
    @jwt_required
    def get(self,id):
        uid = get_jwt_identity()
        location = u'{}/incomes/{}/{}'.format(urls.INCOME_SERVICE, uid, id)
        res = requests.get(location)
        if res.status_code == 201 or res.status_code == 200:
         # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    @ns.expect(parsers.incomeUpdateParser)
    def put(self,id):
        body = parsers.incomeUpdateParser.parse_args()
        uid = get_jwt_identity()
        location = u'{}/incomes/{}/{}'.format(urls.INCOME_SERVICE, uid, id)
        res = requests.put(location, json=body)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    def delete(self,id):
        uid = get_jwt_identity()
        location = u'{}/incomes/{}/{}'.format(urls.INCOME_SERVICE, uid, id)
        res = requests.delete(location)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

@ns.route('/incomes')
class Incomes(Resource):
    @jwt_required
    @ns.expect(parsers.incomeParser)
    def post(self):
        uid = get_jwt_identity()
        location = u'{}/incomes/{}'.format(urls.INCOME_SERVICE,uid)
        body = parsers.incomeParser.parse_args()
        res = requests.post(location,json=body)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    def get(self):
        uid = get_jwt_identity()
        location = u'{}/incomes/{}'.format(urls.INCOME_SERVICE, uid)
        res = requests.get(location)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)



@ns.route('/incomes/barcodes/<int:id>')
class Barcode(Resource):
    @jwt_required
    def get(self,id):
        location = u'{}/barcodes/{}'.format(urls.INCOME_SERVICE, id)
        res = requests.get(location)
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    @ns.expect(parsers.barUpdateParser)
    def put(self,id):
        location = u'{}/barcodes/{}'.format(urls.INCOME_SERVICE, id)
        body = parsers.barUpdateParser.parse_args()
        res = requests.put(location, json=body)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    def delete(self,id):
        location = u'{}/barcodes/{}'.format(urls.INCOME_SERVICE, id)
        res = requests.delete(location)
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

@ns.route('/incomes/barcodes')
class Barcodes(Resource):
    @jwt_required
    @ns.expect(parsers.barParser)
    def post(self):
        location = u'{}/barcodes'.format(urls.INCOME_SERVICE)
        body = parsers.barParser.parse_args()
        res = requests.post(location,json=body)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    def get(self):
        location = u'{}/barcodes'.format(urls.INCOME_SERVICE)
        res = requests.get(location)
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)


@ns.route('/incomes/categories/<string:name>')
class Category(Resource):
    @jwt_required
    def get(self,name):
        location = u'{}/categories/{}'.format(urls.INCOME_SERVICE,name)

        res = requests.get(location)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    def put(self,name):
        location = u'{}/categories/{}'.format(urls.INCOME_SERVICE,name)
        body = parsers.catUpdateParser.parse_args()
        res = requests.put(location, json=body)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    @jwt_required
    def delete(self,name):
        location = u'{}/categories/{}'.format(urls.INCOME_SERVICE, name)
        res = requests.delete(location)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

@ns.route('/incomes/categories')
class Categories(Resource):
    @jwt_required
    @ns.expect(parsers.catParser)
    def post(self):
        location = u'{}/categories'.format(urls.INCOME_SERVICE)
        body = parsers.catParser.parse_args()
        res = requests.post(location,json=body)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    def get(self):
        location = u'{}/categories'.format(urls.INCOME_SERVICE)
        res = requests.get(location)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)





