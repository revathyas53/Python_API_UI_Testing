import requests
import json
from payload import *
url='http://216.10.245.166/Library/Addbook.php'
header={'Content-Type': 'application/json;charset=UTF-8'}
addBook_response=requests.post(url, json=addPayload("r77"), headers=header)
res_addbook_json= addBook_response.json()
print(res_addbook_json)
book_id = res_addbook_json['ID']
print(book_id)
assert res_addbook_json['Msg'] == 'successfully added'
assert addBook_response.status_code==200
deleteBook_response=requests.post("http://216.10.245.166/Library/DeleteBook.php", json={'ID': book_id}, headers=header,)
print(deleteBook_response.json())
assert deleteBook_response.status_code==200