#Simple formula to calculate age of user, add reminder push-notification's for birthday.


birth_year = input("What year were you born? ")

def user_age(birth_year):
    current_year = 2024
    age = current_year - birth_year
    return age

age = user_age (int(birth_year))


print("So, that means you are," " " + f"{age}" + " " "years old!" )


