'''''
Program : Program to traslate words from English to Spanish and Vice-versa
Author : Monika Adhikari

Description: The program prompts the user for a word and checks in the dictionary for english or spanish word. If the word found
then we display the translated word engish to spanish and vice versa. If the word is not in the dictionary, we are giving the option to the user to 
add the word in the given language. If the user gives blank input , it will exit from the code
'''


### Program

print("Program to translate words from English to Spanish and Vice-versa \n")


###  Language Dictionary

word_translation={}
word_translation["cat"]={"spanish":"gato"}
word_translation["gato"]={"english":"cat"}
word_translation["dog"]={"spanish":"perro"}
word_translation["perro"]={"english":"dog"}
word_translation["hello"]={"spanish":"hola"}
word_translation["hola"]={"english":"hello"}
word_translation["goodbye"]={"spanish":"adios"}
word_translation["adios"]={"english":"goodbye"}
word_translation["love"]={"spanish":"amor"}
word_translation["amor"]={"english":"love"}
word_translation["boy"]={"spanish":"chico"}
word_translation["chico"]={"english":"boy"}
word_translation["girl"]={"spanish":"chica"}
word_translation["chica"]={"english":"girl"}
word_translation["sun"]={"spanish":"sol"}
word_translation["sol"]={"engish":"sun"}
word_translation["moon"]={"spanish":"luna"}
word_translation["luna"]={"english":"moon"}




##Data Gathering

while True:
    word=input("Enter an English or Spanish word to translate: ")
    word=word.lower()
    ## if input is Null  then ex
    if word=="":
        print("Exiting ...")
        break
        
    
        
    if word in word_translation.keys():

        if "spanish" in word_translation[word.lower()].keys():

          print(f'The English word {word} is {word_translation[word.lower()]["spanish"]} in Spanish')

        else:
          print(f"The Spanish word {word} is {word_translation[word.lower()]['english']} in English")
          
        
        
## if word not in Spanish and English then Add
    else:
        print(f"The word {word} was not found in English or Spanish word lists")
        till_correct_y_n=True
        while till_correct_y_n:
            print(f"Would you like to add {word} to the lists? <y>es or <n>o ",end="")
            choice=input()
            
        
            ## user don't want to add word
            if choice.lower()=='n':
                till_correct_y_n=False
                
            
            
             ## user want to add word
            elif choice.lower()=='y':
                print(f"What language is {word} in <E>nglish or <S>panish ",end="")
                lang_choice=input()
           
            
            ## User want to add english Word
                if lang_choice.lower()=='e':
                    word_translation[word.lower()]={}
                    lang_input=input(f"what is Spanish word for '{word}'")
                    word_translation[word.lower()].update({"spanish":lang_input})
                    till_correct_y_n=False
                    
             ## User want to add spanish Word
                elif lang_choice=='s':
                    word_translation[word.lower()]={}
                    lang_input=input(f"what is English word for '{word}' ")
                    word_translation[word.lower()].update({"english":lang_input})
                    till_correct_y_n=False
                else:
                    print("you have to choose between English or Spanish")
            
            else:
                print("You entered wrong input. You have to choose between yes or no")
                
            
        
    








    
