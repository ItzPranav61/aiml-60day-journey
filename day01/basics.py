name = "Pranav"
age = 20
gpa = 8.5
is_enrolled = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_enrolled))

age_str= str(age)
gpa_int = int(gpa)
num_from_str = float("3.14")

print(f"Age as string: {age_str}, type: {type(age_str)}")
print(f"GPA as integer: {gpa_int}")
print(f"Number from string: {num_from_str}")

a, b = 17, 5

print(f"\n---- Arithmetic Operations (a={a}, b={b})----")
print(f"Addition: a + b = {a + b}")
print(f"Subtraction: a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division: a / b = {a / b}")
print(f"Floor Division: a // b = {a // b}")
print(f"Modulus: a % b = {a % b}")
print(f"Exponentiation: a ** b = {a ** b}")

print(f"\n---- Comparison Operations (a={a}, b={b})----")
print(f"Equal: a == b -> {a == b}")
print(f"Not Equal: a != b -> {a != b}")
print(f"Greater Than: a > b -> {a > b}")
print(f"Less Than: a < b -> {a < b}")
print(f"Greater Than or Equal: a >= b -> {a >= b}")
print(f"Less Than or Equal: a <= b -> {a <= b}")
print(f"AND: x and y -> {x and y}")
print(f"OR: x or y -> {x or y}")
print(f"NOT: not x -> {not x}")

def calculator(n1,n2):
    print(f"\n---- Calculator Operations (n1={n1}, n2={n2})----")
    print(f"Addition: n1 + n2 = {n1 + n2}")
    print(f"Subtraction: n1 - n2 = {n1 - n2}")
    print(f"Multiplication: n1 * n2 = {n1 * n2}")
    print(f"Division: n1 / n2 = {n1 / n2}")
    print(f"Floor Division: n1 // n2 = {n1 // n2}")
    print(f"Modulus: n1 % n2 = {n1 % n2}")
    print(f"Exponentiation: n1 ** n2 = {n1 ** n2}")
    print(f"Is n1 greater than n2? {n1 > n2}")
    
calculator(34, 7)

full_name = "Pranav Sawant"
print(full_name.upper())
print(full_name.title())
print(len(full_name))
print(full_name.replace("Sawant", "S."))
print("Pranav" in full_name)