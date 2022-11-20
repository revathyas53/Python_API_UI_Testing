import json
Courses='{"Name": "Revathy","Languages": ["Python", "Java"]}'
'''
dict_Courses =json.loads(Courses)
print(type(dict_Courses))
print(dict_Courses)
print(dict_Courses["Languages"][0])
'''

########################################parse content present in a file########################
with open('/Users/revathyanilasreekumar/Projects/BackEndTesting_BDD_Python/BDD/sample.json', 'r') as f:
    file_dict=json.load(f)
    #print(file_dict)
    print(file_dict['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])
    print(type(file_dict['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm']))
    
with open('/Users/revathyanilasreekumar/Projects/BackEndTesting_BDD_Python/BDD/sample1.json','r') as f1:
    file_new=json.load(f1)
    print(file_new)
    print(file_new['employees'][0])
    print(type(file_new['employees'][0]))
    print(file_new['employees'][0]['lastName'])
    print(type(file_new['employees'][0]['lastName']))
    print("## need to find lastNAME OF 'Anna' ##")
    employees=file_new['employees']
    for employee in employees:
        if employee['firstName']=='Anna':
            print(employee['lastName'])
            assert employee['lastName']=='Smith'
### Compare 2 json Files ##
print('### Compare 2 json Files ##')
with open('/Users/revathyanilasreekumar/Projects/BackEndTesting_BDD_Python/BDD/sample.json') as f3:
    data1=json.load(f3)
with open('/Users/revathyanilasreekumar/Projects/BackEndTesting_BDD_Python/BDD/sample1.json') as f4:
    data2=json.load(f4)

print(data1==data2)
#assert data1==data2

with open('/Users/revathyanilasreekumar/Projects/BackEndTesting_BDD_Python/BDD/sample1copy.json') as f5:
    data3=json.load(f5)
print(data3==data2)
assert data3==data2




       


