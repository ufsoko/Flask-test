from App.ext import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    title = db.Column(db.String(25))
    body = db.Column(db.Text(250))
    create_time = db.Columu(db.DateTime)
    #testt

    def save(self):
        db.session.add(self)
        db.session.commit()