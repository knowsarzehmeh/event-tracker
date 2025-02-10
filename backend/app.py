from flask import Flask,request, jsonify

from config import config
from config.db import db
from models.event import Event
app = Flask(__name__)
app.config.from_object(config)    
db.init_app(app)


@app.route("/", methods=["GET"]) 
def index():
    return "Hello, World!"


@app.route('/events',methods=['POST'])
def create_event():
    description = request.get_json().get('description') 
    event = Event(description= description)
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_json()),201

@app.route('/events',methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.date.desc()).all()
    result = [event.to_json() for event in events]
    return jsonify(result),200

@app.route('/events/<int:event_id>',methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_json()),200


@app.route('/events/<int:event_id>',methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify(event.to_json()),200

@app.route('/events/<int:event_id>',methods=['PUT'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    description = request.get_json().get('description')
    event.description = description
    db.session.commit()
    return jsonify(event.to_json()),200

if __name__ == "__main__":
   with app.app_context():
       db.create_all()
   app.run(debug=True)
