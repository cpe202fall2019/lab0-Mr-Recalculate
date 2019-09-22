def weight_on_planets():
   # write your code here
   #prompts user to enter weight and stores weight as a str
   weight = input('What do you weigh on earth? ')
   #casts weight to int
   weight = int(weight)
   #prints user's weigh on mars and jupiter using f string formatting
   print(f"\nOn Mars you would weigh {weight*.38} pounds.\nOn Jupiter you would weigh {weight*2.34} pounds.")
  
if __name__ == '__main__':
   weight_on_planets()