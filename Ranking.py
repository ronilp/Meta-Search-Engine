from supporting import struc
import operator

def minRank(Google,Yahoo):
    if Google.rank <= Yahoo.rank:
        return Google
    else:
        return Yahoo

def LpNorm(Google,Yahoo,p):
    return Google**p + Yahoo**p

def bestRank(googleResults,yahooResults,uniqueList):
    googleURLs = []
    yahooURLs = []
    for result in googleResults:
        googleURLs.append(result.url)

    for result in yahooResults:
        yahooURLs.append(result.url)    
    ul = []
    for i in range(0,len(uniqueList)):
        x = 100
        y = 100
        if uniqueList[i] in googleURLs:
            x = googleURLs.index(uniqueList[i])
        if uniqueList[i] in yahooURLs:
            y = yahooURLs.index(uniqueList[i])
        if x<y:
            z = x + 0.25
        else:
            z = y + 0.5
        ul.append(z)

    BestRankResults = []
    for i in range(0,len(uniqueList)):
        result = struc()
        result.url = uniqueList[i]
        result.rank = ul[i]
        if uniqueList[i] in googleURLs:
            ind = googleURLs.index(uniqueList[i])
            result.title = googleResults[ind].title
            result.description = googleResults[ind].description           
        else:
            ind = yahooURLs.index(uniqueList[i])
            result.title = yahooResults[ind].title
            result.description = yahooResults[ind].description
        BestRankResults.append(result)
        
    BestRankResults.sort(key=operator.attrgetter('rank'))

    filename = 'ResultantRanks_A1.txt'
    file = open(filename,"w")
    count = 0
    for result in BestRankResults:
        count = count + 1
        file.write(str(count) + '    ' + result.title + ' ' + result.description + '\n')
    
    return BestRankResults

def bordaPositional(googleResults,yahooResults):
    size = len(googleResults)
    for Google,Yahoo in range(0,size):
        newRank = LpNorm(Google,Yahoo,1)
    return    
