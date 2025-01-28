import random
import string

def generate_password(min_length, numbers= True,special_characters=True ): 

  letters = string.ascii_letters 
  digits = string.digits 
  special= string.punctuation 
  

  characters=letters #build a character string that has all the characters that we can pick from
  if numbers:  #if there are numbers, execute the following
    characters += digits
  if special_characters:  #if there are special characters, execute the following
    characters += special  

  password= ""  #setting variables
  meets_criteria= False  # so it can be True when it meets the criteria
  has_number= False
  has_special= False
  
  while not meets_criteria or len(password) < min_length: #when either of these are true then we are gonna continue
    new_char= random.choice(characters) #pick a random character
    password+= new_char #adds that random character to the password

    if new_char in digits: # if that random char was a number then "has_number" is true
      has_number= True
    elif new_char in special: #if it was a special char then has_special is true
      has_special= True

    #update the "meets_criteria"  
    meets_criteria = True          #pattern (compound conditional): starting a variable = to true and then trying to prove that it's false
    if numbers:  #checking a few things to set it to false if it is false, otherwise it meets criteria
      meets_criteria= has_number # if we should include a number but we don't have it then meets_criteria is false
    if special_characters:       #if we do have a number then meets_criteria is true
      meets_criteria= meets_criteria and has_special #used "and" because if has_number is false, therefore meets_criteria is false so it won't matter what has_special is, it should return false
  return password                                    #meaning it is gonna be false if we don't have one of the 2 param

min_length= int(input("Enter the minimum length: "))
has_number=input("Do you want to have numbers? (yes/no)").lower()=="yes" #meaning if the user inputs anything other than yes it is gonna be false
has_special=input("Do you want to have special characters? (yes/no)").lower=="yes"
password= generate_password(min_length, has_number, has_special)
print("Your password is: " ,password)


