import hug
import jwt
import db

def token_verify(token):
    secret_key = 'This_should_be_changed'
    try:
        return jwt.decode(token, secret_key, algorithm='HS256')
    except jwt.DecodeError:
        return Falses

token_key_authentication = hug.authentication.token(token_verify)

@hug.get('/token_authenticated', requires=token_key_authentication)  # noqa
def token_auth_call(user: hug.directives.user):
    return 'You are user: {0} with data {1}'.format(user['user'], user['expire'])

@hug.get('/token_generation')  # noqa
def token_gen_call(username, password):
    secret_key = 'This_should_be_changed'
    if db.checkUser(username,password):
        return {"authorized": "True", "token" : jwt.encode({'user': username, 'expire': 'never'}, secret_key, algorithm='HS256')}
    return {"authorized": "False"}

@hug.get('/listTables', requires=token_key_authentication)
def listTables():
    res = db.listTables()
    return(res)
