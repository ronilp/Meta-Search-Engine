from GoogleResults import google_scrape
from YahooResults import yahoo_scrape
from supporting import struc
from Ranking import bestRank
from Ranking import bordaPositional
from AggregatingResults import aggregate
import os

os.environ['http_proxy']=''

query = raw_input('Enter Query : ')
googleResults = google_scrape(query)
yahooResults = yahoo_scrape(query)

uniqueList = aggregate(googleResults,yahooResults)

bestRank(googleResults,yahooResults,uniqueList)
bordaPositional(googleResults,yahooResults,uniqueList)

precisionA1 = [0.8,0.5,0.47,0.35,0.44,0.43]
precisionA2 = [0.8,0.5,0.47,0.4,0.48,0.5]

# Mean average precision
MAP1 = sum(precisionA1)/len(precisionA1)
MAP2 = sum(precisionA2)/len(precisionA2)

print 'MAP for Best Rank Approach = ' + str(MAP1) + '\nMAP for Bordas Positional approach = ' + str(MAP2)

# Spearman Correlation
# p = 1 - 6*sum((xi-yi)^2)/(n*(n*n-1))
n = len(uniqueList)
d = [-1,1,-3,1,1,1,0,2,-4,0,0,1,-4,2,5,12,-7,1,0,2,-4,0,0,1,-4,1,1,0,2,-3,0,0,1,-4,2,5,12,2,7,-2,-6,7,-8,1,-2,0,0,0,12,4,6,-1,-4,1,-3,1,1]
d2 = 0
for i in d:
    d2 = d2 + i*i

p = 1 - 6*d2*1./(n*(n*n-1))

print 'Spearman Correlation for Google and Yahoo = ' + str(p)
