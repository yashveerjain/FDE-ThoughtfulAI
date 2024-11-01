def sort(width, height, length, mass):
  is_bulky = False
  is_heavy = False
  
  # check volume, if volume is greater than 1,000,000, then it is bulky
  if width * height * length > 1e6 :
    is_bulky = True

  # check mass, if mass is greater than 20, then it is heavy
  if mass > 20 :
    is_heavy = True

  if is_heavy and is_bulky:
    return "REJECTED"
  elif is_heavy or is_bulky:
    return "SPECIAL"
  else:
    return "STANDARD"

if __name__ == "__main__":
  width = float(input("Enter the width of the package: "))
  height = float(input("Enter the height of the package: "))
  length = float(input("Enter the length of the package: "))
  mass = float(input("Enter the mass of the package: "))
  print(sort(width, height, length, mass))
  
