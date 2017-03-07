import urllib2, urllib, json
import requests
from requests_oauthlib import OAuth1

CLIENTKEY = 'dj0yJmk9b2dIcVhnbXNGdVdZJmQ9WVdrOVFrWlZUV3hQTkdFbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hNQ--'
CLIENTSECRET = '6cc877ab42a0c65fb61ce4b18c3b0e276accb090'

baseurl = "https://query.yahooapis.com/v1/yql?"

def queryFromList(input):
    if len(input) == 0:
        raise ValueError('0 element list provided.')
    returnList = []
    for i in input:
        returnList.append(querySingle(i))
    return returnList

def querySingle(input):
    yql_query = 'select * from pm.finance.articles where symbol in ("'+input+'")'
    query = {
        'q': yql_query,
        'format': 'json',
        'env': 'store://datatables.org/alltableswithkeys'
    }

    yql_url = baseurl + urllib.urlencode(query)
    queryoauth = OAuth1(CLIENTKEY, CLIENTSECRET, signature_type='query')
    return requests.get(url=yql_url, auth=queryoauth).content