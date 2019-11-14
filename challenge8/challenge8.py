import unittest
import requests
from selenium import webdriver


class Challenge8(unittest.TestCase):

    def test_challenge8(self):
        url = "https://www.copart.com/public/lots/search"
        headers = {
            'authority':"www.copart.com",
            'accept':"application/json, text/javascript, */*; q=0.01",
            'accept-encoding':"gzip, deflate, br",
            'accept-language':"en-US,en;q=0.9",
            'cache-control':"no-cache,no-cache",
            'content-type':"multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cookie':"visid_incap_242093=QZlfrbMbSoyHPi2at53GqYBrdl0AAAAAQUIPAAAAAAA5O3W1OQtvDOY3cgzyBCZl; _ga=GA1.2.1599021799.1568041858; s_fid=1B0AD7A7660F17FC-2EE0842E93BD99A4; OAID=e95e23c3cb89d426bea9e8b5c60e2993; s_vi=[CS]v1|2EBB35C185079D36-6000010F20002D10[CE]; __gads=ID=ce3f3f8b5296b295:T=1568041858:S=ALNI_MYuArmPw4Ci1K1wFRgkeLGB-Ht98Q; _fbp=fb.1.1568041860548.937556269; __cfduid=d73e6d21e38b7f51c1f71a78c1c8f69821568042515; g2app.searchResultsPageLength=20; g2usersessionid=b059377eb1fae1b858f4e810aca4e1db; G2JSESSIONID=3DDAFDE27FF9B092E86B09B0C8CBD27C-n2; userLang=en; incap_ses_517_242093=YzK8a8l/RE0xr1JPU8IsB9N4zV0AAAAAc9srK5933cl+XETxFq8IcA==; timezone=America%2FDenver; copartTimezonePref=%7B%22displayStr%22%3A%22MST%22%2C%22offset%22%3A-7%2C%22dst%22%3Afalse%2C%22windowsTz%22%3A%22America%2FDenver%22%7D; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22Utah%22%2C%22stateCode%22%3A%22UT%22%2C%22cityName%22%3A%22Pleasant%20Grove%22%2C%22latitude%22%3A40.38462%2C%22longitude%22%3A-111.73638%2C%22zipCode%22%3A%2284062%22%2C%22timeZone%22%3A%22-06%3A00%22%7D; _gid=GA1.2.1277846724.1573746903; _gat=1; s_depth=1; s_pv=public%3Ahomepage; s_vnum=1576338902839%26vn%3D1; s_invisit=true; s_lv_s=More%20than%207%20days; s_cc=true; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; usersessionid=79423db72fe159b4ef3a425b9e423f26; s_ppvl=public%253Ahomepage%2C15%2C15%2C579%2C1920%2C578%2C1920%2C1080%2C1%2CP; s_nr=1573746921213-Repeat; s_lv=1573746921215; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dpublic%25253Ahomepage%2526link%253D%25252Fimages%25252Ficons%25252Ficon_Search_Desktop.svg%2526region%253Dsearch-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dpublic%25253Ahomepage%2526pidt%253D1%2526oid%253D%25250A%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%25250A%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%2526oidt%253D3%2526ot%253DSUBMIT; s_ppv=public%253Ahomepage%2C58%2C15%2C579%2C1920%2C578%2C1920%2C1080%2C1%2CP, visid_incap_242093=QZlfrbMbSoyHPi2at53GqYBrdl0AAAAAQUIPAAAAAAA5O3W1OQtvDOY3cgzyBCZl; _ga=GA1.2.1599021799.1568041858; s_fid=1B0AD7A7660F17FC-2EE0842E93BD99A4; OAID=e95e23c3cb89d426bea9e8b5c60e2993; s_vi=[CS]v1|2EBB35C185079D36-6000010F20002D10[CE]; __gads=ID=ce3f3f8b5296b295:T=1568041858:S=ALNI_MYuArmPw4Ci1K1wFRgkeLGB-Ht98Q; _fbp=fb.1.1568041860548.937556269; __cfduid=d73e6d21e38b7f51c1f71a78c1c8f69821568042515; g2app.searchResultsPageLength=20; g2usersessionid=b059377eb1fae1b858f4e810aca4e1db; G2JSESSIONID=3DDAFDE27FF9B092E86B09B0C8CBD27C-n2; userLang=en; incap_ses_517_242093=YzK8a8l/RE0xr1JPU8IsB9N4zV0AAAAAc9srK5933cl+XETxFq8IcA==; timezone=America%2FDenver; copartTimezonePref=%7B%22displayStr%22%3A%22MST%22%2C%22offset%22%3A-7%2C%22dst%22%3Afalse%2C%22windowsTz%22%3A%22America%2FDenver%22%7D; g2app.locationInfo=%7B%22countryCode%22%3A%22USA%22%2C%22countryName%22%3A%22United%20States%22%2C%22stateName%22%3A%22Utah%22%2C%22stateCode%22%3A%22UT%22%2C%22cityName%22%3A%22Pleasant%20Grove%22%2C%22latitude%22%3A40.38462%2C%22longitude%22%3A-111.73638%2C%22zipCode%22%3A%2284062%22%2C%22timeZone%22%3A%22-06%3A00%22%7D; _gid=GA1.2.1277846724.1573746903; _gat=1; s_depth=1; s_pv=public%3Ahomepage; s_vnum=1576338902839%26vn%3D1; s_invisit=true; s_lv_s=More%20than%207%20days; s_cc=true; OAGEO=US%7C%7C%7C%7C%7C%7C%7C%7C%7C%7C; usersessionid=79423db72fe159b4ef3a425b9e423f26; s_ppvl=public%253Ahomepage%2C15%2C15%2C579%2C1920%2C578%2C1920%2C1080%2C1%2CP; s_nr=1573746921213-Repeat; s_lv=1573746921215; s_sq=copart-g2-us-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dpublic%25253Ahomepage%2526link%253D%25252Fimages%25252Ficons%25252Ficon_Search_Desktop.svg%2526region%253Dsearch-form%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dpublic%25253Ahomepage%2526pidt%253D1%2526oid%253D%25250A%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%25250A%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%252520%2526oidt%253D3%2526ot%253DSUBMIT; s_ppv=public%253Ahomepage%2C58%2C15%2C579%2C1920%2C578%2C1920%2C1080%2C1%2CP; visid_incap_242093=QZlfrbMbSoyHPi2at53GqYBrdl0AAAAAQUIPAAAAAAA5O3W1OQtvDOY3cgzyBCZl; G2JSESSIONID=4CD0325F414C60772D2D08C34655A28E-n2; g2usersessionid=b059377eb1fae1b858f4e810aca4e1db; incap_ses_517_242093=YzK8a8l/RE0xr1JPU8IsB9N4zV0AAAAAc9srK5933cl+XETxFq8IcA==; ___utmvbOauElvV=a; ___utmvmOauElvV=a",
            'origin':"https://www.copart.com",
            'pragma':"no-cache",
            'referer':"https://www.copart.com",
            'sec-fetch-mode':"cors",
            'sec-fetch-site':"same-origin",
            'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            'x-requested-with':"XMLHttpRequest",
            'x-xsrf-token':"f4113ad8-ff8d-4aca-8a31-e6db64504a7d",
            'Postman-Token':"3bb63a48-217d-483e-ae30-5a2306c9900d,db1a0766-edde-423f-8434-3760ea6ce8a9",
            'Host':"www.copart.com",
            'Content-Length':"13032",
            'Connection':"keep-alive"
        }
        queries = ["jeep", "jeep wrangler", "cherokee", "jeep cherokee", "lamborghini", "ferrari", "mustang",
                   "corvette", "porsche", "chevrolet silverado"]

        for query in range(len(queries)):
            payload = self.getPayload(queries[query])
            response = requests.request("POST", url, data=payload, headers=headers)
            totalElements = str(response.json()['data']['results']['totalElements'])
            print(totalElements + " results for '" + queries[query] + "'")

    def getPayload(self, searchQuery):
        payload = "" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"draw\"\r\n\r\n 1\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[0][data]\"\r\n\r\n 0\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[0][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[0][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[0][orderable]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[0][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[0][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[1][data]\"\r\n\r\n 1\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[1][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[1][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[1][orderable]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[1][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[1][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[2][data]\"\r\n\r\n 2\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[2][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[2][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[2][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[2][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[2][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[3][data]\"\r\n\r\n 3\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[3][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[3][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[3][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[3][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[3][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[4][data]\"\r\n\r\n 4\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[4][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[4][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[4][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[4][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[4][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[5][data]\"\r\n\r\n 5\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[5][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[5][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[5][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[5][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[5][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[6][data]\"\r\n\r\n 6\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[6][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[6][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[6][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[6][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[6][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[7][data]\"\r\n\r\n 7\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[7][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[7][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[7][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[7][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[7][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[8][data]\"\r\n\r\n 8\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[8][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[8][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[8][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[8][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[8][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[9][data]\"\r\n\r\n 9\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[9][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[9][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[9][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[9][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[9][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[10][data]\"\r\n\r\n 10\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[10][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[10][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[10][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[10][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[10][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[11][data]\"\r\n\r\n 11\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[11][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[11][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[11][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[11][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[11][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[12][data]\"\r\n\r\n 12\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[12][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[12][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[12][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[12][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[12][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[13][data]\"\r\n\r\n 13\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[13][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[13][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[13][orderable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[13][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[13][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[14][data]\"\r\n\r\n 14\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[14][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[14][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[14][orderable]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[14][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[14][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[15][data]\"\r\n\r\n 15\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[15][name]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[15][searchable]\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[15][orderable]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[15][search][value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"columns[15][search][regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"start\"\r\n\r\n 0\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"length\"\r\n\r\n 20\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"search[value]\"\r\n\r\n \r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"search[regex]\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"query\"\r\n\r\n " + searchQuery + "\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"watchListOnly\"\r\n\r\n false\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"freeFormSearch\"\r\n\r\n true\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"page\"\r\n\r\n 0\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition:form-data; name=\"size\"\r\n\r\n 20\r\n" \
            "------WebKitFormBoundary7MA4YWxkTrZu0gW--"

        # payload = {
        #     "draw": "1",
        #     "columns[0][data]": "0",
        #     "columns[0][name]": "",
        #     "columns[0][searchable]": "true",
        #     "columns[0][orderable]": "false",
        #     "columns[0][search][value]": "",
        #     "columns[0][search][regex]": "false",
        #     "columns[1][data]": "1",
        #     "columns[1][name]": "",
        #     "columns[1][searchable]": "true",
        #     "columns[1][orderable]": "false",
        #     "columns[1][search][value]": "",
        #     "columns[1][search][regex]": "false",
        #     "columns[2][data]": "2",
        #     "columns[2][name]": "",
        #     "columns[2][searchable]": "true",
        #     "columns[2][orderable]": "true",
        #     "columns[2][search][value]": "",
        #     "columns[2][search][regex]": "false",
        #     "columns[3][data]": "3",
        #     "columns[3][name]": "",
        #     "columns[3][searchable]": "true",
        #     "columns[3][orderable]": "true",
        #     "columns[3][search][value]": "",
        #     "columns[3][search][regex]": "false",
        #     "columns[4][data]": "4",
        #     "columns[4][name]": "",
        #     "columns[4][searchable]": "true",
        #     "columns[4][orderable]": "true",
        #     "columns[4][search][value]": "",
        #     "columns[4][search][regex]": "false",
        #     "columns[5][data]": "5",
        #     "columns[5][name]": "",
        #     "columns[5][searchable]": "true",
        #     "columns[5][orderable]": "true",
        #     "columns[5][search][value]": "",
        #     "columns[5][search][regex]": "false",
        #     "columns[6][data]": "6",
        #     "columns[6][name]": "",
        #     "columns[6][searchable]": "true",
        #     "columns[6][orderable]": "true",
        #     "columns[6][search][value]": "",
        #     "columns[6][search][regex]": "false",
        #     "columns[7][data]": "7",
        #     "columns[7][name]": "",
        #     "columns[7][searchable]": "true",
        #     "columns[7][orderable]": "true",
        #     "columns[7][search][value]": "",
        #     "columns[7][search][regex]": "false",
        #     "columns[8][data]": "8",
        #     "columns[8][name]": "",
        #     "columns[8][searchable]": "true",
        #     "columns[8][orderable]": "true",
        #     "columns[8][search][value]": "",
        #     "columns[8][search][regex]": "false",
        #     "columns[9][data]": "9",
        #     "columns[9][name]": "",
        #     "columns[9][searchable]": "true",
        #     "columns[9][orderable]": "true",
        #     "columns[9][search][value]": "",
        #     "columns[9][search][regex]": "false",
        #     "columns[10][data]": "10",
        #     "columns[10][name]": "",
        #     "columns[10][searchable]": "true",
        #     "columns[10][orderable]": "true",
        #     "columns[10][search][value]": "",
        #     "columns[10][search][regex]": "false",
        #     "columns[11][data]": "11",
        #     "columns[11][name]": "",
        #     "columns[11][searchable]": "true",
        #     "columns[11][orderable]": "true",
        #     "columns[11][search][value]": "",
        #     "columns[11][search][regex]": "false",
        #     "columns[12][data]": "12",
        #     "columns[12][name]": "",
        #     "columns[12][searchable]": "true",
        #     "columns[12][orderable]": "true",
        #     "columns[12][search][value]": "",
        #     "columns[12][search][regex]": "false",
        #     "columns[13][data]": "13",
        #     "columns[13][name]": "",
        #     "columns[13][searchable]": "true",
        #     "columns[13][orderable]": "true",
        #     "columns[13][search][value]": "",
        #     "columns[13][search][regex]": "false",
        #     "columns[14][data]": "14",
        #     "columns[14][name]": "",
        #     "columns[14][searchable]": "true",
        #     "columns[14][orderable]": "false",
        #     "columns[14][search][value]": "",
        #     "columns[14][search][regex]": "false",
        #     "columns[15][data]": "15",
        #     "columns[15][name]": "",
        #     "columns[15][searchable]": "true",
        #     "columns[15][orderable]": "false",
        #     "columns[15][search][value]": "",
        #     "columns[15][search][regex]": "false",
        #     "start": "0",
        #     "length": "20",
        #     "search[value]": "",
        #     "search[regex]": "false",
        #     "query": searchQuery,
        #     "watchListOnly": "false",
        #     "freeFormSearch": "true",
        #     "page": "0",
        #     "size": "20"
        # }
        return payload

if __name__ == '__main__':
    unittest.main()