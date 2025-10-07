ingredients = ["flour", "sugar", "eggs", "milk"]
oven_temp = "180"
waiting_time = 15
if set(["flour", "sugar", "eggs"]).issubset(ingredients):
    print("Ingredients are complete!")
    print(f"Preheating oven to, {oven_temp}, 'degrees Celsius'")

    for i in range(waiting_time):
        print("Baking... minute", i)

    print("Cake is ready!")
    print("Cake baked successfully")

else:
    print("Missing ingredients!")