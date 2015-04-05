from BeautifulSoup import BeautifulSoup
from supporting import struc
import urllib, urllib2

# Number of results you need to store from each search engine
numresults = 30 

def yahoo_scrape(query):
    yahooResults = []
    address = "https://search.yahoo.com/search?p=" + query + "&n=" + str(numresults)
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)

    titles = []
    descriptions = []
    urls = []

    headers = soup.findAll('div','compTitle')
    for header in headers:
        if header is not None:
            t = header.a.text.encode('utf-8')
            u = header.a.get('href')
            urls.append(u)
            titles.append(t)
    
    desclist = soup.findAll('div','compText aAbs')
    for desc in desclist:
        if desc is not None:
            d = desc.text.encode('utf-8')
            descriptions.append(d)
            
    size = len(titles)
    
    filename = query + '_Yahoo.txt'
    file = open(filename,"w")
    for i in range(0,size):
        result = struc()
        result.rank = i+1
        result.title = titles[i]
        result.description = descriptions[i]
        result.url = urls[i]
        file.write(str(i+1) + '    ' + titles[i] + ' ' + descriptions[i] + '\n')
        yahooResults.append(result)

    return yahooResults
