from BeautifulSoup import BeautifulSoup
from supporting import struc
import urllib, urllib2

# Number of results you need to store from each search engine
numresults = 30 

def google_scrape(query):
    googleResults = []
    address = "http://www.google.com/search?q=" + urllib.quote_plus(query) + "&num=" + str(numresults + 2) +"&hl=en&start=0"
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)

    titles = []
    descriptions = []

    headers = soup.findAll('div','rc')
    for header in headers:
        t = header.a.string.encode('utf-8')
        titles.append(t)
        
    desclist = soup.findAll('span','st')
    for desc in desclist:
        d = desc.text.encode('utf-8')
        descriptions.append(d)
        
    size = len(titles)
    
    filename = query + '_Google.txt'
    file = open(filename,"w")
    for i in range(0,size):
        result = struc()    
        result.rank = i+1
        result.title = titles[i]
        result.description = descriptions[i]
        file.write(str(i+1) + '    ' + titles[i] + ' ' + descriptions[i] + '\n')
        googleResults.append(result)
    return googleResults    
