#Create a dictionary of {name: age}; loop to print adults (>=18) using items()
cricketers = {"Rahul": 1,"Dhoni": 7,"Virat": 18,"Rohit": 45,"Sachin": 10,"Jasprit":93}

# Loop using items()
for name, age in cricketers.items():
    if age >= 18:
        print(f"Adults are :",name)
