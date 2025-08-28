#MadLib.py
#Name: Meg Aerni
#Date: 8/28/2025
#Assignment: Lab #1

def main():
  print("Madlib")
  #Ask user for words
var1 = input("Name an adjective: ")
var2 = input("Name a verb: ")
var3 = input("Name an animal: ")
var4 = input("Give me a number: ")
var5 = input("Name a place: ")
var6 = input("Name an adjective: ")
  #Print the story with the user supplied words.
print("Once upon a time, there was a " + var1 + " girl who loved to " + var2 + ". One day, while she was " + var2 + "ing, a "
+ var3 + " appeared out of nowhere! The girl shrieked and jumped " + var4 + " feet off the ground. 'Where did you come from?', asked the girl. 'From " + 
var5 + "', the " + var3 + " replied. Despite the initial scare, the girl realized that the " + var3 + 
" was very " + var6 + ", so they became friends and lived happily ever after.")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
