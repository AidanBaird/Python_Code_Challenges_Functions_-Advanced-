# Create a function that finds the tip size when given the total cost and the percentaged tip size in question

def tip(total, percentage):
    return ((total * percentage) / 100)


print(tip(10, 25))
print(tip(0, 100))