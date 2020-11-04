from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from Models import setup_db , superheros
import json
from flask_migrate import Migrate


HEROS_PER_PAGE = 10


def paginate_dc(request):
    page = request.args.get('page', 1, type=int)
    try:
        selection_of_heros_dc = superheros.query.filter(
            superheros.publisher == 'DC Comics').paginate(page, per_page=HEROS_PER_PAGE)
    except:
        abort(422)
    
    superheros_dc = [hero.format()
                 for hero in selection_of_heros_dc.items]
    return superheros_dc


def paginate_heros(request):
    page = request.args.get('page', 1, type=int)
    try:
        selection_of_heros = superheros.query.order_by(
            superheros.id).paginate(page, per_page=HEROS_PER_PAGE)
    except:
       abort(422)
    
    superhero = [hero.format()
                 for hero in selection_of_heros.items]

    return superhero

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

    @app.route('/')
    def hello():
        return 'Welcome'
    
    @app.route('/superheros/<string:publisher>', methods=['GET'])
    def get_superheros_by_publisher(publisher):
        try:
            superhero = superheros.query.filter(
            superheros.publisher.like('%'+publisher+'%')).all()    
        except :
            abort(404)

        formated_superhero = [hero.format()
                             for hero in superhero]
        
        return jsonify({
            'success':True,
            publisher+'':formated_superhero
        })

    @app.route('/superhero/<string:publisher>/<string:race>', methods=['GET'])
    def get_race_by_publisher(publisher,race):
        
        try:
            superhero = superheros.query.filter(superheros.publisher == publisher, superheros.race == race).all()
           
        except :
            abort(404)
        formated_superhero = [hero.format() 
                             for hero in superhero]
        
        return jsonify({
            'success':True,
            'race':race,
            'publisher':publisher,
            'superhero':formated_superhero
        })

    @app.route('/superhero/<string:publisher>/<string:gender>')
    def get_hero_by_gender_and_publisher(publisher,gender):
        try:
            superhero = superheros.query.filter(superheros.publisher == publisher, superheros.gender == gender).all()    
        except :
            abort(404)
        formated_superhero = [hero.format() 
                             for hero in superhero]
        
        return jsonify({
            'success':True,
            'gender':gender,
            'publisher':publisher,
            'superhero':formated_superhero
        })
        
    @app.route('/superhero/<int:character_id>')
    def get_character(character_id):
        try:
            superhero = superheros.query.get(character_id)
        except:
            abort(404)
        return jsonify({
            'success': True,
            'superhero': superhero.format()
        })

    @app.route('/superheros', methods=['GET'])
    def get_superhero():
        superhero = paginate_heros(request)
        return jsonify({
            'success': True,
            'superhero':superhero,
        })

    @app.route('/dc-characters', methods=['GET'])
    def getdec_comics():
        superhero_from_dc = paginate_dc(request)
        return jsonify({
            'success': True,
            'superhero':superhero_from_dc,
        })

    @app.route('/add-superhero', methods=['POST'])
    def add_superhero():
        body_json = request.get_json()
        for body in body_json:
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
            'id':superhero.id,
            'success': True
        })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'not found'
        }), 404
    
    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessabble entity'
        }), 422
   

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
