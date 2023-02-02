import requests

#Last Completed Build
lastCompletedBuild = "http://192.168.88.111:8080/job/Test_Selenium_Daily/lastCompletedBuild/api/json?pretty=true&tree=displayName,number,result"

r = requests.get(url = lastCompletedBuild)

data = r.json()
lastBuildName = data['displayName']
lastBuildNumber = data['number']
lastBuildResult = data['result']

buildNumber_1 = lastBuildNumber-1
buildNumber_2 = lastBuildNumber-2

lastBuildlink = "http://192.168.88.111:8080/job/Test_Selenium_Daily/" + str(lastBuildNumber)

print("Test - " + lastBuildName)
if lastBuildResult != "SUCCESS":
    print('\033[91m' + lastBuildResult + '\033[0m' + " - " + lastBuildlink)
else:
    print('\033[92m' + lastBuildResult + '\033[0m' + " - " + lastBuildlink)