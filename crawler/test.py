import httplib2
import re
from html.parser import HTMLParser

rootURL = 'http://www.dianping.com/search/category/2/0'

urlPattern = re.compile(r'<a href="/shop/\d+"(.*)&nbsp;&nbsp;\d{8}</li>')

def getRestaurant(url,filename):
    print(url)
    print(filename)
    try:
        response, content = httplib2.Http().request(url)
    except:
        print('download exception:' + response)
        return 0
    f = open(filename, 'w')
'''    
Parse the Html and get the information about restaurant

   
'''
    
def getURL(url):
    try:
        response, content = httplib2.Http().request(url)
    except:
        print('download exception:' + response)
        return 0
    urlPattern = ''  
    
    
    