from . import db

class User(db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pickuplines_id =db.Column(db.Integer,db.ForeignKey('pickuplines_id'))
    interviewpitch_id =db.Column(db.Integer,db.ForeignKey('interviewpitch_id'))
    productionpitch_id =db.Column(db.Integer,db.ForeignKey('productionpitch_id'))
    promotionPitch_id =db.Column(db.Integer,db.ForeignKey('promotionPitch_id'))
    comments= db.relationship("Comments", backref="user", lazy ="dynamic")

    def __repr__(self):
        return f'User {self.username}'

class Pickuplines(db.model):
    __tablename__='pickuplines'

    id= db.Column(db.Integer,primary_key =True)
    name= db.Column(db.String(255))
    user-id =db.Column(db.Integer,db.ForeignKey("users_id"))
    comments= db.relationship('Comment',backref = 'comments',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'

class Interviewpitch(db.Model):
    __tablename__='interviewpitch'

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(255))
    user-id =db.Column(db.Integer,db.ForeignKey("users_id"))
    comments= db.relationship('Comment',backref = 'comments',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'

class Productionpitch(db.Model):
    __tablename__ ='productionpitch'

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(255))
    user-id =db.Column(db.Integer,db.ForeignKey("users_id"))
    comments= db.relationship('Comment',backref = 'comments',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'

class promotionPitch(db.Model):
    __tablename__ ='Promotionpitch'

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(255))
    user-id =db.Column(db.Integer,db.ForeignKey("users_id"))
    comments= db.relationship('Comment',backref = 'comments',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'

class Comments(db.Model):

    __tablename__ = 'comments'

    id= db.Column(db.Integer,primary_key=True)
    comments= db.Column(db.String(255))
    user_id= db.Column(db.Integer,foreignkey=True)
    pickuplines_id =db.Column(db.Integer,foreignkey=True)


def save_comments(self):
        db.session.add(self)
        db.session.commit()

        @classmethod
        def get_comments(self,id):
            comments = Comments.query.filter_by(pickuplines_id,interviewpitch_id,productionpitch_id,promotionPitch_id).all()
            return comments
