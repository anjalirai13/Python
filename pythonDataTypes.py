# Python Data types

num = 100
print "num is ", num, "and type is ", type(num), "is it int", type(num) is int

welcomeStr = "Hello Python"
print "str is ", welcomeStr, "and type is ", type(welcomeStr) 

sampleList = ['abcd', 786, 2.23, 'john', 70.2]
print "list is ", sampleList, "and type is ", type(sampleList)

sampleTuple = ('abcd', 786, 2.23, 'john', 70.2)
print "tuple is ", sampleTuple, "and type is ", type(sampleTuple)

sampleDict = {'name': 'Anjali', 'code': 1309, 'dept': 'search in progress'}
print "Dictionary is ", sampleDict, "and type is ", type(sampleDict)
print "dictionary keys is ", sampleDict.keys(), "dictionary values is ", sampleDict.values()

# Diff b/w list and tuple
sampleList[2] = 1000     # List updation is possible
# tuple[5] = 500         # Uncomment and run. Throws exception, updation is not possible