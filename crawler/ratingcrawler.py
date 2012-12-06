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
#    print(str_content)  
    result = pattern.findall(str_content)   
#    print(results)
    if result:
        for ret in result:
            return ret
        

if __name__ == '__main__':
    
    url = 'https://play.google.com/store/apps/details?id='
    ratingp = re.compile(r'itemprop="ratingValue" content="(\d\.\d)"')
    
    f= open('games.txt','r')
    fw = open('gamerating.txt','a')
    lines = f.readlines()
    for l in lines:
        game = l.strip()   
        rating = extractInfo(ratingp,url+game)
        fw.writelines(game + '\t' + str(rating))
    f.close()
    fw.close()
    print("********************** END **************************")
        
    
               
    