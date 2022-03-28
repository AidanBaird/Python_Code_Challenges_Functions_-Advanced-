#

def lots_of_math(a,b,c,d):
  aplusb = a + b
  cminusd = c - d
  aplusb_cminusd = aplusb * cminusd
  return (aplusb_cminusd % a)


print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))