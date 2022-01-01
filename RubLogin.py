import requests

url = 'https://login.ruhr-uni-bochum.de/cgi-bin/laklogin'
values = {  'code':'1',
            'loginid':'username',
            'password':'password',
            'ipaddr':'your-IP',
            'action':'Login'    }

r = requests.post(url, data=values)
