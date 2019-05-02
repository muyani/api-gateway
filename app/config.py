
def codeChecker(code):
    if code == 400:
        return {'message':'Bad request ,check your body'},400
    elif code == 401:
        return {'message':'Invalid credentials'},401
    elif code == 404:
        return {'message':'Not found'},404
    elif code == 409:
        return {'message':'Conflict:Already exists or There is constraint'},409
    elif code == 403:
        return {'message':'Wrong credentials'},403
    else:
        return {'message': 'Internal server error'},500
