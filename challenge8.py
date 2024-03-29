import unittest
import requests
from _common.api import Api

class Challenge8(unittest.TestCase):

    def test_challenge8(self):
        url = "https://www.copart.com/public/lots/search"
        queries = ["jeep", "jeep wrangler", "cherokee", "jeep cherokee", "lamborghini", "ferrari", "mustang",
                   "corvette", "porsche", "chevrolet silverado"]
        headers = Api.getHeaders(self)

        for query in range(len(queries)):
            payload = Api.getPayload(self, queries[query])
            response = requests.post(url, data=payload, headers=headers)
            totalElements = str(response.json()['data']['results']['totalElements'])
            print(totalElements + " results for '" + queries[query] + "'")

if __name__ == '__main__':
    unittest.main()