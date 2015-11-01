
def main():
   sentence = raw_input("Enter a sentence: ")
   if ( len(sentence) == 0):
       print"No string entered"
   else:
       convertToList(sentence)

def convertToList(sentence):
    list = []
    for items in sentence:
        list.append(items)

    shift(list)

def shift(list):
    newList = []
    for items in list:
         if items.isalpha():
             num = ord(items) + 1
             newList.append(chr(num))	 
         else:
             newList.append(items)
    putIntoAString(newList)
	
def putIntoAString(list):
    newSentence = ""
    for items in list:
        newSentence = newSentence + str(items)
    print newSentence	
			 
        	
	   
if __name__ == "__main__":
    main()