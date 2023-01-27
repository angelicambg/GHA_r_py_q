from bs4 import BeautifulSoup
import requests
import re
import json
from json import dumps
import pandas

# Load URL in beautiful soup
url = 'https://theathletic.com/2594478/2021/06/15/euro-2020-squads-teams-list/'

# Get the data
res = requests.get(url)

# Use beautiful soup to parse it
soup = BeautifulSoup(res.text, "html.parser")

# SelectorGadget to the rescue :-) 
# I extract the required content (I determined the selection criteria "p , h3" using the SelectorGadget)
plain_text = soup.select("p , h3")

# Extract the plain text (it turned out to work best for me)
text_football = soup.get_text()

 # write to file
with open('TextFootball.json', "w") as outfile:
    json.dump(text_football, outfile)
    
