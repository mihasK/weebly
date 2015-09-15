# weebly
Python functions to simplify interfacing with weebly cloud api

Setup:
Fetch API_KEY and API_SECRET from your Weebly Cloud Dashboard and import them. Also include the user_id of a 
test account.

* WEEBLY_API_KEY
* WEEBLY_API_SECRET
* WEEBLY_TEST_ACCOUNT_ID

For testing, you should create a user account set the user_id as:

* WEEBLY_TEST_ACCOUNT_ID

The following functions are provided:

*     hash = weebly_hash(content)
* response = weebly.get(url)
* response = weebly.post(url, data)
* response = weebly.put(url, data)
* response = weebly.patch(url, data)
* response = weebly.delete(url)
* response = weebly.loginlink(user_id)

Url should NOT include the base https://api.weeblycloud.com.
Check Weebly documentation for specifics on format of data.

Example usage:

        # create new user account
        import weebly
        my_url = 'user/'
        my_data = {'email': 'tester@fake.com'}
        resp = weebly.post(my_url, my_data)
    
    