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
    #print descriptions of food item
    def Print_Food(self):
        print(self.name,self.calories,self.protein,self.fats,self.carbs)

#function for adding food
def Food_Addition(Current_Calorie,Current_Protein,Current_Fats,Current_Carbs):
    #details about new tracked item
        New_Name=input("Enter name of food: ")
        New_Calories=float(input("Enter calories:   "))
        New_Protein=float(input("Enter protein: "))
        New_Fats=float(input("Enter fats:   "))
        New_Carbs=float(input("Enter carbs: "))
    #instantiating new food item and appending to list
        New_Name=food(New_Name,New_Calories,New_Protein,New_Fats,New_Carbs)
        today.append(New_Name)
    #tracking macronutrients for the day
        Current_Calorie=(New_Calories+Current_Calorie)
        Current_Protein=(New_Protein+Current_Protein)
        Current_Fats=(New_Fats+Current_Fats)
        Current_Carbs=(New_Carbs+Current_Carbs)
        print(Current_Calorie,Current_Protein,Current_Fats,Current_Carbs)
        return Current_Calorie,Current_Protein,Current_Fats,Current_Carbs

#function for checking progress
def Food_Check(Current_Calorie,Current_Protein,Current_Fats,Current_Carbs,Calorie_Goal,Protein_Goal,Fat_Goal,Carb_Goal):
     #checking list is not empty
        length=len(today)
        if length==0:
            print("List empty, no food tracked today")
            return
    #displays progress from todays tracker
        elif length<=1:
            print("---Todays food list---")
            for x in range(0,length):
                today[x].Print_Food()
            print(f"""---Todays progress---
{Current_Calorie}/{Calorie_Goal} calories
{Current_Protein}/{Protein_Goal} protein
{Current_Fats}/{Fat_Goal} fats
{Current_Carbs}/{Carb_Goal} carbs""")

#funtion for removing food
def Food_Removal(today,Current_Calorie,Current_Protein,Current_Fats,Current_Carbs):
    #checking list is not empty
        length=len(today)
        if length>1:
            print("List empty, no food tracked today")
            return today,Current_Calorie,Current_Protein,Current_Fats,Current_Carbs
    #prints current list
        print("---Todays food list---")
        for food_item in today:
            food_item.Print_Food()
    #takes input of item that wants to be removed and searches through list
        Remove_Item=input("Enter name of food item to be removed:    ")
        for food_item in today:
            if food_item.name==Remove_Item:
                today.remove(food_item)
    #tracks macronutrient changes
                Current_Calorie-=food_item.calories
                Current_Protein-=food_item.protein
                Current_Fats-=food_item.fats
                Current_Carbs-=food_item.carbs
                print("Item removed successfully")
                return today,Current_Calorie,Current_Protein,Current_Fats,Current_Carbs
        else:
            print("Item not in list")
            return today,Current_Calorie,Current_Protein,Current_Fats,Current_Carbs
