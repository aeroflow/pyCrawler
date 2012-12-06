import re


def extractData(regex, content):
    r = '0'
    p = re.compile(regex)
    m = p.search(content)
    if m:
        r = m.group(1)
        return r;


if __name__ == '__main__':
    regex = r'?aid=(\d+)&logid=\d*&p=com.boyaa.lordland.sina'
    content = "http:\/\/cn.papayamobile.com\/a\/games\/json_cg_c2ba_d?aid=65&logid=5140301&p=com.boyaa.lordland.sina"

 
   
    print(extractData(regex,content))
#    print(extractData(regex,content))
#    print(extractData(regex,content,index+2))
    