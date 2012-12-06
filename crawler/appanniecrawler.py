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
    print(response.status)
    charm = charp.search(response['content-type'])
    if charm:
        decoder = charm.group(1)
        print(decoder)
    str_content = content.decode(decoder)
#    print(str_content)  
    result = pattern.search(str_content)
    if result:
        rv = result.group(1)
        return rv
    
'''    result = pattern.findall(str_content)   
    print(result)
    if result:
        return result[0]
'''        

if __name__ == '__main__':
    
    url = 'http://www.appannie.com/app/android/'
    ratingp = re.compile(r'itemprop="ratingValue" content="(\d\.\d)"')
    
    f= open('games.txt','r')
    fw = open('gamerating.txt','a')
    lines = f.readlines()
    for l in lines:
        game = l.strip()   
        rating = extractInfo(ratingp,url+game)
        fw.writelines(game + '\t' + str(rating) + '\n')
        print(game + '\t' + str(rating))
    f.close()
    fw.close()
    print("********************** END **************************")
        
    
               
    