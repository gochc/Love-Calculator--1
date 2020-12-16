# Love Calculator 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2 # combined both names to make it one string 

lower_combined_name = combined_name.lower() # converted all characters to lower case 

# check how many times each character (true love) appears in the combined names using .count() function
t = lower_combined_name.count("t")  
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")
true = (t + r + u + e) #adding integers of each times the character appears in true 

l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")
love = (l + o + v + e) #adding integers of each times the character appears in love 

love_score = int(str(true) + str(love)) # converted into a string so that the 2 calculations are concatenated rather than calculated 
# The love_score has been wrapped around an int() so that it can be compared against actual numbers in the conditional statements below
if love_score < 10 or love_score > 90:
  print(f"Your score is: {love_score}, you go together like coke and mentos")
elif love_score >=40 and love_score <=50:
  print(f"Your scrore is: {love_score}, You are alright together")
else:
  print(f"Your score is:{love_score}")