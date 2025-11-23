import math

# ----------------------------
# #1 Area of a Circle
# ----------------------------
print("#1:")
print("This is the circle area calculator!")
radius = float(input("What is the radius of the circle? "))
area = math.pi * radius * radius
print("This is the area of your circle:", round(area, 2))
print()

# ----------------------------
# #2 Expression Solver
# ----------------------------
print("#2:")
print("This is the expression solver for  (a - b)+(a * b)!")

def solve_expression(a, b):
    return (a - b) + (a * b)

a = int(input("What is the value for a? "))
b = int(input("What is the value for b? "))
answer = solve_expression(a, b)
print("The answer is:", answer)
print()

# ----------------------------
# #3 ASCII Art
# ----------------------------
print("#3:")
print("Welcome to my ASCII museum!")

art1 = r"""
      ~+
         *       +
      '         |
    ()     - o -
      .-=""'""=.-.
     '=.___.='
"""

art2 = r"""
  (\_/)
  ( •_•)
  / >🍪  Here is a bunny with a cookie
"""

choice = input("Do you want to see picture 1 or 2? ")

if choice.strip() == "1":
    print("Here is picture #1:")
    print(art1)
else:
    print("Here is picture #2:")
    print(art2)
