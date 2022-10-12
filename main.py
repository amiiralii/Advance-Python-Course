import requests
from bs4 import BeautifulSoup as bs
import mariadb
import sys

# Connecting to Database
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="laptops"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print('Connected to db learn')
cur = conn.cursor()


# Creating table
"""
query = 'CREATE TABLE laptops (title VARCHAR(200), price VARCHAR(20), graphicsCard VARCHAR(50), processor VARCHAR(40), screen VARCHAR(70), ram VARCHAR(20), memmory VARCHAR (50))'
cur.execute(query)
print('Table Created Succesfully')
"""

"""
# Collecting laptop data from web-page
all_laptops=[]
for k in range(1,39):

    # Getting the web-page
    URL = "https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops?pageNumber="+str(k)
    r = requests.get(URL)
    soup = bs(r.content, 'html.parser')
    products = soup.find_all('div', attrs={'class':'OfferBox'})

    # Deriving data
    for current_laptop in products:
        laptop_info = {}
        # Find laptop price
        try:
            laptop_info['price'] = current_laptop.find('span',attrs={'class':'offerprice'}).text
        except:
            laptop_info['price'] = ""
        # Find laptop title
        try:
            laptop_info['title'] = current_laptop.find('a', attrs={'class': 'offerboxtitle'}).text
        except:
            laptop_info['title'] = ""

        info = current_laptop.find('div', attrs={'class':'productInfo'})
        derived_data = info.find_all('span')
        for i in range(len(derived_data)):
            derived_data[i] = derived_data[i].text

        # Find laptop Processor Model
        try:
            tmp = derived_data.index('Processor')
            laptop_info['Processor'] = derived_data[tmp - 1]
        except:
            laptop_info['Processor'] = ""

        # Find laptop Graphics card Model
        try:
            tmp = derived_data.index('Graphics card')
            laptop_info['Graphics-card'] = derived_data[tmp - 1]
        except:
            laptop_info['Graphics-card'] = ""

        # Find laptop Screen Model
        chk = 0
        for i in derived_data:
            a = i.find('Screen')
            if a!=-1:
                laptop_info['screen'] = i
                chk=1
        if chk == 0:
            laptop_info['screen'] = ''

        # Find laptop RAM capacity
        try:
            tmp = derived_data.index('RAM')
            laptop_info['ram'] = derived_data[tmp - 1]
        except:
            laptop_info['ram'] = ""

        # Find laptop Memmory
        try:
            tmp = derived_data.index('SSD')
            laptop_info['memmory'] = derived_data[tmp - 1]
        except:
            laptop_info['memmory'] = ""

        all_laptops.append(laptop_info)

        # Adding laptopt to database
        query = 'INSERT into laptops VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (laptop_info['title'], laptop_info['price'], laptop_info['Graphics-card'], laptop_info['Processor'], laptop_info['screen'], laptop_info['ram'], laptop_info['memmory'])
        cur.execute(query)

    print('Products derived from page number '+str(k)+'.')

print("Data from",len(all_laptops),"laptops collected.")

print("All laptop data Added Succesfully to database!")
conn.commit()
conn.close()

"""
