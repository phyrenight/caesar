def main():
    lst = []
    sentence = raw_input("Enter a sentence: ")
    if ( len(sentence) == 0):
        print"No string entered."
    else:
        lst = convertToList(sentence)
        print type(lst)
        if type(lst) == 'string':
            print lst
        else:
            print(shift(lst))

def convertToList(sentence):
    if sentence == None or sentence == "":
	    return "No string entered."
    else:
        lst = []
        for items in sentence:
            lst.append(items)
        return	lst	

def shift(lst):
    newSentence = ""
    print type(lst)
    if type(lst) == 'list':
        if len(lst) > 0:
            for items in lst:
                if items.isalpha():
                    num = ord(items)
                    if num == 122:
                        newSentence += chr(97)
                    elif num == 90:
				        newSentence += chr(65)
                    else:
                        newSentence += (chr(num + 1))	 
                else:
                    newSentence += items
            return newSentence
        else:
            return "No string entered."
    else:
	    return "No string entered."
if __name__ == '__main__':
    main()
