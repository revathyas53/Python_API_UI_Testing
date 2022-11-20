import requests
import json
## **********To add the book***** ##

print(" ********* ADD BOOK ********* ")
url = 'http://216.10.245.166/Library/Addbook.php'
body = {
    "name": "BDD using Python",
    "isbn": "123",
    "aisle": "112",
    "author": "Revathy Anila Sreekumar"
}
header = {'Content-Type': 'application/json;charset=UTF-8'}
response = requests.post(url, json=body, headers=header)
json_response = response.json()
print(json_response)
book_id = json_response['ID']
print(book_id)
assert json_response['Msg'] == 'successfully added'

## **********To delete the book***** ##

print("****** DELETE BOOK ******")
response_deleteBook = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={'ID': book_id}, headers=header,)
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()
print(res_json)
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

