import urllib2
response = urllib2.urlopen('http://downloads.malwarebytes.org/file/mbam/')
html = response.read()
