# Sample records of the form FIRSTNAME, SURNAME, AGE
records = [
    ("Abigail", "Smith", 30),
    ("Barny", "Adams", 25),
    ("David", "Brown", 45),
    ("Freya", "Williams", 22),
    ("Jack", "Johnson", 33),
    ("Nicola", "Lee", 28),
    ("Phoebe", "Taylor", 40),
    ("Trevor", "Clark", 37),
    ("Zuya", "Walker", 29)
]

# FIRST RESORT records by surname to ensure sorted by the key field being used (surname)
records.sort(key=lambda x: x[1])

target = input("Enter a surname to search for: ")

low = 0
high = len(_______) - 1
details = ""

while ___ <= high:

    mid = ___________________________
    
    firstname, surname, age = records[mid]
    
    if surname == target:
        details = "{} {} is age {}".format(firstname, surname, age)
        break
    elif 

print(details if details else "Not found!")