#whichcan server http requ
import util
from flask import Flask, request, jsonify

app = Flask(__name__)


#rerun location in bangalore
@app.route('/get_all_locations', methods=['GET'])
def get_all_locations():
    response = jsonify({
        'locations': util.get_all_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_house_price',methods=['GET', 'POST'])
def predict_house_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = str(request.form['location'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    print("Starting Python Flask server for House Prediction")
    util.load_saved_artifacts()
    #predict_house_price()
    app.run()
