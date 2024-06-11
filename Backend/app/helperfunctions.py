from app import db
from app.models import Categories, Resource
import requests
from bs4 import BeautifulSoup


##Creates vurerable catorgories
def create_categories():
    if Categories.query.count() > 0:
        return
    for category_name in [
        "Elderly",
        "Youth",
        "People with Disabilities",
        "Homeless",
        "Refugees and Asylum Seekers",
        "Veterans",
        "Recovering Addicts",
    ]:
        category = Categories(name=category_name)
        db.session.add(category)
    db.session.commit()


##Takes application address assigns logitude and latitude
def get_lat_long(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json"}
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

    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")

    if img_tags:
        first_img_src = img_tags[0].get("src")
        if not first_img_src.startswith("http"):
            first_img_src = url + first_img_src
        return first_img_src

    return None


def seedResources():
    if Resource.query.count() > 0:
        return
    resource1 = Resource(
        name="House of Charity",
        description="House of Charity is a non-profit organization that provides food, shelter, and support services to those in need.",
        address="32 W Pacific Ave, Spokane, WA 99201",
        phoneNumber="509-624-7821",
        email="Frontdesk@cceasternwa.org",
        website="https://www.houseofcharity.org/",
        category_id=4,
        lon=-117.4234,
        lat=47.6573,
        img="https://www.houseofcharity.org/wp-content/uploads/2019/06/HOC-Logo-Color.png",
    )
    db.session.add(resource1)
    reasource2 = Resource(
        name="Union Gospel Mission",
        description="Union Gospel Mission is a non-profit organization that provides food, shelter, and support services to those in need.",
        address="1224 E Trent Ave, Spokane, WA 99202",
        phoneNumber="509-535-8510",
        email="uniongospelmission@gmail.com",
        website="https://www.ugmspokane.org/",
        category_id=4,
        lon=-117.3987,
        lat=47.6639,
        img="https://www.ugmspokane.org/wp-content/uploads/2020/08/UGM-Logo-Color.png",
    )
    db.session.add(reasource2)
    reasource3 = Resource(name = "Spokane Resource Center", description = "Spokane Resource Center is a non-profit organization that provides food, shelter, and support services to those in need.", address = "130 S Arthur St, Spokane, WA 99202", phoneNumber = "509-456-7111", email = "", website = "https://www.spokaneresourcecenter.org/", category_id = 7, lon = -117.4133, lat = 47.6543, img = "https://www.spokaneresourcecenter.org/wp-content/uploads/2020/07/Spokane-Resource-Center-Logo-Color.png")
    db.session.add(reasource3)
    db.session.commit()
    return
