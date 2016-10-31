from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



def getHookersId():
	"""get Id of hooker's page"""

	url = "http:"
	html = urlopen(url)
	bsObj = BeautifulSoup(html, "lxml")
	girlsNum = list()
	
	IDs = bsObj.findAll("a")
	for girlsId in IDs:
		gUrl = girlsId.attrs['href']
		if "profile" in gUrl:
			girlsNum.append(gUrl)
	return girlsNum
		


def getHookerList():
 	"""get names and days of hookers"""

 	days = list() 
 	time = list()
 	NumList = list()
 	NumList = getHookersId()
 		
 	for num in NumList:
 		rawUrl = "http://"
 		url = rawUrl + str(num)
 		
 		
 		html = urlopen(url)
 		bsObj = BeautifulSoup(html, "lxml")

 		name = bsObj.find("div", {"style":"float:left;"}).get_text()
	 	days = bsObj.findAll("th", {"style":re.compile("(00)*$")})
	 	time = bsObj.find("div",{"id":"schedule"}).findAll("td")
	
	 	print(name)
	 	for day, a_time in zip(days, time):
	 		print(day.get_text(), a_time.get_text())
	 		


getHookerList()



