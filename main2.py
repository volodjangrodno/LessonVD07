from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class nameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = nameForm()
    if form.validate_on_submit():
        name = form.name.data

        return redirect(url_for('hello', name=name))
    return render_template('index.html', form=form)


@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)