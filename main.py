import requests
# Tony Baxter
# NET2008
# Assignment 4: Chinese Zodiac


# Structures needed for Birth Data
class BirthDate:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


# Dictionary for Chinese Zodiac Signs
class ZodiacSigns:
    def __init__(self):
        self.signs = [
            "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
            "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
        ]


# User Input for Date of Birth
def birth_data():
    born = BirthDate()


    # Each Input has error countermeasure in case the input doesn't meet the requirements
    born.month = int(input("Enter your birth month: "))
    while born.month < 1 or born.month > 12:
        print("ERROR! Enter your birth month (1 to 12):")
        born.month = int(input())

    born.day = int(input("Enter your birth day: "))
    while born.day < 1 or born.day > 31:
        print("ERROR! Enter your birth day (1 to 31):")
        born.day = int(input())

    born.year = int(input("Enter your birth year: "))
    while born.year > 2023:
        print("ERROR! Are you from the future?\nEnter your birth year (less than 2023):")
        born.year = int(input())

    return born


# Friend's Input for Date of Birth (Similar to birth_data function)
def friend_data():
    fri_born = BirthDate()

    fri_born.month = int(input("Enter your friend's birth month (between 1 and 12): "))
    while fri_born.month < 1 or fri_born.month > 12:
        print("ERROR! Enter your friend's birth month (1 to 12):")
        fri_born.month = int(input())

    fri_born.day = int(input("Enter your friend's birth day: "))
    while fri_born.day < 1 or fri_born.day > 31:
        print("ERROR! Enter your friend's birth day (1 to 31):")
        fri_born.day = int(input())

    fri_born.year = int(input("Enter your friend's birth year (less than 2023): "))
    while fri_born.year > 2023:
        print("ERROR! Are you from the future?\nEnter your friend's birth year:")
        fri_born.year = int(input())

    return fri_born


# Displays their Zodiac Sign
def print_zodiac_sign(born, zodiac_signs):
    sign = ((born.year - 1912) % 12)
    print(f"Your Sign is: {zodiac_signs.signs[sign]}")


# Displays Friend's Zodiac Sign
def print_friend_zodiac_sign(fri_born, zodiac_signs):
    fri_sign = ((fri_born.year - 1912) % 12)
    print(f"Your Friend's Sign is: {zodiac_signs.signs[fri_sign]}")


# Checks for compatibility between Chinese Zodiac Signs
def is_compatible_zodiac(fri_born, born, zodiac_signs):
    you = ((born.year - 1912) % 12)
    friend = ((fri_born.year - 1912) % 12)

# Adds both Yours and Friend's year to determine compatibility
    if (you + friend) % 2 == 0: # If remainder is 0, the pair is compatible
        print("\nYou two are compatible with each other")
    else:
        print("\nYou two are NOT compatible with each other")


# FINAL RESULT
zodiac_signs = ZodiacSigns()
born = birth_data()
print_zodiac_sign(born, zodiac_signs)
fri_born = friend_data()
print_friend_zodiac_sign(fri_born, zodiac_signs)
is_compatible_zodiac(fri_born, born, zodiac_signs)
