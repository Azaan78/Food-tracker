#variables
    #inputs
Calorie_Goal=(int(input("Enter calorie goal to nearest integer:  ")))
Protein_Goal=(int(input("Enter protein goal to nearest gram:  ")))
Fat_Goal=(int(input("Enter fat goal to nearest gram:  ")))
Carb_Goal=(int(input("Enter carb goal to nearest gram:  ")))
    #day trackers
Current_Calorie=(0)
Current_Protein=(0)
Current_Fats=(0)
Current_Carbs=(0)
    #list day tracker
today=[]

# defining food class
class food:
    def __init__(self,name,calories,protein,fats,carbs):
        self.name=name
        self.calories=calories
        self.protein=protein
        self.fats=fats
        self.carbs=carbs

#main loop for testing in text-based iteration
finished=False
while finished==False:
    select=int(input("""(1) Add new food
(2) View total tracking details
(3) End terminal
"""))
    if select==1:
        New_Name=input("Enter name of food: ")
        New_Calories=float(input("Enter calories:   "))
        New_Protein=float(input("Enter protein: "))
        New_Fats=float(input("Enter fats:   "))
        New_Carbs=float(input("Enter carbs: "))
        New_Name=food(New_Name,New_Calories,New_Protein,New_Fats,New_Carbs)
        today=today.append(New_Name)
    elif select==2:
        print(today)
    elif select==3:
        finished=True