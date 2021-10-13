
import sys
import csv
import random,uuid
from datetime import date, timedelta
import argparse



##  workdays of particular year
def workdays(year):

  days = []
  sdate = date(int(year), 1, 2)   
  edate = date(int(year), 12, 30)   

  delta = edate - sdate       

  for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    if day.isoweekday() not in (6,7):
      new = str(day).replace('-','')
      days.append(new)

  return days


## transaction file generation
def transaction(year):

  days = workdays(year)
  new_days = []
  num = 150
  while  ( num !=0):
    new_days.append(random.choice(days))
    num -= 1

  print(len(new_days))

  with open('transaction.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'currency', 'Amount', 'Description', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n=250
    writer.writeheader()
    while (n != 0):
      # date = random.choice(days)
      # str1 = str(date)
      # new_date = str1.replace('-','')
      writer.writerow({'Date': random.choice(new_days), 'currency': 'INR', 'Amount': round(random.uniform(-100,100),2), 'Description': 'wire out invoice ', 'Ref#':uuid.uuid4().hex[:8]})
      n-=1
      
## balance file generation
def balance(year):
  new_sorted = []
  file = open("transaction.csv")
  csvreader = csv.reader(file)
  header = next(csvreader)
  rows = []
  for row in csvreader:
      rows.append(row)
  new_sorted=sorted(rows,key=lambda x:x[0])

  days = workdays(year)
  accounts = ['current','savings','salary','fixed deposite','NRI']
  
  with open('balance.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'Account', 'Opening', 'Closing', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n=len(days)
    writer.writeheader()
    opening_amout=0
    closing_amount=0
    for i in days:
      for j in new_sorted:
        
        if i in j[0]:
          closing_amount = round(float(opening_amout)+float(j[2]),2)
      writer.writerow({'Date': i, 'Account': random.choice(accounts), 'Opening':opening_amout , 'Closing':closing_amount , 'Ref#': uuid.uuid4().hex[:8]})
      opening_amout = closing_amount

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", type=int, help="Details of the specified year")
args = parser.parse_args()
transaction(args.year)
balance(args.year)
