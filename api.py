# way to upload image

# way to save the image

# function to make prediction on the image

# show the result
import os
from flask import Flask
from flask import request
from flask import render_template
import numpy as np
import random

app = Flask(__name__)

UPLOAD_FOLDER = "/home/sankarshan/Documents/code/web_api_for_computer_vision/static"

# GET: accessing the website
# POST: accessing the form
@app.route("/", methods = ["GET", "POST"])
def upload_predict():
    # this function should show index.html
    # simulate the model prediction value
    
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(
                UPLOAD_FOLDER, 
                image_file.filename
            )
            image_file.save(image_location)
    
            pred_class, pred_proba = get_prediction()
            return render_template("index.html", 
                                prediction_class = pred_class, 
                                prediction_proba = pred_proba,
                                image_file = image_file.filename)

    return render_template("index.html", 
                    prediction_class = "no image given", 
                    prediction_proba = 0, image_file=None)

def get_prediction():
    """This is a random prediction working as a baseline 

    Returns:
        Prediction class and probability
    """
    
    ################################################
    # put your original prediction code here
    ################################################
    
    pred_proba = np.round(np.random.rand(), 4)
    pred_class = random.choice(["cat", "dog",  "monkey"])
    return pred_class, pred_proba

if __name__ == "__main__":
    app.run(port=12000, debug=True)