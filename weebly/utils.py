import requests
import hashlib
import hmac
import json
import base64

base_url = 'https://api.weeblycloud.com/'


def weebly_hash(my_content):
    my_hmac = hmac.new(WEEBLY_API_SECRET, my_content, digestmod=hashlib.sha256).hexdigest()
    my_hash = base64.b64encode(my_hmac)

    return my_hash


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


def create_user():
    # create test account
    my_url = 'user/'
    my_data = {'email': 'tester@fake.com'}
    resp = post(my_url, my_data)

    if (resp.status_code == 200):
        user_id = resp.json()['user']['user_id']
        print('Successfully created tester@fake.com')
    else:
        print('Couldn\'t create tester@fake.com. Does it already exist?')


def create_site():
    # create test site
    my_url = 'user/' + WEEBLY_TEST_ACCOUNT_ID + '/site'
    my_domain = WEEBLY_TEST_ACCOUNT_ID + '.com'
    my_data = {'domain': my_domain, 'site_title': 'My Test Website'}
    resp = post(my_url, my_data)
    if (resp.status_code == 200):
        print('Successfully created ' + WEEBLY_TEST_ACCOUNT_ID + '.com')
    else:
        print('Couldn\'t create ' + WEEBLY_TEST_ACCOUNT_ID + '.com. Does it already exist?')