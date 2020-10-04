from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Models import setup_db , superheros
import json

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,DELETE')
        return response

    @app.route("/")
    def hello():
        # hero = Hero(name='onnys', slug='ola')
    
        return jsonify({
            'success': True
        })

    @app.route('/superhero-api', methods=['GET'])
    def superhero_api():
        #superhero = 
        #formated_hero = [superhero.format for superheros in superhero]
        superhero = list(map(superheros.format, superheros.query.all()))
        return jsonify({
            'success': True,
            'superhero':superhero,
        #   'name': hero.name,
        #   'slug': hero.slug,
          #'powerstats': formated_hero, 
        #   'appearance':,
        #   'biography':,
        #   'work':,
        #   'connections':
        #   'images':
        })

    @app.route('/add-superhero', methods=['POST'])
    def add_superhero():
        body = request.get_json()
        new_name = body.get('name', None)
        new_slug = body.get('slug',None)
        powerstats = body.get('powerstats',None)
        new_intelligence = powerstats['intelligence']
        new_strength = powerstats['strength']
        new_speed = powerstats['speed']
        new_durability = powerstats['durability']
        new_power = powerstats['power']
        new_combat = powerstats['combat']
        # appearance
        appearance = body.get('appearance',None)
        new_gender = appearance['gender']
        new_race = appearance['race']
        new_height = appearance['height']
        new_weight = appearance['weight']
        new_eyeColor = appearance['eyeColor']
        new_hairColor = appearance['hairColor']
        # biography
        biography = body.get('biography',None)
        new_fullName = biography['fullName']
        new_alterEgos = biography['alterEgos']
        new_aliases = biography['aliases']
        new_placeOfBirth = biography['placeOfBirth']
        new_firstAppearance = biography['firstAppearance']
        new_publisher = biography['publisher']
        new_alignment = biography['alignment']
        # work
        work = body.get('work',None)
        new_occupation = work['occupation']
        new_base = work['base']
        # connections
        connections = body.get('connections',None)
        new_groupAffiliation = connections['groupAffiliation']
        new_relatives = connections['relatives']
        # images
        images = body.get('images',None)
        new_xs = images['xs']
        new_sm = images['sm']
        new_md = images['md']
        new_lg = images['lg']
        try:
            superhero = superheros(name = new_name, slug = new_slug, intelligence = new_intelligence,
                    strength = new_strength, speed = new_speed, durability = new_durability, power = new_power,
                    combat = new_combat, gender = new_gender, race = new_race, height = new_height, weight = new_weight,
                    eyeColor = new_eyeColor, hairColor = new_hairColor, fullName = new_fullName, alterEgos = new_alterEgos,
                    aliases = new_aliases, placeOfBirth = new_placeOfBirth, firstAppearance = new_firstAppearance, publisher = new_publisher,
                    alignment = new_alignment, occupation = new_occupation, base = new_base, groupAffiliation = new_groupAffiliation,
                    relatives = new_relatives, xs = new_xs, sm = new_sm, md = new_md, lg= new_lg)
            superhero.insert()   
        except:
            abort(400)
        
        return jsonify({
            'success': True
        })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)