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
- /add-superhero
- /superheros?page=1

POST 'add-superhero'
- Create a new Superhero.
- Resquet Arguments: name, slug, intelligence, strength, speed, durability, power, combat, gender, race, height, weight, eyeColor, hairColor, fullName, alterEgos, aliases, placeOfBirth, firstAppearance, publisher, alignment, occupation, base, groupAffiliation, relatives, xs, sm, md, lg.
- Returns:  success and a superhero id.
bash```
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

GET '/superheros?page=1'
- Fetches  a dictionary of 10 superheros
- Request Arguments: page
- Returns: a success value and a list of 10 superheros 

bash```
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