swear_list = ["fuck", "cunt"]

user_input = raw_input("What did you say? ")
user_input = user_input.split(" ")

for i in user_input:
    for x in swear_list:
        if x == i:
            user_input = " ".join(user_input)
            print user_input.replace(i, "*" * len(x))
