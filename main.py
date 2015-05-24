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
n = 30
dg = [-1,11,-3,1,21,17,0,2,-4,20,10,1,-4,2,5,22,-7,1,9,24,-4,0,0,1,-4,15,18,0,2,-12]
dg2 = 0
for i in dg:
    dg2 = dg2 + i*i

dy = [1,-4,2,9,22,-7,-21,11,0,2,-14,20,10,11,9,24,-4,12,-2,1,-4,15,18,0,2,-12,11,-3,1,21]
dy2 = 0
for i in dy:
    dy2 = dy2 + i*i

p1 = 1 - 6*dg2*1./(n*(n*n-1))
p2 = 1 - 6*dy2*1./(n*(n*n-1))

print 'Spearman Correlation for Best Rank Approach = ' + str(p1)
print 'Spearman Correlation for Bordas Positional Approach = ' + str(p2)
