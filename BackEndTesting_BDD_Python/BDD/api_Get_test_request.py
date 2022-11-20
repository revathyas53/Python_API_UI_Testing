#***********Api automation using request module*******#
#Get book to library api
import requests
import json

response = requests.get('https://rahulshettyacademy.com/Library/GetBook.php?',params={'AuthorName':'Rahul Shetty'})
'''
print(response.text)
print(type(response.text))
dict_response=json.loads(response.text)
print(dict_response)
print(type(dict_response))
print(dict_response[1]['isbn'])
'''

json_response=response.json()
print(json_response[1]['isbn'])

assert response.status_code==200

print(f' headers is ', response.headers)
print(f'cookies is', response.cookies)
assert response.headers['Content-Type']== 'application/json;charset=UTF-8'

### Find the isbn==RS241 ######
print("***** Find the isbn==RS241 *****")

for actual_book in json_response: 
    #print(actual_book)
    if (actual_book['isbn']=='RS241') & (actual_book['aisle']=='227435'):
        print(actual_book)
        break
  
expected_book= {'book_name': 'Learn Appium Automation with Java', 'isbn': 'RS241', 'aisle': '227435'}

assert expected_book==actual_book
    
