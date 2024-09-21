#variables
Calorie_Goal=(int(input("Enter calorie goal to nearest integer:  ")))
Protein_Goal=(int(input("Enter protein goal to nearest integer:  ")))
Fat_Goal=(int(input("Enter fat goal to nearest integer:  ")))
Carb_Goal=(int(input("Enter carb goal to nearest integer:  ")))

# defining food class
class food:
    calories:float
    protein:float
    fats:float
    carbs:float