from flask import Flask, jsonify, request
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*') # Allows cross orgin resource sharing

    return response


@app.route('/predict_home_price',methods=['POST'])
def get_home_prices():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']
    balcony = request.form['balcony']

    response = jsonify({'estimated_price':util.get_estimated_price(location,total_sqft,bath,bhk,balcony)})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask server")
    util.load_saved_artifacts()
    app.run()
