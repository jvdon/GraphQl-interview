from main import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    fidelity = db.Column(db.Integer)
    amount = db.Column(db.Float)


    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": str(self.created_at.strftime('%d-%m-%Y')),
            "user": User.query.filter_by(id=self.user_id).all(),
            "fidelity": self.fidelity,
            "amount": self.amount
        }
    
