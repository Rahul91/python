import urllib2
from bs4 import BeautifulSoup
#from mechanize import Browser


#br = Browser()
#br.set_handle_robots(False)

state = raw_input("Enter the name of the state : ")
city  = raw_input("Enter the name of the city : ")


request = 'https://in.weather.yahoo.com/india/%s/%s-2295412/' %(state, city)
print request

#url = br.open(request)

url = urllib2.urlopen(request)
#url1 = urllib2.urlopen("https://in.weather.yahoo.com/india/maharashtra/pune/")
soup = BeautifulSoup(url)

var1 = soup.find("div", {"class" : "day-temp-current temp-c "})
print var1.text




<script type="text/javascript" src="http://www.webestools.com/google_map_gen.js?lati=22.467555&long=88.412116&zoom=14&width=630&height=400&mapType=normal&map_btn_normal=yes&map_btn_satelite=yes&map_btn_mixte=yes&map_small=yes&marqueur=yes&info_bulle="></script><br /><a href="http://www.webestools.com/google-maps-code-generator-insert-map-on-website-javascript-free-google-map-script.html">Google Maps code Generator</a>