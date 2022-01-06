"""
A four-digit year as input and generate the balances file and 
transactions file for that year.
"""
import sys
import csv
import random,uuid
import argparse
from datetime import date, datetime, timedelta


def workdays(year):
  """"
   - for given year it generate all the workdays
   - input : year 
   - output : days[] list only include the weekday
  """
  days = []
  sdate = date(int(year), 1, 2)           # Not include jan 1st, Dec 31st
  edate = date(int(year), 12, 30)   

  delta = edate - sdate       

  for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    if day.isoweekday() not in (6,7):     # Not include the saturday,sunday in day[]
      new = str(day).replace('-','')      #  Day are in YYYYMMDD format
      days.append(new)

  return days


def newtransaction(days):
    """"
   - for given day[] list it randomly choose 150 days
   - input : days[] list - weekdays of year
   - output : new_list [] - 150 days from day[] list ,there is more than one transaction on atleast 30 week days
    """
    new_list = random.choices(days, k=150)
    new_list = sorted(new_list)
    day=1
    start = datetime.strptime(new_list[0], "%Y%m%d")
    while ( day < len(new_list)):
        end =   datetime.strptime(new_list[day], "%Y%m%d")
        diff = end-start        
        if diff.days >= 30:
             newtransaction(days)
        else: 
            start = end   
        day += 1
          
    return new_list
       
 

def transaction(year):
  """
   - For a particular year it generate transaction.csv file
   - input : year
   - output : generate transaction.csv file, Fieldname : "Date,Currency,Amount,Description,Ref #"

  """
  days = workdays(year)
  
  new_days = newtransaction(days)
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
      

def balance(year):
  
  """
   - for a particular year it generate balance.csv file
   - input : year
   - output : generate balance.csv file, Fieldname : "Date,Account,Opening,Closing,Ref #"

  """
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
