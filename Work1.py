# Sum of two Numbers
print("Sum of two Numbers")
A = int(input("A: "))
B = int(input("B: "))
Sum = A + B
print("Sum = " + str(Sum))

# Return the next number from integer passed
Sum += 1
print("Next number is " + str(Sum))

# Convert Minute to Seconds
print("Convert Minutes To Seconds")
minutes = int(input("Enter time in minutes: "))
seconds = minutes * 60
print("Your time in seconds: " + str(seconds) + " secs")

# # # Area of a Triangle
print("Solve for Area of a Triangle")
b = float(input("Input Base (Enter 0 if not given): "))
h = float(input("Input Height (Enter 0 if not given): "))
if b == 0:
    print("Now solving for Base")
    area = float(input("Enter given Area: "))
    b = area / (0.5 * h)
    print("Base = " + str(b))
elif h == 0:
    print("Now solving for Height")
    area = float(input("Enter given Area: "))
    h = area / (0.5 * b)
    print("Height = " + str(h))
else:
    Area = 0.5 * b * h
    print("Area = " + str(Area))

# Convert Hours to Seconds
print("Convert Hours To Seconds")
minutes = int(input("Enter Hours: "))
seconds = minutes * 3600
print("Your time in seconds: " + str(seconds) + " secs")

# Convert Age to Days
print("How old are you in Days")
age = int(input("Enter your Age: "))
days = age * 365
print("You have lived for " + str(days) + " days")

# Perimeter of a rectangle
print("Solve for perimeter of a Rectangle")
L = float(input("Enter Length (Put 0 if not given); "))
W = float(input("Enter Width (Put 0 if not given); "))
if L == 0:
    print("Now solving for Length")
    perimeter = float(input("Enter given perimeter: "))
    L = (perimeter/2) - W
    print("Length = " + str(L))
elif W == 0:
    print("Now solving for Width")
    perimeter = float(input("Enter given perimeter: "))
    W = (perimeter / 2) - L
    print("Width = " + str(W))
else:
    Perimeter = 2 * (L + W)
    print("Perimeter = " + str(Perimeter))
