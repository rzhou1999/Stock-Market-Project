import collections
import string
from AccessDatabase import *

def generateProbabilitiesDB():
    generateProbabilities(getLikelyArticles())

#when called, will take in input from files "20" and "20n", and then look up relevant articles in the database that fit some criteria defined in AccessDatabase.py
#probability is then taken from each set of articles by putting all of their contents into a set and then counting them
#stopwords are filtered out, and the top 20 of each are then combined to create a final probability for each token
#these are then writtem to keys.py
def generateProbabilities(fromDB = [[],[]]):
    words = file("20", "r").read().split("@@@@")
    if len(fromDB[0])!=0:
        words.extend(fromDB[0])
    articleList = map(lambda x:list(set(x.translate(None, string.punctuation).lower().split())),words)
    x = []
    for article in articleList:
        x.extend(article)
    counter = collections.Counter(x)
    splits = counter.most_common(80)

    wordsN = file("20n", "r").read().split("@@@@")
    if len(fromDB[1])!=0:
        wordsN.extend(fromDB[1])
    articleList = map(lambda x:list(set(x.translate(None, string.punctuation).lower().split())),wordsN)
    x = []
    for article in articleList:
        x.extend(article)
    counter = collections.Counter(x)
    notSplits = counter.most_common(80)

    stopwords = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']
    splits = filter(lambda x:not x[0] in stopwords,splits)[:40]
    notSplits = filter(lambda x:not x[0] in stopwords,notSplits)[:40]


    splitD = dict(splits)
    notSplitD = dict(notSplits)
    finalD = {}

    for i in splitD:
        finalD[i] = (splitD[i] - notSplitD.get(i, 0))/(len(words)*1.0)
    for i in notSplitD:
        finalD[i] = (-notSplitD[i] + splitD.get(i, 0))/(len(wordsN)*1.0)
    print "Total tokens recorded: " + str(len(finalD))
    sortedL = sorted(finalD.items(), key=lambda x: x[1])
    keys = open("keys.py","w")
    keys.write("#"+str(len(finalD)))
    keys.write("\nkeys={" + ','.join(map(lambda i:"\n'"+i[0]+"': "+str(i[1]),sortedL))+"\n}")
    keys.close()
