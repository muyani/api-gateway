from flask_restplus import fields
from main import api
# income service
incomeStructure = api.model('Income', {
    'id': fields.Integer,
    'name': fields.String,
    'amount': fields.String,
    'date': fields.DateTime,
    'usernumber': fields.String,
    'barcodeId': fields.Integer,
    'categoryId': fields.Integer
})

categoryStructure = api.model('Category', {
    'id': fields.Integer,
    'name': fields.String,
    'budget': fields.Float
})

barcodeStructure = api.model('Barcode', {
    'id': fields.Integer,
    'code': fields.String,
    'productName': fields.String,
    'amount': fields.Float
})

# users service
userStructure = api.model('user',{
    'id':fields.String,
    'fullName':fields.String,
    'email':fields.String
})


