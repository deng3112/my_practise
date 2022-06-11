# import logging
from requests.auth import HTTPBasicAuth
import requests
import re
from requests_oauthlib import OAuth1
from requests import Request, Session

# resp = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
# titles = re.findall(pattern,resp.text)
# print(titles)

# print(resp.text)
# resp = requests.get('http://httpbin.org/get')
# print(resp.text)
# data = {
#     'name' : 'germey',
#     'age' : 25
# }
# resp = requests.get('http://httpbin.org/get',params=data)
# print(type(resp.text))
# print(resp.json())

# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
# }
# resp = requests.get('https://github.com/favicon.ico',headers=header,verify=False)
#
#
# logging.captureWarnings(True)
# print(resp.text)
# print(resp.content)

# resp = requests.get('https://ssr1.scrape.center/')
# exit() if not resp.status_code == requests.codes.ok else print('Requests Successfully')

# files = {'file':open('favicon.ico','rb')}
# resp = requests.post('https://httpbin.org/post',files=files)
# print(resp.text)


# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
# headers = {
#     'Cookie': '_octoGH1.1.604123048.1654868221; _device_id=166c2154786154ff5a1ded15cef6e196; user_session=mmdvlObXn4EcbivFNpNrHD21PHGK-psJC-bNsmDx7uNRy23V; __Host-user_session_same_site=mmdvlObXn4EcbivFNpNrHD21PHGK-psJC-bNsmDx7uNRy23V; logged_in=yes; dotcom_user=deng3112; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=OxymzeCIzcYs5THpSc49DdM03D1b6for%2FuWtJISumf0UBg%2B9Vnc%2BMZ2XrVf%2F%2BbomCYqO1JDUGq1cWfSvFKwt6m3iz302hn9%2FZ4Mjc16M05EtGYzcqWt6Vm5N%2BCpXmTScPd%2FsgS5v8VzyGYEscrM6H%2BFwtGu4Mr8j%2BAlwETx%2B0DY5nNrPJSNJphXeHjI%2FvD6T--1yjReVbTB1kdnUH7--SGuN3A7mhUCZ0xHm5C5wSA%3D%3D',
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# resp = requests.get('https://github.com/',headers=headers,verify=False)
# print(resp.text)

# s = requests.Session()
# s.get('https://httpbin.org/cookies/set/number/123456789')
# resp = s.get('https://httpbin.org/cookies')
# print(resp.text)


# response = requests.get('https://ssr2.scrape.center/',timeout='')
# print(response.status_code)

# resp = requests.get('https://ssr3.scrape.center/',auth=('admin','admin'))
# print(resp.status_code)

# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url,auth=auth,verify=False)


# proxies = {
#     'http': 'http://10.10.10.10:1080',
#     'https': 'http://10.10.10.10:1080',
# }
# requests.get("https://httpbin.org/get")




url = 'https://httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
