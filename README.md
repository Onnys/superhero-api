# SuperHeros API
An Api that has endpoints that returns a superheroes list paginated in 10 heros
## Getting Started 

### Installing Dependencies

#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

From within the  directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```
# End-points
* This API is deployed at 
- https://superherosapi.herokuapp.com/add-superhero
- https://superherosapi.herokuapp.com/superheros?page=1
- https://superherosapi.herokuapp.com/dc-comics

## POST 'https://superherosapi.herokuapp.com/add-superhero'
- Create a new Superhero.
- Resquet Arguments: name, slug, intelligence, strength, speed, durability, power, combat, gender, race, height, weight, eyeColor, hairColor, fullName, alterEgos, aliases, placeOfBirth, firstAppearance, publisher, alignment, occupation, base, groupAffiliation, relatives, xs, sm, md, lg.
- Returns:  success and a superhero id.
```bash
 {
    "id": 1,
    "name": "A-Bomb",
    "slug": "1-a-bomb",
    "powerstats": {
      "intelligence": 38,
      "strength": 100,
      "speed": 17,
      "durability": 80,
      "power": 24,
      "combat": 64
    },
    "appearance": {
      "gender": "Male",
      "race": "Human",
      "height": [
        "6'8",
        "203 cm"
      ],
      "weight": [
        "980 lb",
        "441 kg"
      ],
      "eyeColor": "Yellow",
      "hairColor": "No Hair"
    },
    "biography": {
      "fullName": "Richard Milhouse Jones",
      "alterEgos": "No alter egos found.",
      "aliases": [
        "Rick Jones"
      ],
      "placeOfBirth": "Scarsdale, Arizona",
      "firstAppearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
      "publisher": "Marvel Comics",
      "alignment": "good"
    },
    "work": {
      "occupation": "Musician, adventurer, author; formerly talk show host",
      "base": "-"
    },
    "connections": {
      "groupAffiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
      "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
    },
    "images": {
      "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/1-a-bomb.jpg",
      "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/1-a-bomb.jpg",
      "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/1-a-bomb.jpg",
      "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/1-a-bomb.jpg"
    }
  }
  
