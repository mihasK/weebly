import unittest

from .utils import *


# Create your tests here.
class WeeblyApiTests(unittest.TestCase):


    def setUp(self):
        self.user_id = WEEBLY_TEST_ACCOUNT_ID


    def test_fetch_user_info(self):
        my_url ='user/' + self.user_id
        resp = get(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['user']['email'], 'tester@fake.com')
        self.assertEqual(resp.json()['user']['test_mode'], True)
        self.assertEqual(resp.json()['user']['language'], 'en')


    def test_change_user_data(self):
        my_url = 'user/' + self.user_id
        my_data = {'email': 'xyz@yoohoo.com', 'test_mode': False, 'language': 'it'}

        resp = patch(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['user']['email'], 'xyz@yoohoo.com')
        self.assertEqual(resp.json()['user']['test_mode'], False)
        self.assertEqual(resp.json()['user']['language'], 'it')


    def test_change_user_data_back(self):
        my_url = 'user/' + self.user_id
        my_data = {'email': 'tester@fake.com', 'test_mode': True, 'language': 'en'}

        resp = put(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['user']['email'], 'tester@fake.com')
        self.assertEqual(resp.json()['user']['test_mode'], True)
        self.assertEqual(resp.json()['user']['language'], 'en')


    def test_disable_user(self):
        my_url = 'user/' + self.user_id + '/disable'

        resp = post(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], True)


    def test_enable_user(self):
        my_url = 'user/' + self.user_id + '/enable'

        resp = post(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], True)


    def test_delete_restore_site(self):
        # get site id
        my_url = 'user/' + self.user_id + '/site'
        resp = get(my_url)
        self.assertEqual(resp.status_code, 200)
        site_id = resp.json()['sites'][0]['site_id']
        domain = resp.json()['sites'][0]['domain']

        # first delete
        my_url = 'user/' + self.user_id + '/site/' + site_id
        resp = delete(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], True)

        # then restore
        my_url = my_url + '/restore'
        my_domain = self.user_id + '.com'
        my_data = {'domain': my_domain}

        resp = post(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], True)


    def test_fetch_user_sites(self):
        my_url = 'user/' + self.user_id + '/site'

        resp = get(my_url)
        self.assertEqual(resp.status_code, 200)
        my_domain = 'www.' + self.user_id + '.com'
        self.assertEqual(resp.json()['sites'][0]['domain'], my_domain)

