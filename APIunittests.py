import unittest
import requests

# use below to time API response time 
# import time 
# start = time.time()
# roundtrip = time.time() - start

class URLEndpointTests(unittest.TestCase):

    def setUp(self):
        self.url_dist = 'http://localhost:8000/api/v1/racks/{}/{},{}'
        self.url_default = 'http://localhost:8000/api/v1/racks/{},{}'

    def helper_API_get(self, *args):
        if len(args) == 2: 
            url = self.url_default.format(args[0], args[1])
        elif len(args) == 3:
            url = self.url_dist.format(args[0], args[1], args[2])
        else: 
            raise ValueError('Args for url not correct')  

        return requests.get(url)


    def test_API_get_dist_provided_one_rack_returned(self):
        response = self.helper_API_get(30, 45.524433, -122.677825)
        json = response.json()

        self.assertEqual(len(json['racks']), 1)
        self.assertEqual(response.status_code, 200)

    def test_API_get_default_dist_one_rack_returned(self):
        response = self.helper_API_get(45.524433, -122.677825)
        json = response.json()

        self.assertEqual(len(json['racks']), 1)
        self.assertEqual(response.status_code, 200)

    def test_API_get_dist_provided_all_racks_returned_within_30K(self):
        response = self.helper_API_get(30000, 45.524433, -122.677825) 
        json = response.json() 

        # 6746 total number of racks in DB
        self.assertEqual(len(json['racks']), 6746)

    def test_API_get_bad_url_params(self): 
        response = self.helper_API_get("abc", 45.524433, -122.677825)
        self.assertEqual(response.status_code, 404)

        response = self.helper_API_get(50, "SELECT", -122.677825)
        self.assertEqual(response.status_code, 404)

        response = self.helper_API_get(50, 45.66678, "FROM")
        self.assertEqual(response.status_code, 404)

    # you're able to pass inlvaild lat/longs in without decimal points 
    def test_API_get_invalid_lat_long(self):
        response = self.helper_API_get(500, 45524433, -122.677825)
        self.assertEqual(response.status_code, 404)

        response = self.helper_API_get(500, 45.524433, -122677825)
        self.assertEqual(response.status_code, 404)

        response = self.helper_API_get(500, 45, -122)
        self.assertEqual(response.status_code, 404)







if __name__ == '__main__':
    unittest.main()