import requests
import hashlib
import hmac
import json
import base64

class WeeblyClient(object):

    WEEBLY_API_KEY = 'YOUR_API_KEY'
    WEEBLY_API_SECRET = 'YOUR_API_SECRET'
    WEEBLY_TEST_ACCOUNT_ID = 'YOUR_TEST_ACCOUNT'

    base_url = 'https://api.weeblycloud.com/'

    def __init__(self, key, secret, account_id):
        self.WEEBLY_API_KEY = key
        # the same for other parameters

    def weebly_hash(self, my_content):
        my_hmac = hmac.new(self.WEEBLY_API_SECRET, my_content, digestmod=hashlib.sha256).hexdigest()
        my_hash = base64.b64encode(my_hmac)
    
        return my_hash

#the same for other functions - make them methods of class
def post(my_url, my_data=None):

    # get url
    full_url = base_url + my_url

    # get hash
    if (my_data == None):
        my_content = 'POST' + '\n' + my_url + '\n'
    else:
        my_content = 'POST' + '\n' + my_url + '\n' + json.dumps(my_data)

    my_hash = weebly_hash(my_content)

    # get headers
    if (my_data == None):
        post_header = {
            'X-Public-Key': WEEBLY_API_KEY,
            'X-Signed-Request-Hash': my_hash,
        }
    else:
        post_header = {
            'Content-Type': 'application/json',
            'X-Public-Key': WEEBLY_API_KEY,
            'X-Signed-Request-Hash': my_hash,
        }

    # send request
    if (my_data == None):
        resp = requests.post(full_url, headers=post_header)
    else:
        resp = requests.post(full_url, data=json.dumps(my_data), headers=post_header)

    return resp


def get(my_url):

    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'GET' + '\n' + my_url + '\n'
    my_hash = weebly_hash(my_content)

    # get headers
    get_header = {
        'X-Public-Key': WEEBLY_API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.get(full_url, headers=get_header)

    return resp


def put(my_url, my_data):
    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'PUT' + '\n' + my_url + '\n' + json.dumps(my_data)
    my_hash = weebly_hash(my_content)

    # get headers
    put_header = {
        'Content-Type': 'application/json',
        'X-Public-Key': WEEBLY_API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.put(full_url, data=json.dumps(my_data), headers=put_header)

    return resp


def patch(my_url, my_data):
    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'PATCH' + '\n' + my_url + '\n' + json.dumps(my_data)
    my_hash = weebly_hash(my_content)

    # get headers
    patch_header = {
        'Content-Type': 'application/json',
        'X-Public-Key': WEEBLY_API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.patch(full_url, data=json.dumps(my_data), headers=patch_header)

    return resp


def delete(my_url):
    full_url = base_url + my_url

    #get hash
    my_content = 'DELETE' + '\n' + my_url + '\n'
    my_hash = weebly_hash(my_content)

    # get headers
    post_header = {
        'X-Public-Key': WEEBLY_API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.delete(full_url, headers=post_header)

    return resp


