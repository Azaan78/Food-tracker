#importing functions
from function import food,Food_Addition,Food_Check,Food_Removal

#importing variables and array
from function import Current_Calorie,Current_Protein,Current_Fats,Current_Carbs,today

#inputs
Calorie_Goal=(float(input("Enter calorie goal to nearest integer:  ")))
Protein_Goal=(float(input("Enter protein goal to nearest gram:  ")))
Fat_Goal=(float(input("Enter fat goal to nearest gram:  ")))
Carb_Goal=(float(input("Enter carb goal to nearest gram:  ")))

#main loop for testing in text-based iteration
finished=False
while finished==False:
    #option select
    select=int(input("""---OPTION SELECT---
(1) Track new food
(2) View todays tracking details
(3) Remove item from list
(4) End terminal
"""))
    #calling food addition function
    if select==1:
        Current_Calorie,Current_Protein,Current_Fats,Current_Carbs=Food_Addition(Current_Calorie,Current_Protein,Current_Fats,Current_Carbs)
    #calling food check function
    elif select==2:
    #checking list is not empty
        Food_Check(Current_Calorie,Current_Protein,Current_Fats,Current_Carbs,Calorie_Goal,Protein_Goal,Fat_Goal,Carb_Goal)
    #calling food removal function
    elif select==3:
        today,Current_Calorie,Current_Protein,Current_Fats,Current_Carbs=Food_Removal(today,Current_Calorie,Current_Protein,Current_Fats,Current_Carbs)
    #ends loop and program
    elif select==4:
        print("---END TERMINAL---")
        finished=True