from flask_restful import Resource
import requests, json

class Pokemon(Resource):
    def get(self, id):
        r = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(id))

        json_response = r.json()

        included = []

        for ability in json_response['abilities']:
            json_ability = requests.get(ability['ability']['url']).json()
            json_api_ability = {
                "type" : "abilities"
                , "id" : json_ability['id']
                , "attributes" : {
                    "name" : json_ability['name']
                    , "is_main_series" : json_ability['is_main_series']
                    , "is_hidden" : ability['is_hidden']
                    , "slot" : ability['slot']
                }
            }
            included.append(json_api_ability)

        for form in json_response['forms']:
            json_form = requests.get(form['url']).json()
            json_api_form = {
                "type": "form"
                , "id" : json_form['id']
                , "attributes" : {
                    "name" : form['name']
                    , "form_name" : json_form['form_name']
                    , "form_order" : json_form['form_order']
                    , "is_battle_only" : json_form['is_battle_only']
                    , "is_default" : json_form['is_default']
                    , "is_mega" : json_form['is_mega']
                    , "order" : json_form['order'] 
                }
            }
            included.append(json_api_form)


        json_api_response = {
            "data" : [{
                "type" : "pokemon"
                , "id" : json_response['id']
                , "attributes" : {
                    "name" : json_response['name']
                    , "base_experience" : json_response['base_experience']
                    , "height" : json_response['height']
                    , "is_default" : json_response['is_default']
                    , "order" : json_response['order']
                    , "weight" : json_response['weight']
                    , "location_area_encounters" : json_response['location_area_encounters'] #not sure if this should be here 
                }
            }], 
            "included" : included
        }

        return json.dumps(json_api_response)