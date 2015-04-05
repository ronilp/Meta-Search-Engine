from BeautifulSoup import BeautifulSoup
from collections import namedtuple
import urllib, urllib2

# Number of results you need to store from each search engine
numresults = 30 

class struc:
    def __init__(self):
        self.title = ''
        self.description = ''

def find_between(s, first, last):
    start = s.index(first) + len(first)
    end = s.index(last, start)
    return s[start:end]

def yahoo_scrape(query):
    yahooResults = []
    address = "https://search.yahoo.com/search?p=" + query + "&n=" + str(numresults)
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)
    '''
    s = soup.findAll('div','compTitle')
    for i in s:
        print i.prettify()
    '''
    title = []
    description = []

    headers = soup.findAll('div','compTitle')
    for header in headers:
        if header is not None:
            t = header.a.text.encode('utf-8')
            title.append(t)
    
    desclist = soup.findAll('div','compText aAbs')
    for desc in desclist:
        if desc is not None:
            d = desc.text.encode('utf-8')
            description.append(d)

    return yahooResults
    
'''
    title = []
    description = []

    headers = soup.findAll('div','rc')
    for header in headers:
        t = header.a.string.encode('utf-8')
        title.append(t)
        
    desclist = soup.findAll('span','st')
    for desc in desclist:
        isSubstring = '<span class="st">' in str(desc)
        if isSubstring:
            d = find_between(str(desc),'<span class="st">','</span>')
        else:
            d = find_between(str(desc),'<span class="_dwd st s std" style="','</span>')
        description.append(d)
        
    urllist = soup.findAll()
        
    size = len(title)
    
    filename = query + '_google.txt'
    file = open(filename,"w")
    for i in range(0,size):
        result.rank = i+1
        result.title = title
        result.description = description
        file.write(str(i+1) + '    ' + title[i] + ' ' + description[i] + '\n')
    googleResults.append(result)
'''
''' 
    for each in googleResults:
        print each.rank
        print each.title
        print each.description
'''

    
result = struc()
links = yahoo_scrape('jaguar')
