'''
Program : Program to traslate words from English to Spanish and Vice-versa
Author : Monika Adhikari
Description : The program prompts the user for a word then check if word is in english list using index and then compute index to find the corresponding word in Spanish
otherwise check if the words is in spanish and repeat the last step by computing the index in the spanish list,finding it in english list and printing it.
otherwise if the word is in niether of the list print a message saying it could not be found.



'''


### Program

print("Program to translate words from English to Spanish and Vice-versa \n")


###  Language List
english=['cat','dog','hello','goodbye','love','boy','girl','sun','moon']
spanish=['gato','perro','hola','adios','amor','chico','chica','sol','luna']


##Data Gathering

while True:
    word=input("Enter an English or Spanish word to translate: ")
    word=word.lower()
    ## if input is Null  then ex
    if word=="":
        print("Exiting ...")
        break
 ## If word in english   
    if word in english:
        index=english.index(word)
        translated_word=spanish[index]
        print("The English word '{}' is '{}' in Spanish".format(word,translated_word))
        
## if word in spanish
    elif word in spanish:
        index=spanish.index(word)
        translated_word=english[index]
        print("The Spanish word '{}' is '{}' in English".format(word,translated_word))
        
## if word not in Spanish and English then Add
    else:
        print("The word '{}' was not found in English or Spanish word lists".format(word))
        till_correct_y_n=True
        while till_correct_y_n:
            print("Would you like to add {} to the lists? <y>es or <n>o ".format(word),end="")
            choice=input()
            
            
        
            ## user don't want to add word
            if choice.lower()=='n':
                till_correct_y_n=False
                
            
            
             ## user want to add word
            elif choice.lower()=='y':
                print("What language is {} in <E>nglish or <S>panish ".format(word),end="")
                lang_choice=input()
           
            
            ## User want to add english Word
                if lang_choice.lower()=='e':
                    english.append(word)
                    lang_input=input("what is Spanish word for '{}' ".format(word))
                    spanish.append(lang_input)
                    till_correct_y_n=False
                    
             ## User want to add spanish Word
                elif lang_choice=='s':
                    spanish.append(word)
                    lang_input=input("what is english word for '{}' ".format(word))
                    english.append(lang_input)
                    till_correct_y_n=False
                else:
                    print("you have to choose between English or Spanish")
            
            else:
                print("You entered wrong input. You have to choose between yes or no")
                
            
        
    








    