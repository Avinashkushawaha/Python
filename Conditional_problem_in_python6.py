# Choose a mode of transportion based on the distance(e.g, <3 km: Walk, 3-15km: Bike, >15km:Car).
distance = int(input("Enter km here : " ))

if distance < 3:
    transport = "Walk"

elif distance <= 15:
    transport = "bike"

else:
    transport = "Car"

print(transport)            