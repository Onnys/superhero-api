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
                "eyeColor": "Blue",
                "gender": "Male",
                "hairColor": "No Hair",
                "height": [
                    "6'1",
                    "185 cm"
                ],
                "race": "Ungaran",
                "weight": [
                    "200 lb",
                    "90 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Lagzia"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Showcase #22 (October, 1959)",
                "fullName": "",
                "placeOfBirth": "Ungara",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Green Lantern Corps, Black Lantern Corps",
                "relatives": "Amon Sur (son), Arin Sur (sister), Thaal Sinestro (brother-in-law), Soranik Natu (niece)"
            },
            "id": 3,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/3-abin-sur.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/3-abin-sur.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/3-abin-sur.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/3-abin-sur.jpg"
            },
            "name": "Abin Sur",
            "powerstats": {
                "combat": 65,
                "durability": 64,
                "intelligence": 50,
                "power": 99,
                "speed": 53,
                "strength": 90
            },
            "slug": "3-abin-sur",
            "work": {
                "base": "Oa",
                "occupation": "Green Lantern, former history professor"
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
                "race": "Human",
                "weight": [
                    "195 lb",
                    "88 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Warrior of Two Worlds",
                    "Savior of Rann"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Outsiders #6 (April, 1986)",
                "fullName": "Adam Strange",
                "placeOfBirth": "Chicago, Illinois",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Omega Men, L.E.G.I.O.N., R.E.B.E.L.S., formerly Seven Soldiers of Victory",
                "relatives": "Alanna Strange (wife); Aleea Strange (daughter); Sardath (father-in-law); Janey Strange (sister); Todd Strange (brother, deceased); Bantteir (mother-in-law); Adam Strange II (descendent)"
            },
            "id": 8,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/8-adam-strange.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/8-adam-strange.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/8-adam-strange.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/8-adam-strange.jpg"
            },
            "name": "Adam Strange",
            "powerstats": {
                "combat": 50,
                "durability": 40,
                "intelligence": 69,
                "power": 37,
                "speed": 33,
                "strength": 10
            },
            "slug": "8-adam-strange",
            "work": {
                "base": "Rann, Alpha Centauri System",
                "occupation": "Adventurer, archaelogist, ambassador"
            }
        },
        {
            "appearance": {
                "eyeColor": "Blue",
                "gender": "Male",
                "hairColor": "Blond",
                "height": [
                    "5'11",
                    "180 cm"
                ],
                "race": null,
                "weight": [
                    "201 lb",
                    "90 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Green Lantern",
                    "White King",
                    "Sentinal"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "All-American Comics 16 (1940)",
                "fullName": "Alan Ladd Wellington Scott",
                "placeOfBirth": "Gotham City",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Justice Society of America; Formerly Checkmate; the Sentinels of Magic; Formerly All-Star Squadron",
                "relatives": "Harlequin (Molly Mayne-Scott) (wife), Thorn (Rose Canton) (first wife, deceased), Todd Rice (Obsidian, son), Jennie-Lynn Hayden (Jade, daughter, deceased)"
            },
            "id": 13,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/14-alan-scott.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/14-alan-scott.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/14-alan-scott.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/14-alan-scott.jpg"
            },
            "name": "Alan Scott",
            "powerstats": {
                "combat": 32,
                "durability": 90,
                "intelligence": 63,
                "power": 100,
                "speed": 23,
                "strength": 80
            },
            "slug": "14-alan-scott",
            "work": {
                "base": "Gotham City and New York City; Formerly Capitol City",
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
                "race": "Human",
                "weight": [
                    "160 lb",
                    "72 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Alfred Beagle"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Batman #16 (April, 1943)",
                "fullName": "Alfred Thaddeus Crane Pennyworth",
                "placeOfBirth": "-",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Batman Family, Outsiders",
                "relatives": "Jarvis Pennyworth (father, deceased), Wilfred Pennyworth (older brother), Daphne Pennyworth (niece); Bruce Wayne (Batman, legal ward)"
            },
            "id": 15,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/17-alfred-pennyworth.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/17-alfred-pennyworth.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/17-alfred-pennyworth.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/17-alfred-pennyworth.jpg"
            },
            "name": "Alfred Pennyworth",
            "powerstats": {
                "combat": 55,
                "durability": 10,
                "intelligence": 63,
                "power": 7,
                "speed": 17,
                "strength": 10
            },
            "slug": "17-alfred-pennyworth",
            "work": {
                "base": "Wayne Manor; Batcave; Gotham City",
                "occupation": "Butler; Caretaker, former Actor; Field Medic; Government Agent"
            }
        },
        {
            "appearance": {
                "eyeColor": "Red",
                "gender": "Male",
                "hairColor": "-",
                "height": [
                    "8'5",
                    "257 cm"
                ],
                "race": "Android",
                "weight": [
                    "385 lb",
                    "173 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "Professor Ivos Amazing Android",
                    "Timazo",
                    "Humazo",
                    "Hourmazo"
                ],
                "alignment": "bad",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Brave and the Bold #30 (July, 1960)",
                "fullName": "",
                "placeOfBirth": "-",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Formerly the Secret Society of Super Villains",
                "relatives": "Professor Ivo (creator), Kid Amazo (cyborg offspring)"
            },
            "id": 17,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/20-amazo.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/20-amazo.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/20-amazo.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/20-amazo.jpg"
            },
            "name": "Amazo",
            "powerstats": {
                "combat": 100,
                "durability": 100,
                "intelligence": 63,
                "power": 100,
                "speed": 83,
                "strength": 100
            },
            "slug": "20-amazo",
            "work": {
                "base": "-",
                "occupation": "-"
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
                    "185 lb",
                    "83 kg"
                ]
            },
            "biography": {
                "aliases": [
                    "The Human Zoo; A-Man; The Man with Animal Powers"
                ],
                "alignment": "good",
                "alterEgos": "No alter egos found.",
                "firstAppearance": "Strange Adventures #180 (September, 1965)",
                "fullName": "Bernhard Baker",
                "placeOfBirth": "-",
                "publisher": "DC Comics"
            },
            "connections": {
                "groupAffiliation": "Formerly Animal Masters, Forgotten Heroes, Justice League of America, Justice League Europe",
                "relatives": "Ellen Frazier (wife), Cliff Baker (son), Maxine Baker (daughter), unnamed second daughter, Frank Baker, Jr. (father), Phyllis Baker (mother), unnamed sister, Frank, Sr (grandfather), Teddy (great grandfather), Sherman (great-great grandfather), Jack (great-great-great grandfather), Mary Frazier (mother-in-law), Dudley (uncle-in-law), Annie Cassidy (mother of second daughter), Lucy Cassidy (half-sister of second daughter)"
            },
            "id": 22,
            "images": {
                "lg": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/lg/28-animal-man.jpg",
                "md": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/md/28-animal-man.jpg",
                "sm": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/sm/28-animal-man.jpg",
                "xs": "https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/images/xs/28-animal-man.jpg"
            },
            "name": "Animal Man",
            "powerstats": {
                "combat": 80,
                "durability": 85,
                "intelligence": 56,
                "power": 73,
                "speed": 47,
                "strength": 48
            },
            "slug": "28-animal-man",
            "work": {
                "base": "San Diego, California",
                "occupation": "-"
            }
        },
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