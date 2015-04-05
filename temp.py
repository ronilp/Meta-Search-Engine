from BeautifulSoup import BeautifulSoup
import urllib, urllib2

query = 'jaguar'

address = "http://www.google.com/search?q=" + urllib.quote_plus(query) + "&num=10&hl=en&start=0"
request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
urlfile = urllib2.urlopen(request)
page = urlfile.read()
soup = BeautifulSoup(page)

print 'done'
