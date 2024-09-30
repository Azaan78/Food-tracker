#importing functions for flask
from flask import Flask, render_template, request, redirect, url_for, flash, session

# defining food class
class food:
    def __init__(self,name,calories,protein,fats,carbs):
        self.name=name
        self.calories=calories
        self.protein=protein
        self.fats=fats
        self.carbs=carbs

    #print descriptions of food item
    def Print_Food(self):
        print(self.name,self.calories,self.protein,self.fats,self.carbs)

    #converts object to dictionary so can be read by flask to be compatible with JSON and cookies
    def to_dict(self):
        return {
            'name': self.name,
            'calories': self.calories,
            'protein': self.protein,
            'fats': self.fats,
            'carbs': self.carbs
            }
    
    #creates an object from a dictionary
    @staticmethod
    def from_dict(data):
        return food(data['name'], data['calories'], data['protein'], data['fats'], data['carbs'])

#defining app-website
app=Flask(__name__,template_folder="WebPages")
app.secret_key=('Secret_Yeah_Shush')

#initialising session variables
@app.before_request
def before_request():
     if 'Current_Calorie' not in session:
        session['Current_Calorie']=0
        session['Current_Protein']=0
        session['Current_Fats']=0
        session['Current_Carbs']=0
        session['today']=[]

#defining home page and route
@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

#defining addition page and route
@app.route('/Add_Food',methods=['POST','GET'])
def Food_Add_Page():
    if request.method=="POST":
    #fetching variable values from HTML form
        New_Name=request.form['name']
        New_Calories=float(request.form['calories'])
        New_Protein=float(request.form['protein'])
        New_Fats=float(request.form['fats'])
        New_Carbs=float(request.form['carbs'])
    #instantiating new object form class
        New_Name=food(New_Name,New_Calories,New_Protein,New_Fats,New_Carbs)
        session['today'].append(New_Name.to_dict())
        print(session['today'])
    #updating variables
        session['Current_Calorie']+=New_Calories
        session['Current_Protein']+=New_Protein
        session['Current_Fats']+=New_Fats
        session['Current_Carbs']+=New_Carbs
        return redirect('/')
    return render_template('Food_Addition.html')

#defining removal page and route
@app.route('/Remove_Food',methods=['POST','GET'])
def Food_Remove_Page():
    return render_template('Food_Removal.html')

#defining check page and route
@app.route('/Check_Food',methods=['POST','GET'])
def Food_Check_Page():
    return render_template('Food_Check.html')

#initialise the loop to set up website
if __name__=="__main__":
	app.run(host="0.0.0.0", port=80, debug=True)