from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/get_fruit', methods=['GET', 'POST'])
def predict_fruit():
    raw_img = request.form['img']


    response = jsonify({
        'fruit': utils.get_fruit(raw_img)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Vision Pay...")
    utils.load_saved_artifacts()
    app.run()