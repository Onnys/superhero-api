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
## GET 'https://superherosapi.herokuapp.com/dc-comics?page=1'
- Fetches  a dictionary of 10 superheros from Marvel Comics
- Request Arguments: page
- Returns: a success value and a list of 10 superheros from Marvel Comics

```bash
{
    "success": true,
    "superhero": [
        {
            "appearance": {
                "eyeColor": "Green",
                "gender": "Male",
                "hairColor": "No Hair",
                "height": [
                    "5'11",
                    "180 cm"
                ],
                "race": null,
                "weight": [
                    "200 lb",
                    "90 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "The Living Death That Walks",
                    "Lord of the Negative Zone"
                ],
                "alignment": "bad",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Fantastic Four Annual #6 (1968)",
                "fullName": "Annihilus",
                "placeOfBirth": "Planet of Arthros, Sector 17A, Negative Zone",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Sometime ally of Blastaar",
                "relatives": "Annihilus is a series of clonal scions"
            },
            "id": 23,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/29-annihilus.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/29-annihilus.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/29-annihilus.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/29-annihilus.jpg"
            },
            "name": "Annihilus",
            "powerstats": {
                "combat": 64,
                "durability": 56,
                "intelligence": 75,
                "power": 59,
                "speed": 47,
                "strength": 80
            },
            "slug": "29-annihilus",
            "work": {
                "base": "-",
                "occupation": "Conqueror, scavenger"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Male",
                "hairColor": "Blond",
                "height": [
                    "6'0",
                    "183 cm"
                ],
                "race": "Human",
                "weight": [
                    "190 lb",
                    "86 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Myrmidon",
                    "Scott Edward Harris Lang"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Avengers Vol 1 #181 (March, 1979)",
                "fullName": "Scott Lang",
                "placeOfBirth": "Coral Gables, Florida",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Ant-Man Security Solutions; formerly Future Foundation (leader), Fantastic Four (leader), Defenders, Avengers, Heroes For Hire, Stark Industries",
                "relatives": "Cassandra Eleanor Lang (daughter), Ruth (sister), Carl (brother-in-law), Peggy Rae (ex-wife)"
            },
            "id": 25,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/31-ant-man-ii.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/31-ant-man-ii.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/31-ant-man-ii.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/31-ant-man-ii.jpg"
            },
            "name": "Ant-Man II",
            "powerstats": {
                "combat": 30,
                "durability": 40,
                "intelligence": 75,
                "power": 53,
                "speed": 17,
                "strength": 18
            },
            "slug": "31-ant-man-ii",
            "work": {
                "base": "South Beach, Miami, Florida; formerly Farmingdale, Long Island, New York",
                "occupation": "Electronics Technician,"
            }
        },
        {
            "appearance": {
                "eyeColor": "Red",
                "gender": "Male",
                "hairColor": "Black",
                "height": [
                    "7'0",
                    "213 cm"
                ],
                "race": "Mutant",
                "weight": [
                    "300 lb",
                    "135 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "The Eternal One",
                    "the High Lord",
                    "Set",
                    "Huitxilopochti",
                    "Sauru",
                    "Kali-Ma"
                ],
                "alignment": "bad",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "X-Factor #5 (June, 1986)",
                "fullName": "En Sabah Nur",
                "placeOfBirth": "Akkaba, Egypt",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Clan Akkaba, employer of Apocalypse's Horsemen, Dark Riders, former employer of the Alliance of Evil, 198",
                "relatives": "Baal of the Crimson Sands (adopted father, deceased)"
            },
            "id": 28,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/35-apocalypse.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/35-apocalypse.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/35-apocalypse.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/35-apocalypse.jpg"
            },
            "name": "Apocalypse",
            "powerstats": {
                "combat": 60,
                "durability": 100,
                "intelligence": 100,
                "power": 100,
                "speed": 33,
                "strength": 100
            },
            "slug": "35-apocalypse",
            "work": {
                "base": "Celestial Ship, mobile",
                "occupation": "Student; formerly Conqueror; Scientist"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Female",
                "hairColor": "Blond",
                "height": [
                    "5'9",
                    "175 cm"
                ],
                "race": "Human",
                "weight": [
                    "140 lb",
                    "63 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Spider-Woman",
                    "Madame Web"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Marvel Super Heroes Secret Wars #6",
                "fullName": "Julia Carpenter",
                "placeOfBirth": "Los Angeles, California",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Omega Flight, formerly Commission on Superhuman Activities , Freedom Force , Avengers , Secret Defenders , Force Works , Queen?s Vengeance , West Coast Avengers, Secret Avengers (Civil War)",
                "relatives": "Rachel Carpenter (daughter), Walter Cornwall (father), Elizabeth Cornwall (mother), Larry Carpenter (ex-husband, deceased)"
            },
            "id": 32,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/39-arachne.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/39-arachne.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/39-arachne.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/39-arachne.jpg"
            },
            "name": "Arachne",
            "powerstats": {
                "combat": 70,
                "durability": 70,
                "intelligence": 50,
                "power": 71,
                "speed": 50,
                "strength": 48
            },
            "slug": "39-arachne",
            "work": {
                "base": "Mobile; formerly Denver, Colorado; formerly Avengers Compound, Los Angeles, California",
                "occupation": "Adventurer, fugitive, former government agent"
            }
        },
        {
            "appearance": {
                "eyeColor": "White",
                "gender": "Female",
                "hairColor": "Orange",
                "height": [
                    "6'4",
                    "193 cm"
                ],
                "race": "Alien",
                "weight": [
                    "218 lb",
                    "98 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "-"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "The Order #4",
                "fullName": "Ardina",
                "placeOfBirth": "-",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "-",
                "relatives": "Norrin Radd (Silver Surfer, clonal source), Clea (creator)"
            },
            "id": 35,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/42-ardina.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/42-ardina.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/42-ardina.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/42-ardina.jpg"
            },
            "name": "Ardina",
            "powerstats": {
                "combat": 25,
                "durability": 80,
                "intelligence": 63,
                "power": 100,
                "speed": 100,
                "strength": 100
            },
            "slug": "42-ardina",
            "work": {
                "base": "-",
                "occupation": "-"
            }
        },
        {
            "appearance": {
                "eyeColor": "Brown",
                "gender": "Male",
                "hairColor": "Brown",
                "height": [
                    "6'1",
                    "185 cm"
                ],
                "race": null,
                "weight": [
                    "600 lb",
                    "270 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "God of War",
                    "Mister Talon",
                    "Mars",
                    "Warhawk"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Thor #129",
                "fullName": "",
                "placeOfBirth": "-",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Avengers, Mighty Avengers, Olympic Pantheon; Warhawks",
                "relatives": "Zeus (father), Hera (mother), Enyo (wife), Deimos, Phobos, Alexander (sons), Neptune, Pluto (uncles), Demeter, Hestia (aunts), Hephaestus (brother), Apollo, Dionysus, Hercules, Hermes(half-brothers), Artemis, Pallas Athena, Venus, (half-sisters)"
            },
            "id": 36,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/43-ares.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/43-ares.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/43-ares.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/43-ares.jpg"
            },
            "name": "Ares",
            "powerstats": {
                "combat": 101,
                "durability": 80,
                "intelligence": 75,
                "power": 84,
                "speed": 35,
                "strength": 82
            },
            "slug": "43-ares",
            "work": {
                "base": "Avengers Tower, formerly Olympus",
                "occupation": "-"
            }
        },
        {
            "appearance": {
                "eyeColor": "Purple",
                "gender": "Female",
                "hairColor": "Pink",
                "height": [
                    "5'5",
                    "165 cm"
                ],
                "race": null,
                "weight": [
                    "130 lb",
                    "59 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "-"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Fallen Angels #1 (1987)",
                "fullName": "Ariel",
                "placeOfBirth": "-",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "X-Men, Formerly Fallen Angels",
                "relatives": "-"
            },
            "id": 37,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/44-ariel.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/44-ariel.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/44-ariel.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/44-ariel.jpg"
            },
            "name": "Ariel",
            "powerstats": {
                "combat": 28,
                "durability": 14,
                "intelligence": 50,
                "power": 94,
                "speed": 12,
                "strength": 10
            },
            "slug": "44-ariel",
            "work": {
                "base": "-",
                "occupation": "Leader, refugee alien; former alien mutant-hunter and hedonist"
            }
        },
        {
            "appearance": {
                "eyeColor": "Black",
                "gender": "Female",
                "hairColor": "Black",
                "height": [
                    "5'4",
                    "163 cm"
                ],
                "race": null,
                "weight": [
                    "112 lb",
                    "50 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "X-Girl",
                    "Kid"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Astonishing X-Men #4 (2004)",
                "fullName": "Hisako Ichiki",
                "placeOfBirth": "-",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "X-Men, formerly: Xavier Institute Student Body, New X-Men",
                "relatives": "-"
            },
            "id": 38,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/45-armor.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/45-armor.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/45-armor.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/45-armor.jpg"
            },
            "name": "Armor",
            "powerstats": {
                "combat": 54,
                "durability": 80,
                "intelligence": 50,
                "power": 55,
                "speed": 12,
                "strength": 63
            },
            "slug": "45-armor",
            "work": {
                "base": "-",
                "occupation": "Adventurer, student"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Female",
                "hairColor": "Black",
                "height": [
                    "5'11",
                    "180 cm"
                ],
                "race": "Mutant",
                "weight": [
                    "140 lb",
                    "63 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Sister Beaubier"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "X-Men #121 (1979)",
                "fullName": "Jeanne-Marie Beaubier",
                "placeOfBirth": "Montreal, Quebec, Canada",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "Alpha Flight, Alpha Flight (Space Program), Royal Canadian Mounted Police; formerly Weapon X, ally of the Havok's Brotherhood, Headbangers , Children of the Vault, X-Men (interim member)",
                "relatives": "Jean-Baptiste Beaubier (father, deceased), unidentified mother (deceased), Jean-Paul Beaubier (Northstar, twin brother) Joanna Beaubier (adopted niece, deceased); Lois and Genevieve Martin (first cousins once removed/adopted parents, deceased)"
            },
            "id": 43,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/56-aurora.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/56-aurora.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/56-aurora.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/56-aurora.jpg"
            },
            "name": "Aurora",
            "powerstats": {
                "combat": 56,
                "durability": 60,
                "intelligence": 63,
                "power": 74,
                "speed": 96,
                "strength": 10
            },
            "slug": "56-aurora",
            "work": {
                "base": "Laval, Quebec, Canada",
                "occupation": "Adventurer; former terrorist, nun, history/geography teacher"
            }
        },
        {
            "appearance": {
                "eyeColor": "Yellow",
                "gender": "Male",
                "hairColor": "Black",
                "height": [
                    "6'0",
                    "183 cm"
                ],
                "race": "Neyaphem",
                "weight": [
                    "149 lb",
                    "67 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Semihazah",
                    "Duma",
                    "Keriel",
                    "Mastema",
                    "Beliar",
                    "Gadreel",
                    "Beelzebub",
                    "Satan"
                ],
                "alignment": "bad",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Uncanny X-Men #428 (2003)",
                "fullName": "",
                "placeOfBirth": "Isla des Demonas, Caribbean Sea",
                "publisher": "Marvel Comics"
            },
            "connections": {
                "groupAffiliation": "-",
                "relatives": "Kurt Wagner (Nightcrawler, son), Nils Styger (Abyss, son), Kiwi Black (son), numberous other offspring (deceased)"
            },
            "id": 44,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/57-azazel.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/57-azazel.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/57-azazel.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/57-azazel.jpg"
            },
            "name": "Azazel",
            "powerstats": {
                "combat": 80,
                "durability": 95,
                "intelligence": 50,
                "power": 100,
                "speed": 47,
                "strength": 11
            },
            "slug": "57-azazel",
            "work": {
                "base": "Brimstone Dimension; formerly La Isla des Demonas, Bermuda",
                "occupation": "Leader of the Neyaphem"
            }
        }
    ]
}
```