```

## GET 'https://superherosapi.herokuapp.com/superheros?page=1'
- Fetches  a dictionary of 10 superheros
- Request Arguments: page
- Returns: a success value and a list of 10 superheros 

```bash
{
    "success": true,
    "superhero": [
        {
            "appearance": {
                "eyeColor": "Yellow",
                "gender": "Male",
                "hairColor": "No Hair",
                "height": [
                    "6'8",
                    "203 cm"
                ],
                "race": "Human",
                "weight": [
                    "980 lb",
                    "441 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Rick Jones"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
                "fullName": "Richard Milhouse Jones",
                "placeOfBirth": "Scarsdale, Arizona",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
                "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
            },
            "id": 1,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/1-a-bomb.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/1-a-bomb.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/1-a-bomb.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/1-a-bomb.jpg"
            },
            "name": "A-Bomb",
            "powerstats": {
                "combat": 64,
                "durability": 80,
                "intelligence": 38,
                "power": 24,
                "speed": 17,
                "strength": 100
            },
            "slug": "1-a-bomb",
            "work": {
                "base": "-",
                "occupation": "Musician, adventurer, author; formerly talk show host"
            }
        },
        {
            "appearance": {
                "eyeColor": "Yellow",
                "gender": "Male",
                "hairColor": "No Hair",
                "height": [
                    "6'8",
                    "203 cm"
                ],
                "race": "Human",
                "weight": [
                    "980 lb",
                    "441 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Rick Jones"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
                "fullName": "Richard Milhouse Jones",
                "placeOfBirth": "Scarsdale, Arizona",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
                "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
            }
```
## GET 'https://superherosapi.herokuapp.com/dc-characters?page=1'
- Fetches  a dictionary of 10 superheros from DC Comics
- Request Arguments: page
- Returns: a success value and a list of 10 superheros from DC Comics

```bash
{
    "success": true,
    "superhero": [
        {
            "appearance": {
                "eyeColor": "Yellow",
                "gender": "Male",
                "hairColor": "No Hair",
                "height": [
                    "200",
                    "61.0 meters"
                ],
                "race": "God / Eternal",
                "weight": [
                    "- lb",
                    "0 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Monitor",
                    "Mobius"
                ],
                "alignment": "bad",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Crisis on Infinite Earths #4",
                "fullName": "",
                "placeOfBirth": "Moon of Qward",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Sinestro Corps, Weaponers of Qward, Thunderers of Qward, Shadow Demons",
                "relatives": "Monitor (\"brother\"), The Monitors"
            },
            "id": 26,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/32-anti-monitor.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/32-anti-monitor.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/32-anti-monitor.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/32-anti-monitor.jpg"
            },
            "name": "Anti-Monitor",
            "powerstats": {
                "combat": 90,
                "durability": 100,
                "intelligence": 88,
                "power": 100,
                "speed": 50,
                "strength": 100
            },
            "slug": "32-anti-monitor",
            "work": {
                "base": "Qward, Antimatter Universe",
                "occupation": "-"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Male",
                "hairColor": "Blond",
                "height": [
                    "-",
                    "0 cm"
                ],
                "race": null,
                "weight": [
                    "- lb",
                    "0 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "-"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Aquaman #23 (October, 1965)",
                "fullName": "Arthur Curry, Jr.",
                "placeOfBirth": "-",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Aquaman Family",
                "relatives": "Aquaman (Orin/Arthur Curry) (father); Mera (mother); Koryak (half-brother); A.J. (half-brother); Atlan (grandfather); Tom Curry (adoptive grandfather, deceased); Orm Marius (uncle); Kordax (ancestor, deceased); Arthur Joseph Curry (adoptive cousin)"
            },
            "id": 29,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/36-aquababy.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/36-aquababy.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/36-aquababy.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/36-aquababy.jpg"
            },
            "name": "Aquababy",
            "powerstats": {
                "combat": 14,
                "durability": 14,
                "intelligence": 10,
                "power": 37,
                "speed": 12,
                "strength": 16
            },
            "slug": "36-aquababy",
            "work": {
                "base": "Atlantis",
                "occupation": "-"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Male",
                "hairColor": "Black",
                "height": [
                    "5'10",
                    "178 cm"
                ],
                "race": "Atlantean",
                "weight": [
                    "235 lb",
                    "106 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "-"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Adventure Comics #269 (February, 1960)",
                "fullName": "Garth",
                "placeOfBirth": "Poseidonis, Atlantis",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Aquaman Family; formerly Black Lantern Corps, Sentinels of Magic, Teen Titans",
                "relatives": "Cerdian (son), Dolphin (wife), Berra (mother), Thar (father), Slizzath (uncle) Donna (grand-daughter)"
            },
            "id": 30,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/37-aqualad.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/37-aqualad.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/37-aqualad.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/37-aqualad.jpg"
            },
            "name": "Aqualad",
            "powerstats": {
                "combat": 60,
                "durability": 75,
                "intelligence": 63,
                "power": 89,
                "speed": 42,
                "strength": 44
            },
            "slug": "37-aqualad",
            "work": {
                "base": "Atlantis",
                "occupation": "Adventurer; Magician, former Sidekick"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Male",
                "hairColor": "Blond",
                "height": [
                    "6'1",
                    "185 cm"
                ],
                "race": "Atlantean",
                "weight": [
                    "325 lb",
                    "146 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Dweller in the Depths",
                    "Swimmer",
                    "Waterbearer",
                    "Mental Man",
                    "Aquaboy",
                    "Water Wraith"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "More Fun Comics #73 (November, 1941)",
                "fullName": "Orin",
                "placeOfBirth": "Atlantis",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Justice League, Aquaman Family, Atlantean Royal Family; formerly Black Lantern Corps, Justice League International, Justice League Detroit, U.N.",
                "relatives": "Koryak (son), Arthur Curry, Jr. (son), A.J. (son), Orm Marius (half-brother), Debbie Perkins (half-sister), Drin (adopted brother), Atlanna (mother), Atlan (father), Atlena (aunt), Porm (adopted mother), Tom Curry (adopted father), Mera (wife), Hila (sister-in-law), Haumond (uncle), Kraken (uncle), Honsu (grandfather), Lorelei (grandmother), Manu (ancestor), Nala (ancestor), Fatima (ancestor), Kalunga (ancestor), Gana (ancestor), Fiona (ancestor), Regin (ancestor), Kordax (ancestor), Bazil (ancestor), Cora (ancestor), Illya (ancestor), Dardanus (ancestor), Alloroc (ancestor), Cole (ancestor), Narmea (ancestor), Orin (ancestor), Loma (ancestor), Shalako (ancestor), Thorvall (ancestor)"
            },
            "id": 31,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/38-aquaman.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/38-aquaman.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/38-aquaman.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/38-aquaman.jpg"
            },
            "name": "Aquaman",
            "powerstats": {
                "combat": 80,
                "durability": 80,
                "intelligence": 81,
                "power": 100,
                "speed": 79,
                "strength": 85
            },
            "slug": "38-aquaman",
            "work": {
                "base": "Atlantean Royal Palace; Poseidonis, Atlantis",
                "occupation": "Protector of the Seas and Oceans, King of Poseidonis"
            }
        }
    ]
}
```