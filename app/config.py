
def codeChecker(code):
    if code == 400:
        return {'message':'your request body cannot be processed'},400
    elif code == 401:
        return {'message':'the user does not have the necessary credentials'},401
    elif code == 404:
        return {'message':'resource not found'},404
    elif code == 409:
        return {'message':'Resource already exists'},409
    elif code == 403:
        return {'message':'Wrong credentials'},403
    else:
        return {'message': 'We encountered an error at the server'}, 500
