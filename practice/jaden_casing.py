def toJadenCase(string):
    
    #split string into array
    split_str = string.lower().split(" ")
    #print split_str
    
    #iterate over array
    for word in split_str:
        #uppercase index[0] letter of word
        #print rest of word in lowercase
        upper_letter = word[0].upper()
        complete_sentence = upper_letter + word[1:len(word)].lower()
        #print word[0].upper() + word[1:len(word)]
        #print word.join(" ")
        return complete_sentence

quote = "How can mirrors be real if our eyes aren't real"

print toJadenCase(quote)