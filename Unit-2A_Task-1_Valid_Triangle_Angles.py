#Determining if the given angles can form a valid triangle
Angle1 = float(input("Enter the first angle: "))
Angle2 = float(input("Enter the second angle: "))
Angle3 = float(input("Enter the third angle: "))

if Angle1 + Angle2 + Angle3 == 180 and Angle1 > 0 and Angle2 > 0 and Angle3 > 0:
    print(f"The given angles {Angle1}, {Angle2}, and {Angle3} can form a valid triangle.")
else:
    print(f"The given angles {Angle1}, {Angle2}, and {Angle3} cannot form a valid triangle.")