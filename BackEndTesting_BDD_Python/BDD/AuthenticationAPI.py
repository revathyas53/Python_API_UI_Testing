import requests
import json
from utilities.configuration import *
url= 'https://api.github.com'
authentication=('revathyas53', getPassword())
github_response=requests.get(url, auth=authentication)
print(github_response.status_code)
json_github_response = github_response.json()
print(json_github_response)

url2='https://api.github.com/users/repos'
github_response2=requests.get(url2, auth=authentication)
print(github_response2.status_code)
json_github_response2 = github_response2.json()
print(json_github_response2)


# Concept of session manager no need of authentication every time in request call if we authenticate using session manager
# for that se=requests.session() is used to create a session
print("******Using Session Manager*******")
se=requests.session()
se.auth=('revathyas53', getPassword())
response_usingsession=se.get(url2)
print(response_usingsession.status_code)
json_response_usingsession =response_usingsession.json()
print(json_response_usingsession)


##### concept of cookies
print("*********Cookies***********")
#'visit-month'
cookie = {'visit-month':'November'}
cookie_response=requests.get('http://rahulshettyacademy.com',allow_redirects=True, cookies=cookie, timeout=1)
print(cookie_response.status_code)
print(cookie_response.history)
cookie_response2=requests.get('https://httpbin.org/cookies',cookies={'visit-year': '2022'})
print(cookie_response2.json())
##########attachments
print("*******ATTACHMENTS**********")
image_file={'file':open('/Users/revathyanilasreekumar/Python_API_UI_Testing/image.jpg', 'rb')}
image_response=requests.post('https://petstore.swagger.io/v2/pet/12309876/uploadImage',files=image_file)
print(image_response.json())
print(image_response.status_code)
print(image_response.headers)