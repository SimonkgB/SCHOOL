import sys

try:
    C = float(sys.arg[1])
except:
    print("Please provide C as a command-line argument")
    C = float(input("C:"))

    
print(f"Successfully read the number {C} from the command-line")
