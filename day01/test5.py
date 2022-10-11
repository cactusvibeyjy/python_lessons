import requests

URL = "http://www.naver.com"
response = requests.get(URL)
html_text = response.text
#print(html_text)
print(html_text.find('<h3 class="blind">'))
print(html_text.find('급'))