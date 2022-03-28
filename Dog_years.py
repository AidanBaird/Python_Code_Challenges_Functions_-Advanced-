# Create a function that takes your name and age and returns you a message that tells you your age in dog years

def dog_years(name, age):
  years = (age * 7)
  return name + " , you are " + str(years) + " years old in dog years"

print(dog_years("Lola", 16))
print(dog_years("Baby", 0))