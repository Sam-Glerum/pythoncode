def palindrome(s):
	split_string = s.split(" ")

	for word in split_string:
		print word[::-1]


palindrome("fuck yeah racecar")

'''
def longest_palindrome (s):

    #convert string to list, which enables us to check invidual words
    split_string = s.split(" ")
    if len(s) <= 0:
        return 0

    else:
        for word in split_string:
            #check if word is a palindrome
            if word == word[::-1] and len(word) > 0:
                print word
                return len(word)
            else:
                return len(word) - 1

    pass
'''
