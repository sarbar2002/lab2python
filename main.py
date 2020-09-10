# Author: Sarthak Singh sxs6666@psu.edu
#Collaborator: Nicholas Cole nyc5096@psu.edu
# Collaborator: Bryce Awono bna5160@psu.edu
# Section: 12R
# Breakout: 8

def getLetterGrade(grade):
  if grade >= 93:
    return "A"
  elif grade >= 90:
    return "A-"
  elif grade >= 87:
    return "B+."
  elif grade >= 83:
    return "B." 
  elif grade >= 80:
    return "B-."
  elif grade >= 77:
    return "C+."
  elif grade >= 70:
    return "C."
  elif grade >= 60:
    return "D."
  elif grade < 60:
   return "F."

def run():
    grade_input = float(input("Enter your CMPSC 131 grade: "))  
    print(f"Your letter Grade for CMPSC 131 is {getLetterGrade(grade_input)}")
  


  if __name__ == "__main__":
    run()