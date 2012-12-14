#encoding='utf-8'
import httplib2
import re
from html.parser import HTMLParser

def extractCountries(url,pattern1,pattern2):
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
    box= pattern1.search(str_cont)    
    if box :
        result = box.group(1)
#        print(result)
        cbox = pattern2.findall(result)
        return cbox       
        



def extractInfo(url,pattern):
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
 
    if result:
        for i in range(len(result)):
            result[i]=HTMLParser().unescape(result[i])
        return result    

def toText(file,rec,country,tag):
    fw=open(file,'ab')
    print('Writing Top %s.....' %tag)
    try:
        i=0
        for t in rec:
            i+=1
            l = str(i)+'\t'+t+'\t'+tag+'\t'+country+'\n'
            fw.write(l.encode(encoding='utf_8', errors='strict'))
    except (TypeError) as e:
        print(e)
    fw.close()        
        

if __name__ == '__main__':
    
    rurl = 'http://www.appannie.com/top/android/united-states/overall/'
    
    prefix = 'http://www.appannie.com/top/android/'
    
    boxp = re.compile(r'<div id="all-stores" class="select_box">\s*?<ul>([\s\S]*?)</ul>\s*?</div>')
    countryp = re.compile(r'<li><a href="/top/android/(.*?)/overall.*?>.*?</a></li>')
    top_paid_p = re.compile(r'<td class="top_paid app paid no_iap feed_5">[\s\S]*?class="app-name"><a.*?>(.*?)</a></span>')
    top_free_p = re.compile(r'<td class="top_free app free no_iap feed_5">[\s\S]*?class="app-name"><a.*?>(.*?)</a></span>')
    top_gross_p = re.compile(r'<td class="top_free app free no_iap feed_5">[\s\S]*?class="app-name"><a.*?>(.*?)</a></span>')
    top_new_paid_p = re.compile(r'<td class="top_new_paid app paid no_iap feed_5">[\s\S]*?class="app-name"><a.*?>(.*?)</a></span>')
    top_new_free_p = re.compile(r'<td class="top_new_free app free no_iap feed_5">[\s\S]*?class="app-name"><a.*?>(.*?)</a></span>')
    
    print('Extracting Countries.......') 
    countries = extractCountries(rurl,boxp,countryp)    
 

    for c in ['china']:
        url = prefix + c + '/overall'
        
        print('Index of Countries:\t%d/%d' %(countries.index(c)+1,len(countries)))
        print(url)
        
        print('Extracting Top Paid.....')
        top_paid=extractInfo(url,top_paid_p)
        print('Extracting Top Free.....')
        top_free=extractInfo(url,top_free_p)
        print('Extracting Top Gross.....')
        top_gross=extractInfo(url,top_gross_p)
        print('Extracting Top New Paid.....')
        top_new_paid=extractInfo(url,top_new_paid_p)
        print('Extracting Top New Free.....')
        top_new_free=extractInfo(url,top_new_free_p)
        
        fw= open('topapps.txt','ab')
        toText('topapps.txt',top_paid,c,'Paid')
        toText('topapps.txt',top_free,c,'Free')
        toText('topapps.txt',top_gross,c,'Gross')
        toText('topapps.txt',top_new_paid,c,'New Paid')
        toText('topapps.txt',top_new_free,c,'New Free')     
     
        
    print("********************** END **************************")
        
    
               
    