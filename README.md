## Ice Cream Sales Prediction App

This project predicts the revenue of ice cream sales based on temperature using linear regression. The backend is built using Flask, and the model is deployed on Render.

## Features :
Input: Users provide the current temperature.

Output: The app predicts the estimated revenue of ice cream sales based on the given temperature.

Model: A linear regression model.

## Deployment :
The app is deployed on Render. To access the live version, visit:
https://icecream-sales-revenue-prediction.onrender.com/ 

## Pictures
Some screenshots from the app:

![image](https://github.com/user-attachments/assets/687a2a08-0292-48c0-831d-5f165f895b72)
![image](https://github.com/user-attachments/assets/7b7d0591-026b-4670-8685-fee07771fbb0)
![image](https://github.com/user-attachments/assets/6fb3b794-750b-4a5a-8d12-7a6b9bb20e80)

## Structure
main.py: The main Flask app that serves the API.

model.pkl: The trained linear regression model.

machine_learning.ipynb: The Jupyter notebook for training and evaluating the machine learning model.

iceCreamData.csv: The dataset used for training the model.

templates/: Contains HTML files for the frontend.

static/: Contains CSS files for the frontend styling.

requirements.txt: A list of dependencies for the app.

Procfile: Specifies the commands to run the app on Render.
