from bs4 import BeautifulSoup
import urllib.request
import bs4 as bs
import re
shopifyurl = ''#enter shopify sitelist url
req = urllib.request.urlopen(shopifyurl).read()
soup = bs.BeautifulSoup(req, 'lxml')
rawdata = re.findall(r'<loc>(.*?)</loc>', str(soup))
for Product_list in rawdata:
	print(Product_list)



 





