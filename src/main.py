from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Dipta Saha")
print("Today's Date:", date.today())

print("Add Result:", add(10, 5))
print("Subtract Result:", subtract(10, 5))

print("Multiply Result:", multiply(10, 5))

print("Divide Result:", divide(10, 0))
print("Divide Result:", divide(10, 2))