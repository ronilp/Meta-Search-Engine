from supporting import struc
from supporting import intersect
from supporting import union

def aggregate(googleResults,yahooResults):
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
            file.write(str(count) + '    ' + googleResults[i].title + ' ' + googleResults[i].description + '\n')
        elif link in yahooURLs:
            count = count + 1
            i = yahooURLs.index(link)
            file.write(str(count) + '    ' + yahooResults[i].title + ' ' + yahooResults[i].description + '\n')
    return uniqueList
