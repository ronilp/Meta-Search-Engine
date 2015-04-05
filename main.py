from GoogleResults import google_scrape
from YahooResults import yahoo_scrape
from supporting import struc
from supporting import intersect
from supporting import union

query = raw_input('Enter Query : ')
googleResults = google_scrape(query)
yahooResults = yahoo_scrape(query)
'''
for each in googleResults:
    print each.rank
    print each.title
    print each.description

for each in yahooResults:
    print each.rank
    print each.title
    print each.description
'''

l1 = []
l2 = []
uniques = struc()
for each in googleResults:
    l1.append(each.url)
    
for each in yahooResults:
    l2.append(each.url)

uniqueList = union(l1,l2)

# Common Results
print(intersect(l1,l2))
print str(len(l1)) + ' Google Results, ' + str(len(l2)) + ' Yahoo results, ' + str(len(uniqueList)) + ' Unique Results'

googleURLs = []
yahooURLs = []

for result in googleResults:
    googleURLs.append(result.url)

for result in yahooResults:
    yahooURLs.append(result.url)

# Writing Aggregated Documents
filename = 'UniqueDocuments.txt'
file = open(filename,"w")
count = 0
for link in uniqueList:
    if link in googleURLs:
        count = count + 1
        i = googleURLs.index(link)
        file.write(str(count) + '    ' + unique.title[i] + ' ' + unique.description[i] + '\n')
        print count
        print link
    elif link in yahooURLs:
        count = count + 1
        i = yahooURLs.index(link)
        file.write(str(count) + '    ' + unique.title[i] + ' ' + unique.description[i] + '\n')
        print count
        print link


