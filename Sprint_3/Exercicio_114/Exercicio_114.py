import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://csfloat.com/')
    
except:
    print('Site fora do ar')
    
else:
    print('O site esta no ar')