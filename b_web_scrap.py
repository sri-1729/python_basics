import requests
from bs4 import BeautifulSoup
url = "https://www.codechef.com/users/"
url = url + input("Enter UserName: ")
page = requests.get(url)
obj = BeautifulSoup(page.content, "html.parser")
if(obj.find("h2") == None):
	print("User Not Found")
	exit();
print("Name: ",obj.find("h2").text)
print("Rating: ",obj.find("div", class_="rating-number").text)
if(obj.find("label",text="Institution:") == None):
	print("No Instituition Mentioned")
else:
	print("Instituition: ",obj.find("label",text="Institution:").next_sibling.text)
if(obj.find("label",text="Motto:") != None):
	print("Motto: ",obj.find("label", text="Motto:").next_sibling.text)





#for i in a:
#	print(i.get('href'))

