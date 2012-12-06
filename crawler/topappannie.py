#encoding='utf-8'
import httplib2
import re
from html.parser import HTMLParser

def extractCountries(pattern,url):
    charp = re.compile(r'charset=(.*?)$')
    try:
        resp, cont = httplib2.Http().request(url)
    except:
        print ('download exception:\t' + resp)
        return 0
    charm = charp.search(resp['content-type'])
    if charm:
        decoder = charm.group(1)
    str_cont = cont.decode(decoder)
    result= pattern.findall(str_cont)    
    return result
        
        



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
#    print(str_content)  
    result = pattern.findall(str_content)   
#    print(results)
    if result:
        for ret in result:
            return ret
        

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
        
    
               
    