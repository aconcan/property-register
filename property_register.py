from bs4 import BeautifulSoup
import requests
import ast
import re
import sqlite3

locations = ['Dun Laoghaire', 'Glenageary', 'Sallynoggin'] 

# Retrieve housing data for each location
def pull(): 
    for location in locations: 
        data = requests.get(url=f'https://www.propertypriceregister.ie/Website/npsra/PPR/npsra-ppr.nsf/PPR-By-Date&Start=1&Query=%5Bdt_execution_date%5D%3E=01/01/2021%20AND%20%5Bdt_execution_date%5D%3C01/01/2022%20AND%20%5Baddress%5D=*{location}*%20AND%20%5Bdc_county%5D=Dublin&County=Dublin&Year=2021&StartMonth=01&EndMonth=&Address={location}', verify=False)
        parse(data, location)


def parse(data, location):
    soup = BeautifulSoup(data.text, 'html.parser')
    soup = soup.find_all('script', type='text/javascript')[5]
    
    parsed = re.findall(r'\[.*,]', str(soup))[0]
    parsed = ast.literal_eval(parsed)

    store_to_db(parsed, location)    


def store_to_db(parsed, location):
    new_sales = []

    # Parse spaces for table name creation
    location = location.replace(' ', '')
    
    # Set up connection 
    con = sqlite3.connect('locations.db')
    cur = con.cursor()
    
    # Create table if doesn't exist already
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {location} (
            date TEXT,
            price TEXT,
            link TEXT UNIQUE PRIMARY KEY)''')
    
    # Add new sales to array + update table
    for sale in parsed:
        sale[2] = sale[2].replace('"', '')
        sale[2] = sale[2].replace("'", '')
        
        if not cur.execute(f'SELECT * from {location} WHERE link LIKE "{sale[2]}"'): 
            new_sales.append(sale)
            cur.execute(f'INSERT INTO {location} VALUES ("{sale[0]}", "{sale[1]}", "{sale[2]}")')

    con.commit()
    con.close()


pull()


# Define Twilio function to send a text with housing sales updates to phone