def sort(width, height, length, mass):
  is_bulky = False
  is_heavy = False
  
  # check volume, if volume is greater than 1,000,000, then it is bulky
  if width * height * length >= 1e6 or width >= 150 or height >= 150 or length >= 150:
    is_bulky = True

  # check mass, if mass is greater than 20, then it is heavy
  if mass >= 20 :
    is_heavy = True

  if is_heavy and is_bulky:
    return "REJECTED"
  elif is_heavy or is_bulky:
    return "SPECIAL"
  else:
    return "STANDARD"

if __name__ == "__main__":
    print("Running Test Cases: ")
    print("Width : 100, Height : 50, Length : 20, Mass : 10")
    print("output: ", sort(100, 50, 20, 10))  # Expected output: "STANDARD"

    print("Width : 1000, Height : 100, Length : 100, Mass : 10")
    print("output: ", sort(1000, 100, 100, 10))  # Expected output: "SPECIAL"

    print("Width : 100, Height : 50, Length : 20, Mass : 25")
    print("output: ", sort(100, 50, 20, 25))  # Expected output: "SPECIAL" 
    
    
    print("Width : 150, Height : 10, Length : 15, Mass : 25")
    print("output: ", sort(150, 10, 15, 25))  # Expected output: "REJECTED" (heavy and bulky)

    # get user input
    inp = str(input("Want to enter your own dimensions? (y/n): "))
    if inp == "y" or inp == "Y":    
        width = float(input("Enter the width of the package: "))
        height = float(input("Enter the height of the package: "))
        length = float(input("Enter the length of the package: "))
        mass = float(input("Enter the mass of the package: "))
        print(sort(width, height, length, mass))
    else:
        print("Bye!")
