from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import random






'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

API_KEY = "TopSecretKey"

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    


with app.app_context():
    db.create_all()






@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random',methods=['GET'])
def random_cafe() :
    if request.method == "GET" :
        max_id = db.session.query(func.max(Cafe.id)).scalar()
        number = random.randint(1,int(max_id))
        random_cafe = db.session.query(Cafe).filter_by(id=str(number)).first()
        if random_cafe:
        # Convert the Cafe object to a dictionary for JSON response
            cafe_data = {
                'id': random_cafe.id,
                'name': random_cafe.name,
                'map_url': random_cafe.map_url,
                'img_url': random_cafe.img_url,
                'location': random_cafe.location,
                'seats': random_cafe.seats,
                'has_toilet': random_cafe.has_toilet,
                'has_wifi': random_cafe.has_wifi,
                'has_sockets': random_cafe.has_sockets,
                'can_take_calls': random_cafe.can_take_calls,
                'coffee_price': random_cafe.coffee_price
            }

            return jsonify(cafe_data)
        else:
            return jsonify({"message":"Content Not Found"})
        

@app.route('/all', methods=['GET'])
def show_all_cafes() :
    list_of_Cafes = []
    if request.method == "GET" :
        cafes = db.session.query(Cafe).all()
        for cafe in cafes :
            temp = {}
            temp ={
                'id': cafe.id,
                'name': cafe.name,
                'map_url': cafe.map_url,
                'img_url': cafe.img_url,
                'location': cafe.location,
                'seats': cafe.seats,
                'has_toilet': cafe.has_toilet,
                'has_wifi': cafe.has_wifi,
                'has_sockets': cafe.has_sockets,
                'can_take_calls': cafe.can_take_calls,
                'coffee_price': cafe.coffee_price
            }
            list_of_Cafes.append(temp)

        return jsonify({"cafes":list_of_Cafes})
    else :
        return jsonify({"message":"404 Error"})
    

@app.route('/search',methods=["GET"])
def searched_cafe() :
    list_of_Cafes = []
    loc = request.args.get('loc')
    if request.method == "GET" :
        if loc :
            cafes = db.session.query(Cafe).filter_by(location=loc).all()
            if cafes :
                for cafe in cafes :
                    temp = {}
                    temp ={
                        'id': cafe.id,
                        'name': cafe.name,
                        'map_url': cafe.map_url,
                        'img_url': cafe.img_url,
                        'location': cafe.location,
                        'seats': cafe.seats,
                        'has_toilet': cafe.has_toilet,
                        'has_wifi': cafe.has_wifi,
                        'has_sockets': cafe.has_sockets,
                        'can_take_calls': cafe.can_take_calls,
                        'coffee_price': cafe.coffee_price
                    }
                    list_of_Cafes.append(temp)
                if list_of_Cafes :
                    return jsonify({"cafes":list_of_Cafes})
            else :
                return jsonify({"message":"Error"})
    else :
        return jsonify({"message":"Error"})
                



# HTTP POST - Create Record
def convert_to_bool(string) :
    if 'rue' in string :
        return True
    elif 'alse' in string :
        return False
    else :
        return string

@app.route('/add',methods=['POST'])
def add_new_cafe() :
    if request.method == "POST" :
        response = {
            'name': request.form['name'],
            'map_url': request.form['map_url'],
            'img_url': request.form['img_url'],
            'location': request.form['location'],
            'seats': request.form['seats'],
            'has_toilet': request.form['has_toilet'],
            'has_wifi': request.form['has_wifi'],
            'has_sockets': request.form['has_sockets'],
            'can_take_calls': request.form['can_take_calls'],
            'coffee_price': request.form['coffee_price'] }
        if response :
            try :
                newCafe = Cafe(name=response['name'],map_url=response['map_url'],img_url=response['img_url'],location=response['location'],seats=response['seats'],has_toilet=convert_to_bool(response['has_toilet']),has_wifi=convert_to_bool(response['has_wifi']),has_sockets=convert_to_bool(response['has_sockets']),can_take_calls=convert_to_bool(response['can_take_calls']),coffee_price=response['coffee_price'])
                db.session.add(newCafe)
                db.session.commit()
                return jsonify({"response":{"success":"succesfully added to the database"}})
            except Exception as e :
                return jsonify({"message":e})
    else :
        return jsonify({"message":"Error"})
    

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:id>',methods=['PATCH'])
def update_price(id:int) :
    if request.method == "PATCH" :
        record = Cafe.query.get_or_404(id)
        if "coffee_price" in request.json :
            record.coffee_price = request.json['coffee_price']
        db.session.commit()
        return jsonify({'success':'Successfully updated the record'})
    else :
        return jsonify({"message":"Error"})
    




# HTTP DELETE - Delete Record
@app.route('/closed-report/<id>',methods=['DELETE'])
def closed_cafe(id) :
    if request.method == "DELETE" :
        if "API_KEY" in request.json :
            if API_KEY == request.json['API_KEY'] :
                record = Cafe.query.get_or_404(id)
                if record :
                    db.session.delete(record)
                    db.session.commit()
                    return jsonify({"Success":"Record has been deleted"})
                else :
                    return jsonify({"Error":"Record with this id does'nt exist"})
            else :
                return jsonify({"Error":"You are not authorized"})
        else :
            return jsonify({"Error":"Please Pass The API Key for delete the record"})
    else :
        return jsonify({"Error":"Request not exist"})



if __name__ == '__main__':
    app.run(debug=True)
