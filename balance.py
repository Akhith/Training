import sys
import csv
import random,uuid
from datetime import date, timedelta


##  workdays of particular year
def workdays(year):

  days = []
  sdate = date(int(year), 1, 2)   
  edate = date(int(year), 12, 30)   

  delta = edate - sdate       

  for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    if day.isoweekday() not in (6,7):
      days.append(day)

  return days


## transaction file generation
def transaction(year):

  days = workdays(year)

  with open('transaction.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'currency', 'Amount', 'Description', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n=250
    writer.writeheader()
    while (n != 0):
      # date = random.choice(days)
      # str1 = str(date)
      # new_date = str1.replace('-','')
      writer.writerow({'Date': str(random.choice(days)).replace('-',''), 'currency': 'INR', 'Amount': round(random.uniform(-100,100),2), 'Description': 'wire out invoice ', 'Ref#':uuid.uuid4().hex[:8]})
      n-=1

## balance file generation
def balance(year):

  days = workdays(year)
  accounts = ['current','savings','salary','fixed deposite','NRI']
  
  with open('balance.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'Account', 'Opening', 'Closing', 'Ref#']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    n=150
    writer.writeheader()
    while (n != 0):

      writer.writerow({'Date': str(random.choice(days)).replace('-',''), 'Account': random.choice(accounts), 'Opening': round(random.uniform(0,1000)), 'Closing': round(random.uniform(0,2000),2), 'Ref#': uuid.uuid4().hex[:8]})
      n-=1

def main():
  if len(sys.argv) != 2:
    print ('usage: year as command line')
    sys.exit(1)

  year = sys.argv[1]
  transaction(year)
  balance(year)

if __name__ == '__main__':
  main()