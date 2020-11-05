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
* This API is deployed at [superheros-api](https://superherosapi.herokuapp.com/)
- https://superherosapi.herokuapp.com/add-superhero
- https://superherosapi.herokuapp.com/superheros?page=1
- https://superherosapi.herokuapp.com/dc-comics
- https://superherosapi.herokuapp.com/superheros/<string:publisher>
- https://superherosapi.herokuapp.com/<string:publisher>/<string:race>
- https://superherosapi.herokuapp.com/superheros/<string:publisher>/<string:gender>
- https://superherosapi.herokuapp.com//superhero/<int:character_id>
 


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

## GET 'https://superherosapi.herokuapp.com/superheros/<string:publisher>'
- Fetches  a dictionary of superheros from a given publisher in URL
- Request Arguments: publisher
- Returns: a success value and a list of superheros from given publisher

## GET 'https://superherosapi.herokuapp.com/<string:publisher>/<string:race>'
- Fetches  a dictionary of superheros from a given publisher and race in URL
- Request Arguments: publisher and race
- Returns: a success value and a list of superheros from given publisher and race
```bash
https://superherosapi.herokuapp.com/superhero/DC Comics/Human
```

## GET 'https://superherosapi.herokuapp.com/superheros/<string:publisher>/<string:gender>'
- Fetches  a dictionary of superheros from a given publisher and gender in URL
- Request Arguments: publisher and gender
- Returns: a success value and a list of superheros from given publisher and gender

```bash
https://superherosapi.herokuapp.com/superhero/DC Comics/Male
```

## GET 'https://superherosapi.herokuapp.com//superhero/<int:character_id>'

- Fetches  a superhero from an ID in URL
- Request Arguments: character_id
- Returns: a success value and a superhero from given ID

```bash
https://superherosapi.herokuapp.com/superhero/2
```