# Create a function that returns the two given names in a new order

def introduction(first_name, last_name):
  comma_last = last_name + ", "
  return comma_last + first_name + " " + last_name

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))
