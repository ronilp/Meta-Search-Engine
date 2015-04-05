from supporting import struc
import operator

def LpNorm(Google,Yahoo,p):
    return Google**p + Yahoo**p

def printResults(newRankList,uniqueList,googleResults,yahooResults,googleURLs,yahooURLs,ul,filename):
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
        newRankList.append(result)
        
    newRankList.sort(key=operator.attrgetter('rank'))
    
    file = open(filename,"w")
    count = 0
    for result in newRankList:
        count = count + 1
        file.write(str(count) + '    ' + result.title + '    ' + result.description + '\n')
    return

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
    filename = 'ResultantRanks_A1.txt'
    printResults(BestRankResults,uniqueList,googleResults,yahooResults,googleURLs,yahooURLs,ul,filename)
    return

def bordaPositional(googleResults,yahooResults,uniqueList):
    googleURLs = []
    yahooURLs = []
    for result in googleResults:
        googleURLs.append(result.url)

    for result in yahooResults:
        yahooURLs.append(result.url)    
    ul = []
    for i in range(0,len(uniqueList)):
        x = 0
        y = 0
        if uniqueList[i] in googleURLs:
            x = googleURLs.index(uniqueList[i])
        if uniqueList[i] in yahooURLs:
            y = yahooURLs.index(uniqueList[i])
        z = LpNorm(x,y,1)
        ul.append(z)
    BordaPositionalResults = []
    filename = 'ResultantRanks_A2.txt'
    printResults(BordaPositionalResults,uniqueList,googleResults,yahooResults,googleURLs,yahooURLs,ul,filename)
    return
