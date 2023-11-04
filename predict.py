from flask import Flask, render_template, request
import numpy as np
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'G:/My Drive/Plant-Leaf-Disease-Prediction-main/model.h5'
trained_model = load_model(filepath)
print(trained_model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
  test_image = load_img(tomato_plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = trained_model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if pred==0:
      return "Bacteria Spot Disease", 'Bacteria Spot.html'
       
  elif pred==1:
      return "Early Blight Disease", 'Early_Blight.html'
        
  elif pred==2:
      return "Healthy and Fresh Leaves", 'Healthy.html'
        
  elif pred==3:
      return "Late Blight Disease", 'Late_blight.html'
       
  elif pred==4:
      return "Leaf Mold Disease", 'Leaf_Mold.html'
        
  elif pred==5:
      return "Septoria Leaf Spot Disease", 'Septoria_leaf_spot.html'
        
  elif pred==6:
      return "Target Spot Disease", 'Target_Spot.html'
        
  elif pred==7:
      return "Yellow Leaf Curl Virus Disease", 'Yellow_Leaf_Curl_Virus.html'
  elif pred==8:
      return "Mosaic Virus Disease", 'Mosaic_virus.html'
        
  elif pred==9:
      return "Two Spotted Spider Mite Disease", 'Two-spotted_spider_mite.html'

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fed input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('G:/My Drive/Plant-Leaf-Disease-Prediction-main/static/upload', filename)
        file.save(file_path)

        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=5080) 
    
    
