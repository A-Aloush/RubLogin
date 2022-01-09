import requests
from bs4 import BeautifulSoup

ip = 'https://login.ruhr-uni-bochum.de/cgi-bin/start'

b = BeautifulSoup(requests.get(ip).content, "html.parser")
s = b.find_all(type="ipaddr")

url = 'https://login.ruhr-uni-bochum.de/cgi-bin/laklogin'
values = {  'code':'1',
            'loginid':'username',
            'password':'password',
            'ipaddr':str(s).split("value")[1][2:-4],
            'action':'Login'    }

r = requests.post(url, data=values)
