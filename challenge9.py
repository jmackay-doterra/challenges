import unittest
import requests
import random
from _common.api import Api

class Challenge9(unittest.TestCase):

    def test_challenge9(self):
        url = "https://www.copart.com/public/lots/search"
        queries = ["jeep", "jeep wrangler", "cherokee", "jeep cherokee", "lamborghini", "ferrari", "mustang",
                   "corvette", "porsche", "chevrolet silverado"]
        headers = Api.getHeaders(self)
        expectedTypes = Api.getExpectedTypes(self)

        for query in range(len(queries)):
            payload = Api.getPayload(self, queries[query])
            response = requests.post(url, data=payload, headers=headers)
            totalElements = str(response.json()['data']['results']['totalElements'])
            print(totalElements + " results for '" + queries[query] + "'")

            print("Validating types of one random object:")
            randomObject = random.randint(1, int(len(response.json())))
            for i in response.json()['data']['results']['content'][randomObject]:
                data = response.json()['data']['results']['content'][randomObject][i]
                print(" ", i, ':', data, type(data))
                assert(type(data)==expectedTypes[i])

            print("--------------------------------------------------")

if __name__ == '__main__':
    unittest.main()