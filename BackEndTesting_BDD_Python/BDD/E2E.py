#***********Api automation using request module*******#
#Get book to library api
import requests
import json
print(" ********* ADD BOOK ********* ")



url = 'http://216.10.245.166/Library/Addbook.php'
body = {
    "name": "BDD using Python",
    "isbn": "098",
    "aisle": "345",
    "author": "Revathy"
}
header = {'Content-Type': 'application/json;charset=UTF-8'}
add_response = requests.post(url, json=body, headers=header)
json_response = add_response.json()
print(json_response)
book_id = json_response['ID']
print(book_id)
assert json_response['Msg'] == 'successfully added'



print("********** GET Book **********")

response = requests.get('https://rahulshettyacademy.com/Library/GetBook.php?',params={'AuthorName':"Revathy"})
json_response_get=response.json()
print(json_response_get)
#isbn=json_response_get[0]['isbn']

assert response.status_code==200

print(f' headers is ', response.headers)
print(f'cookies is', response.cookies)
assert response.headers['Content-Type']== 'application/json;charset=UTF-8'

### Find the isbn==isbn ######
print("***** Find the isbn==RAS557 *****")

for actual_book in json_response_get: 
    #print(actual_book)
    if actual_book['isbn']=="RAS557":
        print(actual_book)
        break
  
expected_book= {'book_name': 'JavaScript', 'isbn': 'RAS557', 'aisle': '22'}
assert expected_book==actual_book


print("****** DELETE BOOK ******")

response_deleteBook = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={'ID': book_id}, headers=header,)
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
print(res_json)
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"