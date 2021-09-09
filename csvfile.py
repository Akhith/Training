import requests
import csv
import json
import urllib.request
url='https://reqres.in/api/users?per_page=30'
r = requests.get('https://reqres.in/api/users?per_page=30')
content=r.json()
word_data=content.get('data')
header=list(word_data[0].keys())
with open('people.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=header,

                       )
    fc.writeheader()
    fc.writerows(word_data)