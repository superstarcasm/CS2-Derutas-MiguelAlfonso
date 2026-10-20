# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")


while True:
    previous = input("Enter previous meter reading: ")
    
    try: 
        previous = float(previous)
        break
    except ValueError:
        print("Invalid previous meter reading. Please try again.")
        previous = float(input("Enter previous meter reading:"))

while True:
    current = input("Enter current meter reading: ")
    
    try: 
        current = float(current)
        break
    except ValueError:
        print("Invalid previous meter reading. Please try again.")
        current = float(input("Enter current meter reading:"))

if name.strip() == "":
    print("Invalid name entered. Please try again.")
    name = input("Enter customer name:")
    
if name.isdigit == True:
    print("Invalid name entered. Please try again.")
    name = input("Enter customer name:")
    
try:
    float(name)
    print("Invalid name entered. Please try again.")
    name = input("Enter customer name:")
except ValueError:
    name = name
    
if previous < 0:
    print("Invalid previous meter reading entered. Please try again.")
    previous = float(input("Enter previous meter reading:"))
    
if current < previous:
    print("Invalid current meter reading entered. Please try again.")
    current = float(input("Enter current meter reading."))
    
    
consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
