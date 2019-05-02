from flask_restplus import reqparse

registerParser = reqparse.RequestParser()
registerParser.add_argument('fullName', type=str, help='user fullname',required= True)
registerParser.add_argument('email', type=str, help='Email of the user',required= True)
registerParser.add_argument('password', type=str, help='Password of the user',required= True)

loginParser = reqparse.RequestParser()
loginParser.add_argument('email', type=str, help='Email of the user',required= True)
loginParser.add_argument('password', type=str, help='Password of the user',required= True)

incomeParser = reqparse.RequestParser()
incomeParser.add_argument('name', type=str, help='Name of Income',required= True)
incomeParser.add_argument('amount', type=float, help='Amount of Income',required=True)
incomeParser.add_argument('barcodeId', type=int, help='Barcode Id',required= False)
incomeParser.add_argument('categoryId', type=int, help='Category Id',required= True)

incomeUpdateParser = reqparse.RequestParser()
incomeUpdateParser.add_argument('name', type=str, help='New name',required= False)
incomeUpdateParser.add_argument('amount', type=float, help='New Amount',required= False)
incomeUpdateParser.add_argument('barcodeId', type=int, help='Change Barcode Id',required= False)
incomeUpdateParser.add_argument('categoryId', type=int, help='Change Category Id',required= False)


catUpdateParser = reqparse.RequestParser()
catUpdateParser.add_argument('name', type=str, help='New name',required= False)
catUpdateParser.add_argument('budget', type=float, help='New Category Budget',required= False)


catParser = reqparse.RequestParser()
catParser.add_argument('name', type=str, help='Name of Category',required= True)
catParser.add_argument('budget', type=float, help='Category Budget',required= False)


barUpdateParser = reqparse.RequestParser()
barUpdateParser.add_argument('code', type=str, help='New Bar Code',required= False)
barUpdateParser.add_argument('productName', type=str, help='New Product Name',required= False)
barUpdateParser.add_argument('amount', type=float, help='New Amount attached to Barcode',required= False)


barParser = reqparse.RequestParser()
barParser.add_argument('code', type=str, help=' Bar Code',required= True)
barParser.add_argument('productName', type=str, help='Product Name',required= True)
barParser.add_argument('amount', type=float, help=' Amount attached to Barcode',required= True)


