"""
A four-digit year as input and generate the balances file and 
transactions file for that year.
"""
import sys
import csv
import random,uuid
import argparse
from datetime import date, timedelta

""""
1. workdays(year) - it generate working days of particular year
   -The output of the function is a days[] list. The elements in the list is in YYYYMMDD format.
   -The function called by inside the transaction(year), balance(year) function

"""


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

"""
2. transaction(year) - it generate transaction.csv file
   - First it fetch the days[] list from workdays() function
   - create new_days[] list which include only 150 days from days[] list by using randomized selection.
   - create a transaction.csv file using open() function.
   - write the header from the list fieldnames = ['Date', 'currency', 'Amount', 'Description', 'Ref#']
   - open a while loop for limit 250 transaction  into transaction.csv file
   - write each raw in the dict format by randomized choosen values

"""
## transaction file generation
def transaction(year):

  days = workdays(year)
  new_days = []
  num = 150
  while  ( num !=0):
    new_days.append(random.choice(days))
    num -= 1

  
  with open('transaction.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'currency', 'Amount', 'Description', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    n = 250
    transaction_days=[]
    while (n != 0):
      transaction_days.append(random.choice(new_days))
      n -= 1
    for day in sorted(transaction_days):
      writer.writerow({'Date': day, 'currency': 'INR', 'Amount': round(random.uniform(-100,100),2), 'Description': 'wire out invoice ', 'Ref#':uuid.uuid4().hex[:8]})
      
## balance file generation
"""
2. balance(year) - it generate balance.csv file
   - First read the transaction.csv file for getting all the transactions 
   - write each row wise data into row[] list
   - create a new_sorted[] list from row[] which is a sorted list by the fieldname Date 
   - call the workday(year) function get the days[] list
   - create a balance.csv file using open() function
   - write the header from the list fieldnames = ['Date', 'Account', 'Opening', 'Closing', 'Ref#']
   - fetch each day in days[] list
   - write each raw in the dict format by randomized choosen values
   - calculating the opening and closing value by amount which fetch from new_sorted[] list
"""
def balance(year):
  new_sorted = []
  file = open("transaction.csv")
  csvreader = csv.reader(file)
  header = next(csvreader)
  rows = []
  for row in csvreader:
      rows.append(row)
  days = workdays(year)
  accounts = ['current','savings','salary','fixed deposite','NRI']
  
  with open('balance.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'Account', 'Opening', 'Closing', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    opening_amout=0
    closing_amount=0
    for day in days:
      total=0
      for row in rows:
        if day == row[0]:
          total = float(row[2]) +float(total)
      closing_amount = round(total+float(opening_amout),2)

      writer.writerow({'Date': day, 'Account': random.choice(accounts), 'Opening':opening_amout , 'Closing':closing_amount , 'Ref#': uuid.uuid4().hex[:8]})
      opening_amout = closing_amount



parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", type=int, help="Details of the specified year")
args = parser.parse_args()
transaction(args.year)
balance(args.year)
