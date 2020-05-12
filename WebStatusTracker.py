'''Program: Website Status Tracker
    Author: DataDaemonMau
    Purpose: Allows the user to check a site(s) status, whether they are
    online, offline..etc.
'''
# modules to import here
import sys
import requests

#def main():

    # Inputs Workflow
print("Welcome to your Web Status Tracker tool..")
    # Py queries the user for a url
url = input('Enter your name: ')
try:
    r = requests.head(url)
    print(r.status_code)
except requests.ConnectionError:
    print("failed to connect")
    # user enters a site url

    # Processing Workflow
    #print(urllib.request.urlopen(url).getcode())
    # Py takes url & searches web for url
    # obtains site status code

    # Outputs Workflow
    # Py outputs the status code to the user
    #sys.exit()
#main()
