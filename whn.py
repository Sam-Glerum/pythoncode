#Download and run Anti-Malwarebytes
import urllib

class Download_file(object):
	
	def download_anmb(self):
		link_url = raw_input()
		urllib.urlretrieve(link_url)
		

download_link = Download_file()
download_link.download_anmb()
