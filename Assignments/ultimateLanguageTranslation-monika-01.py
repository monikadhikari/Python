'''
Program : Program to traslate words from English to Spanish and Vice-versa using file
Author : Monika Adhikari
Description : The program prompts the user to translate a word from english to spanish and vice versa. In this program,we are using text file.
First the program read the file and save the file data into a data variable.Then take an input word from the user and prompt the translated word.
If the word is not found in the file, we will write the translated word into the file by taking the input from the user.With the help of file, program can
persist the data for the next run. 
'''


print("Program to translate words from English to Spanish and Vice-versa \n")

## Read file funtion 
def readfile():
    with open ("vocabulary.txt",'r') as f:
        data = f.readlines()
        return  [i.split() for i in data]
        
        
    
        
def writeFile(data,english,spanish):

  with open ("vocabulary.txt",'w') as f:
    for item in data:
      f.write(f"{item[0]} {item[1]}\n")
    f.write(f"{english} {spanish}\n")



## reading data first Time    
data=readfile()



while True:
    word=input("Enter an English or Spanish word to translate: ")
    word=word.lower()
    ## if input is Null  then ex
    if word=="":
        print("Exiting ...")
        break
 # If word in english   
    word_found_in_vocab=False
    for index,item in enumerate(data):
      if word ==item[0]: ## word found in english
        print(f"The English word '{word}' is '{item[1]}' in Spanish")
        word_found_in_vocab=True
        break
      if word == item[1]: ## word found in spanish
        print(f"The Spanish word '{word}' is '{item[0]}'' in English")
        word_found_in_vocab=True
        break
        
## if word not in Spanish and English then Add

    if not word_found_in_vocab:
      print(f"The word '{word}' was not found in English or Spanish word lists")

      input_choice_y_n=True
      while input_choice_y_n:
          print(f"Would you like to add '{word}' to the lists? <y>es or <n>o ",end="")
          choice=input()
        
        ## user don't want to add word
          if choice.lower()=='n':
              input_choice_y_n=False
              
          
          
            ## user want to add word
          elif choice.lower()=='y':
              print(f"What language is '{word}' in <E>nglish or <S>panish ",end="")
              lang_choice=input()
              #             ## User want to add english Word
              if lang_choice.lower()=='e':
                  lang_input=input(f"what is Spanish word for '{word}' ")
                  writeFile(data,english=word,spanish=lang_input)
                  data=readfile()
                  input_choice_y_n=False
                  
            ## User want to add spanish Word
              elif lang_choice=='s':
                  lang_input=input("what is english word for '{word}' ")
                  writeFile(data,english=lang_input,spanish=word)
                  data=readfile()
                  input_choice_y_n=False
              else:
                  print("you have to choose between English or Spanish")

          else:
                print("You entered wrong input. You have to choose between yes or no")
                
            
        
    

