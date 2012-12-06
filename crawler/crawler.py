#encoding='utf-8'
import httplib2
import re
from html.parser import HTMLParser

def extractInfo(pattern,url):
    print(url)
    charp = re.compile(r'charset=(.*?)$')
    try:
        response, content = httplib2.Http().request(url)
    except:
        print('download exception:' + response)
        return 0
    charm = charp.search(response['content-type'])
    if charm:
        decoder = charm.group(1)
    str_content = content.decode(decoder)
    results = pattern.findall(str_content)   
#    print(results)
    for rest in results:
        print(rest[0]+'\t'+rest[1]+rest[2]+'\t'+rest[3])

if __name__ == '__main__':
    
    url = 'http://www.dianping.com/search/category/2/0/p4'
    infop = re.compile(r'<li class="shopname">\s*<a.*?target="_blank">(.*?)</a>.*\s*<li class="address">.*?class="Black-H">(.*?)</a>(.*?)&nbsp;&nbsp;(\d*?\D*?\d*?)</li>')
    
    extractInfo(infop,url)       
    