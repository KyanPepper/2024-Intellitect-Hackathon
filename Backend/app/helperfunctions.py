from app import db
from app.models import Categories, Resource, Application
import requests
from bs4 import BeautifulSoup
import random

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
    #todo add real images
    if Resource.query.count() > 0:
        return
    resource1 = Resource(
        name="House of Charity",
        description="House of Charity is a non-profit organization that provides food, shelter, and support services to those in need.",
        address="32 W Pacific Ave\nSpokane, WA 99201",
        phoneNumber="509-624-7821",
        email="Frontdesk@cceasternwa.org",
        website="https://www.houseofcharity.org/",
        tags="health,shelter,food",
        category_id=4,
        lon=-117.4234,
        lat=47.6573,
        img="https://bloximages.newyork1.vip.townnews.com/kxly.com/content/tncms/assets/v3/editorial/5/ce/5ced6f53-6e72-5869-9d67-4270a1b55f1d/63bc93acbea42.image.jpg?crop=1024%2C538%2C0%2C19&resize=1024%2C538&order=crop%2Cresize",
    )
    db.session.add(resource1)

    reasource2 = Resource(
        name="Union Gospel Mission",
        tags="health,shelter,people",
        description="Union Gospel Mission is a non-profit organization that provides food, shelter, and support services to those in need.",
        address="1224 E Trent Ave\nSpokane, WA 99202",
        phoneNumber="509-535-8510",
        email="uniongospelmission@gmail.com",
        website="https://www.ugmspokane.org/",
        category_id=4,
        lon=-117.3987,
        lat=47.6639,
        img="https://www.homelessshelterdirectory.org/gallery/941__zkl.jpg",
    )
    db.session.add(reasource2)

    reasource3 = Resource(name = "Spokane Resource Center",
                          description = "Spokane Resource Center is a non-profit organization that provides food, shelter, and support services to those in need.",
                          address = "130 S Arthur St\nSpokane, WA 99202",
                          phoneNumber = "509-456-7111",
                          email = "",
                          website = "https://www.spokaneresourcecenter.org/",
                          category_id = 7,
                          lon = -117.4133,
                          lat = 47.6543,
                          img = "https://www.spokaneresourcecenter.org/wp-content/uploads/2020/07/Spokane-Resource-Center-Logo-Color.png")
    db.session.add(reasource3)

    reasource4 = Resource(name = "Aging and Long Term Care of Eastern Washington",
                          description = "ALTCEW helps you find resources for elderly individuals seeking to make independent living more sustainable with information regarding caregivers, in-home care, care transitions, medication management, and more.\n\nThe Rock Pointe Office, in particular, offers most of the main services associated with this organization (unlike the Post Street Office).",
                          address = "316 W Boone Ave, Suite 260\nSpokane, WA 99201",
                          phoneNumber = "509-458-2509",
                          email = "",
                          website = "https://www.altcew.org/",
                          category_id = 1,
                          lon = -117.415830,
                          lat = 47.668770,
                          img = "https://unicoprop.com/wp-content/uploads/2018/01/RockPointe2_Exterior_2014_3511-1200x893.jpg"),
    db.session.add(reasource4)

    reasource5 = Resource(name = "Aging and Long Term Care of Eastern Washington",
                          description = "ALTCEW helps you find resources for elderly individuals seeking to make independent living more sustainable with information regarding caregivers, in-home care, care transitions, medication management, and more.\n\nThe Rock Pointe Office, in particular, offers most of the main services associated with this organization (unlike the Post Street Office).",
                          address = "1222 N. Post Street\nSpokane, WA 99201",
                          phoneNumber = "509-458-2509",
                          email = "",
                          website = "https://www.altcew.org/",
                          category_id = 1,
                          lon = -117.423170,
                          lat = 47.668980,
                          img = "https://www.altcew.org/wp-content/uploads/sites/24/2020/05/ALTCEW-building-exterior-Web-Page-scaled.jpg")
    db.session.add(reasource5)

    db.session.commit()
    return



def seed_applications():
    if Application.query.count() > 0:
        return

    categories = Categories.query.all()

    if not categories:
        for category_name in Categories.categories:
            category = Categories(name=category_name)
            db.session.add(category)
        db.session.commit()
        categories = Categories.query.all()

    vulnerable_organizations = [
        "Hope Haven Shelter",
        "Empowerment Center for the Disabled",
        "Healing Hearts Refugee Aid",
        "Veterans Support Network",
        "Recovery Road Addiction Center"
    ]

    descriptions = [
        "Providing shelter and support services for homeless individuals and families.",
        "Offering programs and resources to empower people with disabilities.",
        "Assisting refugees and asylum seekers with resettlement and integration.",
        "Providing counseling, job placement, and other support for veterans.",
        "Offering rehabilitation programs and counseling for recovering addicts."
    ]

    addresses = [
        "123 Hope Lane, Cityville, USA",
        "456 Empowerment Street, Townsville, USA",
        "789 Refugee Road, Settlement City, USA",
        "101 Veteran Avenue, Service Town, USA",
        "202 Recovery Road, Healing City, USA"
    ]

    phone_numbers = [
        "123-456-7890",
        "234-567-8901",
        "345-678-9012",
        "456-789-0123",
        "567-890-1234"
    ]

    emails = [
        "info@hopehaven.org",
        "info@empowermentcenter.org",
        "info@healinghearts.org",
        "info@veteranssupport.org",
        "info@recoveryroad.org"
    ]

    websites = [
        "http://www.hopehaven.org",
        "http://www.empowermentcenter.org",
        "http://www.healinghearts.org",
        "http://www.veteranssupport.org",
        "http://www.recoveryroad.org"
    ]

    # Seed 5 applications
    for _ in range(5):
        organization = random.choice(vulnerable_organizations)
        description = random.choice(descriptions)
        address = random.choice(addresses)
        phone_number = random.choice(phone_numbers)
        email = random.choice(emails)
        website = random.choice(websites)
        category = random.choice(categories)

        application = Application(organization=organization,
                                  description=description,
                                  address=address,
                                  phoneNumber=phone_number,
                                  email=email,
                                  website=website,
                                  category=category)
        db.session.add(application)

    db.session.commit()
    print("Applications seeded successfully.")
