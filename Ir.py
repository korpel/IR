


import urllib, urllib2
from bs4 import BeautifulSoup
import requests
import sys
'''
import SimpleHTTPServer
import SocketServer

PORT = 8888

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
'''


googleDict = dict()
yahooDict = dict()
bingDict = dict()
allLists = []
allListsDict = dict()
listYG = []
listGB = []
listYB = []

dictYG = dict()
dictYB = dict()
dictGB = dict()



numresults = 100

def google_scrape(query):
    ctr2 = 100
    address = "http://www.google.com/search?q=" + urllib.quote_plus(query) + "&num=" + str(numresults) +"&hl=en&start=0"
    request = urllib2.Request(address, None, {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page, "html.parser")


    headers = soup.findAll('div','rc')
    for header in headers:
    	header.a.string.encode('utf-8')
        k = header.a.get('href')
        u = k.decode('utf-8')
        u = u.rstrip('/')
        googleDict[u] = ctr2
        ctr2 = ctr2 - 1
        if ctr2 ==  -1:
            return
    return 


def bing_scrape(query):
    ctr2 = 100
    for i in range(0,2):
        url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
        payload = {
        	'q': query,
        	'count': numresults,
            'offset' : i*50
        	}
        headers = {'Ocp-Apim-Subscription-Key': '5e55ee0ca47e47b283dbc95988bc54d3'}
        r = requests.get(url, params=payload, headers=headers)
        k = r.json()
        p = k['webPages']['value']
        s = len(p)
        for i in range(0, len(p)):
            t = p[i]['displayUrl']
            t = t.strip('/') 
            bingDict[t] = ctr2
            ctr2 = ctr2 - 1
    return 


def yahoo_scrape(query):
    ctr2 = 100
    counter = 10
    ranger = numresults/10 
    for ctr in range(0,ranger):
        address = "https://search.yahoo.com/search?p=" + query + "&b=" + str(counter)
        request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
        urlfile = urllib2.urlopen(request)
        page = urlfile.read()
        soup = BeautifulSoup(page, "lxml")
        headers = soup.findAll('h3', {"class": "title"})
        for header in headers:
            if not header.a:
                continue
            k = header.a.get('href')
            u = k.decode('utf-8')
            u = u.rstrip('/')
            yahooDict[u] = ctr2
            ctr2 = ctr2 - 1
            if ctr2 == -1:
                return
        counter += 10
    return


with open('IrQuery.txt', 'r') as IrQueryFile:
    query = IrQueryFile.read()
query = query.decode('utf-8')

with open('IrEngines.txt', 'r') as IrEnginesFile:
    IrEnginesValue = IrEnginesFile.read()
IrEnginesValue = IrEnginesValue.decode('utf-8')

googleBool = IrEnginesValue[0]
yahooBool = IrEnginesValue[1]
bingBool = IrEnginesValue[2]

if googleBool == '1':
    google_scrape(query)
if yahooBool == '1':
    yahoo_scrape(query)
if bingBool == '1':
    bing_scrape(query)
allLists = list(set(googleDict.keys()) & set(yahooDict.keys()) & set(bingDict.keys()))
for key in allLists:
    allListsDict[key] = googleDict[key] + yahooDict[key] + bingDict[key]
    del googleDict[key]
    del yahooDict[key]
    del bingDict[key]

listYB = list(set(yahooDict.keys()) & set(bingDict.keys()))
listGB = list(set(googleDict.keys()) & set(bingDict.keys()))
listYG = list(set(yahooDict.keys()) & set(googleDict.keys()))


for key in listYB:
    dictYB[key] = yahooDict[key] + bingDict[key]
    del yahooDict[key]
    del bingDict[key]

for key in listGB:
    dictGB[key] = googleDict[key] + bingDict[key]
    del googleDict[key]
    del bingDict[key]

for key in listYG:
    dictYG[key] = yahooDict[key] + googleDict[key]
    del yahooDict[key]
    del googleDict[key]



print('\n')
print('G+B+Y')
for word in sorted( ((v,k) for k,v in allListsDict.iteritems()), reverse=True):
    print word 

print('\n')
print('Y+B')
for word in sorted( ((v,k) for k,v in dictYB.iteritems()), reverse=True):
    print word

print('\n')
print('Y+G')
for word in sorted( ((v,k) for k,v in dictYG.iteritems()), reverse=True):
    print word

print('\n')
print('G+B')
for word in sorted( ((v,k) for k,v in dictGB.iteritems()), reverse=True):
    print word

z = dict()
for i in googleDict.keys():
    z[i] = googleDict[i]
for i in yahooDict.keys():
    z[i] = yahooDict[i]
for i in bingDict.keys():
    z[i] = bingDict[i]
print('\n')
print('All Other Stuff')
for word in sorted( ((v,k) for k,v in z.iteritems()), reverse=True):
    print word
'''
print("yahoo")
print(yahooDict)
print('\n')
print("google")
print(googleDict)
print('\n')
print("bing")
print(bingDict)
print kope


'''