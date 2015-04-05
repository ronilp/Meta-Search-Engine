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
