from config.db import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


    def __repr__(self):
        return '<Event %r>' % self.description
    
    
    def to_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'date': self.date
        }