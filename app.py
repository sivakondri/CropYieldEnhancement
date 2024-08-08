from flask import Flask, render_template, request, redirect, url_for
import pickle
from openpyxl import Workbook
from sklearn.tree import DecisionTreeClassifier 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/suggest')
def suggest():
    global prediction
    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
    if int(prediction)in crop_dict:
        crop = crop_dict[int(prediction)]
    plant_spacing_dict = {
        "Rice": {"Spacing": "15-30 cm"},
        "Maize": {"In-row spacing": "20-30 cm", "Between-row spacing": "75-90 cm"},
        "Jute": {"In-row spacing": "15-20 cm", "Between-row spacing": "30-45 cm"},
        "Cotton": {"In-row spacing": "45-75 cm", "Between-row spacing": "75-120 cm"},
        "Coconut": {"Spacing": "7-9 meters"},
        "Papaya": {"Spacing": "2-3 meters"},
        "Orange": {"Spacing": "5-7 meters"},
        "Apple": {"Spacing": "4-6 meters"},
        "Muskmelon": {"In-row spacing": "90-120 cm", "Between-row spacing": "180-240 cm"},
        "Watermelon": {"In-row spacing": "90-120 cm", "Between-row spacing": "180-240 cm"},
        "Grapes": {"Spacing": "2-3 meters"},
        "Mango": {"Spacing": "6-10 meters"},
        "Banana": {"Spacing": "2-3 meters"},
        "Pomegranate": {"Spacing": "4-6 meters"},
        "Lentil": {"In-row spacing": "5-10 cm", "Between-row spacing": "30-45 cm"},
        "Blackgram": {"In-row spacing": "10-15 cm", "Between-row spacing": "30-45 cm"},
        "Mungbean": {"In-row spacing": "10-15 cm", "Between-row spacing": "30-45 cm"},
        "Mothbeans": {"In-row spacing": "10-15 cm", "Between-row spacing": "30-45 cm"},
        "Pigeonpeas": {"In-row spacing": "30-60 cm", "Between-row spacing": "90-120 cm"},
        "Kidneybeans": {"In-row spacing": "5-10 cm", "Between-row spacing": "30-45 cm"},
        "Chickpea": {"In-row spacing": "10-15 cm", "Between-row spacing": "30-45 cm"},
        "Coffee": {"In-row spacing": "1-2 meters", "Between-row spacing": "2-3 meters"}
    }
    spacing_info = plant_spacing_dict[crop]    
    for key, value in spacing_info.items():
        return render_template('result.html',key=key,value=value,Crop=crop)
 
@app.route('/submit', methods=['POST'])
def submit():
     global prediction
     if request.method=='POST':
        nitrogen=float(request.form['nitrogen'])
        phosphorus=float(request.form['phosphorus'])
        potassium=float(request.form['potassium'])
        temperature=float(request.form['temperature'])
        humidity=float(request.form['humidity'])
        ph=float(request.form['ph'])
        rainfall=float(request.form['rainfall'])
        model=pickle.load(open('Crop.pkl','rb'))
        prediction=model.predict([[nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
        #print(prediction)
        #return f'Nitrogen: {nitrogen}, Phosphorus: {phosphorus}, Potassium: {potassium}, Temperature: {temperature}, Humidity: {humidity}, pH: {ph}, Rainfall: {rainfall}'
        #return f'<html><body><h1>the best crop to be cultivated is : {int(prediction)}</h1></body></html>'
    
        k=prediction[0]
        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
        if int(k)in crop_dict:
            crop = crop_dict[int(k)]
        return render_template('result.html',crop=crop)
  
if __name__ == '__main__':
    app.run(debug=True)
