from app import db
from app.models import Categories
import requests
from bs4 import BeautifulSoup
##Creates vurerable catorgories
def create_categories():
    if Categories.query.count() > 0:
        return
    for category_name in [
        'Elderly',
        'Youth',
        'People with Disabilities',
        'Homeless',
        'Refugees and Asylum Seekers',
        'Veterans',
        'Recovering Addicts'
    ]:
        category = Categories(name=category_name)
        db.session.add(category)
    db.session.commit()


##Takes application address assigns logitude and latitude
def get_lat_long(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
            return None, None
    data = response.json()
    if len(data) > 0:
        return float(data[0].get("lat", 0)), float(data[0].get("lon", 0))

def scrape_img_from_provided_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')

    if img_tags:
        first_img_src = img_tags[0].get('src')
        if not first_img_src.startswith('http'):
            first_img_src = url + first_img_src
        return first_img_src

    return None