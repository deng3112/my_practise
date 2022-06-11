import logging

import requests
import re

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

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}
resp = requests.get('https://github.com/favicon.ico',headers=header,verify=False)


logging.captureWarnings(True)
print(resp.text)
print(resp.content)