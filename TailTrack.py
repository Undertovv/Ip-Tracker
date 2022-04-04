from termcolor import colored
import requests

input(str("Target IP Address: "))

#Send a request to ipinfo.io to get target ip address
response = requests.get("https://ipinfo.io/" + targetIP + "/json")

#print output of requests in an easy-to-edit format. 
location = response.json()
print("I really respect your opinion,", colored("however\n", 'red'))
print(location['ip'])
print(location['country'])
print(location['region'])
print(location['city'])
print(location['loc'])
#print(location[])
