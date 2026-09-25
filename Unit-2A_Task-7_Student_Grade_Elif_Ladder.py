#Student grades based on marks using elif ladder
marks = int(input("Enter the marks obtained: "))
if marks >= 90:
    print(f"Grade: A (Marks: {marks})")
elif marks >= 80:
    print(f"Grade: B (Marks: {marks})")
elif marks >= 70:
    print(f"Grade: C (Marks: {marks})")
elif marks >= 60:
    print(f"Grade: D (Marks: {marks})")
else:
    print(f"Grade: F (Marks: {marks})")
