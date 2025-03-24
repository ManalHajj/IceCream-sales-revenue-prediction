import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb')) #undumping our model

# Home URL, if the user search this what do we want to show him ?
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        prediction = model.predict([[float(request.form.get('temperature'))]])
        output = round(prediction[0],2) # Max 2 decimal points
        print(output)
    except ValueError: 
        return render_template('index.html', prediction_text="Invalid input! Please enter a valid number.")
    
    return render_template('index.html', prediction_text=f'Total revenue generated is {output} MAD')

if __name__== '__main__':
    app.run(debug=True)