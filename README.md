# python_weebly_api
Python functions to simplify interfacing with weebly cloud api

Requires that you fetch the API_KEY and API_SECRET and assign them as follows:

* WEEBLY_API_KEY
* WEEBLY_API_SECRET

For testing, you should create a user account set the user_id as:

* WEEBLY_TEST_ACCOUNT_ID

The following functions are provided:

*     hash = weebly_hash(content)
* response = weebly_get(url)
* response = weebly_post(url, data)
* response = weebly_put(url, data)
* response = weebly_patch(url, data)
* response = weebly_delete(url)

Url should NOT include the base https://api.weeblycloud.com.
Check Weebly documentation for specifics on format of data.

Example usage:

    
        # create new user account
        my_url = 'user/'
        my_data = {'email': 'tester@fake.com'}
        resp = weebly_post(my_url, my_data)
    
    