from GoogleResults import google_scrape
from YahooResults import yahoo_scrape
from supporting import struc

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

# Assuming same documents have same titles, 
# we can find the unique documents by taking union of the search results
'''
filename = 'UniqueDocuments.txt'
file = open(filename,"w")
for i in range(0,size):
    file.write(str(i+1) + '    ' + unique.title[i] + ' ' + unique.description[i] + '\n')
'''
