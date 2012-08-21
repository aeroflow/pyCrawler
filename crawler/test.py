import httplib2
import re
from html.parser import HTMLParser

rootURL = 'http://www.dianping.com/search/category/2/0/p1'

urlPattern = re.compile(r'<a href="/shop/\d+"(.*)&nbsp;&nbsp;\d{8}</li>')

def getRestaurant(pattern,url):
    print(url)
#    print(filename)
    try:
        response, content = httplib2.Http().request(url)
    except:
        print('download exception:' + response)
        return 0
#    f = open(filename, 'w')
    
    results = pattern.findall(content)
    print(results)
'''    
Parse the Html and get the information about restaurant

   

    
def getURL(url):
    try:
        response, content = httplib2.Http().request(url)
    except:
        print('download exception:' + response)
        return 0
    urlPattern = ''  
    
''' 
if __name__ == '__main__':
    getRestaurant(urlPattern,rootURL)       
    