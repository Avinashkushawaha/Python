# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
Order_size = "Large"
extra_shot = True

if extra_shot:
    coffee = Order_size + " coffee with an extra shot"

else:
    coffee = Order_size + " coffee" 

print("Order:" , coffee)       
