from flask import request
from flask_restful import Resource
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
import requests
from config import codeChecker

USER_SERVICE = 'http://127.0.0.1:5050/'
INCOME_SERVICE = 'http://127.0.0.1:5051/'
EXPENSE_SERVICE = 'http://127.0.0.1:5052/'


# auth service
class UserRegistration(Resource):
    def post(self):
        # print(request.get_json())
        res = requests.post(USER_SERVICE + 'register', json=request.get_json())
        # print(res.status_code)
        # print(res.json())
        if res.status_code == 201 or res.status_code == 200:
            email = res.json()['message']
            access_token = create_access_token(identity=email)
            return {'message': 'User {} was created'.format(email),
                    'access_token': access_token
                    }, 201
        return codeChecker(res.status_code)
class UserLogin(Resource):
    def post(self):
        res = requests.post(USER_SERVICE + 'login', json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            email = res.json()['message']
            access_token = create_access_token(identity=email)
            return {'message': '{} logged in success'.format(email),
                    'access_token': access_token
                    }, 200
        return codeChecker(res.status_code)
class UserLogout(Resource):
    def post(self):
        res = requests.post(USER_SERVICE + 'logout', json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
class AllUsers(Resource):
    def get(self):
        res = requests.get(USER_SERVICE + 'users')
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

# income service
class Income(Resource):
    def get(self,id):
        res = requests.get(INCOME_SERVICE + 'income/'+id)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    def put(self,id):
        res = requests.get(INCOME_SERVICE + 'income/'+id, json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    def delete(self,id):
        res = requests.get(INCOME_SERVICE + 'income/'+id, json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
class Incomes(Resource):
    def post(self):
        res = requests.post(INCOME_SERVICE + 'income',json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    def get(self):
        res = requests.get(INCOME_SERVICE + 'income')
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    def delete(self):
        res = requests.get(INCOME_SERVICE + 'income')
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
class Barcode(Resource):
    def get(self,id):
        res = requests.get(INCOME_SERVICE + 'barcode/'+id)
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    def put(self,id):
        res = requests.get(INCOME_SERVICE + 'barcode/'+id, json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    def delete(self,id):
        res = requests.get(INCOME_SERVICE + 'barcode/'+id, json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
class Barcodes(Resource):
    def post(self):
        res = requests.post(INCOME_SERVICE + 'barcode',json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    def get(self):
        res = requests.get(INCOME_SERVICE + 'barcode')
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    def delete(self):
        res = requests.get(INCOME_SERVICE + 'barcode')
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
class Category(Resource):
    def get(self,name):
        res = requests.get(INCOME_SERVICE + 'category/'+name)
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    def put(self,name):
        res = requests.get(INCOME_SERVICE + 'category/'+name, json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
    def delete(self,name):
        res = requests.get(INCOME_SERVICE + 'category/'+name, json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)
class Categories(Resource):
    def post(self):
        res = requests.post(INCOME_SERVICE + 'category',json=request.get_json())
        if res.status_code == 201 or res.status_code == 200:
            return res.json()
        else:
            return codeChecker(res.status_code)

    def get(self):
        res = requests.get(INCOME_SERVICE + 'category')
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)

    def delete(self):
        res = requests.get(INCOME_SERVICE + 'category')
        if res.status_code == 201 or res.status_code == 200:
            # print(res.json())
            return res.json()
        else:
            return codeChecker(res.status_code)




