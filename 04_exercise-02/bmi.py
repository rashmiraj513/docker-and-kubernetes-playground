print("(1) Metric (m, kg) or (2) Non-Metric (ft, pounds)?")

chosen_system = input("Please choose: ")

if chosen_system != "1" and chosen_system != "2":
    print("You have to choose either metric or non-metric. Shutting down...")
    exit()

height_unit = "meters"
weight_unit = "kilograms"

if chosen_system == "2":
    height_unit = "feet"
    weight_unit = "pounds"

print("Please enter your height in " + height_unit)
user_height = float(input("Your height: "))

print("Please enter your weight in " + weight_unit)
user_weight = float(input("Your weight: "))

adj_height = user_height
adj_weight = user_weight

if chosen_system == "2":
    adj_height = user_height / 3.28084
    adj_weight = user_weight / 2.20462

bmi = adj_weight / (adj_height * adj_height)
print("\nYour body-mass-index: " + str(bmi))

print("\n")

# Showing the health risk according to the calculated BMI
if bmi < 18.5:
    print("You are underweight and health risk is minimal.")
elif bmi < 25:
    print("You are normal weight and health risk is minimal.")
elif bmi < 30:
    print("You are overweight and health risk is increased.")
elif bmi < 35:
    print("You are obese and health risk is high.")
elif bmi < 40:
    print("You are severely obese and health risk is very high.")
else:
    print("You are morbidly obese and health risk is extremely high.")
