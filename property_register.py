from bs4 import BeautifulSoup
import requests
import ast
import re
import sqlite3


locations = ['Dun%20Laoghaire', 'Glenageary', 'Sallynoggin']

# retrieve for each location
def pull(): 
    for location in locations: 
        data = requests.get(url=f'https://www.propertypriceregister.ie/Website/npsra/PPR/npsra-ppr.nsf/PPR-By-Date&Start=1&Query=%5Bdt_execution_date%5D%3E=01/01/2021%20AND%20%5Bdt_execution_date%5D%3C01/01/2022%20AND%20%5Baddress%5D=*{location}*%20AND%20%5Bdc_county%5D=Dublin&County=Dublin&Year=2021&StartMonth=01&EndMonth=&Address={location}', verify=False)
        parse(data, location)

def parse(data, location):

    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup.prettify())
    soup = soup.find_all('script', type='text/javascript')[5]
    parsed = re.findall(r'\[.*,]', str(soup))[0]
    parsed = ast.literal_eval(parsed)

    print(parsed)

#     store_to_db(parsed, location)    

# def store_to_db(location):

#     con = sqlite3.connect('example.db')
#     # Create table
#     cur.execute('''CREATE TABLE stocks
#                 (date text, trans text, symbol text, qty real, price real)''')

#     # Insert a row of data
#     cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#     # Save (commit) the changes
#     con.commit()

#     # We can also close the connection if we are done with it.
#     # Just be sure any changes have been committed or they will be lost.
#     con.close()
    


# parse function

# check if db exists
# if not create new
# if so, obtain a list of everything updated
# update db


pull()