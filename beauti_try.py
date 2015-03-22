import urllib2
from bs4 import BeautifulSoup

#url1 = urllib2.urlopen("https://google.co.in")
url2 = urllib2.urlopen("https://twitter.com/MishraRahul91")

#soup1 = BeautifulSoup(url1)

#var1 = soup1.find('title')
#print var1.get_text()

soup2 = BeautifulSoup(url2)

var3 = soup2.find('title')
print var3.text

var2 = soup2.find_all('p', {"class" : "ProfileTweet-text js-tweet-text u-dir"})
for items in var2:
	print items.text
	print " "

