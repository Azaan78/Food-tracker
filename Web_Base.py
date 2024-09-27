#importing functions for flask
from flask import Flask, render_template, request, redirect, url_for, flash

#importing functions
from function import food,Food_Addition,Food_Check,Food_Removal

#importing variables and array
from function import Current_Calorie,Current_Protein,Current_Fats,Current_Carbs,today

app=Flask(__name__,template_folder="WebPages")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Add_Food')
def Food_Add_Page():
    return render_template('Food_Addition.html')

if __name__=="__main__":
	app.run(host="0.0.0.0", port=80, debug=True)