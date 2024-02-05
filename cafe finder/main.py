from flask import Flask, render_template, redirect, url_for ,request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import pandas as pd
import os
import csv
import requests
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    link = StringField(label='Cafe Link', validators=[DataRequired()])
    open = StringField(label='Cafe Opening Time', validators=[DataRequired()])
    close = StringField(label='Cafe Closing Time', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating',choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],validators=[DataRequired()])
    wifi = SelectField(label='Wifi Strength',choices = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],validators=[DataRequired()])
    power = SelectField(label='Socket Available',choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"] ,validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit() :
        cafe_data = list(form.data.values())
        print(cafe_data)
        with open("cafe-data.csv", 'a', encoding='UTF8'  ) as f :
            
            f.write(f"\n{form.cafe.data},"
                        f"{form.link.data},"
                        f"{form.open.data},"
                        f"{form.close.data},"
                        f"{form.coffee.data},"
                        f"{form.wifi.data},"
                        f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes',methods=['GET','POST'])
def cafes():
    df = pd.read_csv('cafe-data.csv')
    list_of_rows = df.values.tolist()
    return render_template('cafes.html',cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
