from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index =True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    # pass_secure =db.Column(db.String(255))
    password_hash =db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    comments= db.relationship("Comments", backref="user", lazy ="dynamic")
    vote = db.relationship("Votes", backref="user",lazy= "dynamic")

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class PitchCategory(db.Model):

    __tablename__ = 'categories'

    # pitchCategory columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))


    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = PitchCategory.query.all()
        return categories


#pitches class
class Pitch(db.Model):
    """
    List of pitches in each category
    """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="pitches", lazy = "dynamic")
    vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    def save_pitch(self):
        ''' Save the pitches '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.pitched_ideas.clear()

    # display pitches

    def get_pitches(id):
        pitches = Pitch.query.order_by(
                Pitch.posted.desc()).filter_by(category_id=id).all()
        return pitches



class Comments(db.Model):

    __tablename__ = 'comments'

    id= db.Column(db.Integer,primary_key=True)
    comments= db.Column(db.String(255))
    user_id= db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id =db.Column(db.Integer,db.ForeignKey("pitches.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    def save_comment(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_comments(self,id):
       comment= Comments.query.filter_by(pitches_id =id).all()
       return comment

#votes
class Votes(db.Model):
    '''
    class to model votes
    '''
    __tablename__='votes'

    id = db.Column(db. Integer, primary_key=True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitches_id):
        votes = Vote.query.filter_by(user_id=user_id, pitches_id=pitches_id).all()
        return votes
