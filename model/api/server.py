from flask import Flask, request, jsonify
import utils
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

@app.route('/get_fruit', methods=['POST'])
def predict_fruit():
    # Ensure image data is present in the request
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Process the image from the request
    image_file = request.files['image']
    image = Image.open(image_file.stream).convert('RGB')
    image = image.resize((224, 224))  # Resize if needed
    img_array = np.array(image) / 255.0  # Normalize the image

    # Get prediction from the model
    prediction = utils.get_fruit(img_array)

    response = jsonify({
        'fruit': prediction
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Vision Pay...")
    utils.load_saved_artifacts()
    app.run(debug=True)
