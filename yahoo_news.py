import urllib2
from bs4 import BeautifulSoup

url   = urllib2.urlopen("https://in.finance.yahoo.com/news/netherlands-seeks-join-asian-infrastructure-113916849.html")
soup1  = BeautifulSoup(url)
#print soup1
var2 = soup1.find("p", {"class":"first"})
print var2