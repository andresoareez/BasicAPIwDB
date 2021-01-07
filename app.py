from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from models import People, Activities, Usuarios
from flask_httpauth import HTTPBasicAuth
import json

# First simple api created to make a list of developers

auth = HTTPBasicAuth()
apiflask = Flask(__name__)
api = API(app)

@auth.verify_password
def verify(login, password):
    if not (login, password):
        return False
    return users.query.filter_by(login=login, password=password).first()


class Person(Resource):
    @auth.login_required
    def get(self, name):
        person = person.query.filter_by(name=name).first()
        try:
            response = {
                'name': person.name,
                'age': person.name,
                'id': person.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'message':'Person not found'
            }
        return response

    def put(self, name):
        person = People.query.filter_by(name=name).first()
        content = request.json
        if 'name' in content:
            person.name = content['name']
        if 'age' in content:
            person.age = content['age']
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }
        return response

    def delete(self, name):
        person = People.query.filter_by(name=name).first()
        message = 'Person Excluded Successful'.format(person.name)
        person.delete()
        return {'status': 'success', 'message': message}

class PeopleList(Resource):
    @auth.login_required
    def get(self):
        people = People.query.all()
        response = [{'id':i.id, 'name':i.name, 'age':i.age} for i in people]
        return response

    def post(self):
        contents = request.json
        person = People(name=contents['name'], age=contents['age'])
        person.save()
        response = {
            'id':person.id,
            'name':person.name,
            'age':person.age
        }
        return response

class ActivitiesList(Resource):
    def get(self):
        activities = ActivitiesList.query.all()
        response = [{'id':i.id, 'name':i.name, 'person':i.person.name} for i in activities]
        return response

    def post(self):
        content = request.json
        person = People.query.filter_by(name=content['person']).first()
        activity = Activities(name=content['name'], person=person)
        activity.save()
        response = {
            'pessoa':activity.person.name,
            'name':activity.name,
            'id':activity.id
        }
        return response

api.add_resource(Person, '/person/<string:name>/')
api.add_resource(PeopleList, '/person/')
api.add_resource(ActivitiesList, '/activities/')


if __name__ == '__main__':
    app.run(debug=True)
