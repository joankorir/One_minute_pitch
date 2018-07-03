from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    '''
    Class to create a wtf form for pitch creation
    '''
    content = TextAreaField('PITCH CONTENT')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    '''
    class to create a wtf form for creating the Comments
    '''

    comments = TextAreaField("WRITE COMMENT")
    submit = SubmitField('SUBMIT')

class CategoryForm(FlaskForm):
    '''
    Class to create wtf form for displaying the get_categories
    '''

    name = StringField('Category Name', validators=[Required])
    submit =SubmitField('SUBMIT')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required])
    submit = SubmitField('SUBMIT')
