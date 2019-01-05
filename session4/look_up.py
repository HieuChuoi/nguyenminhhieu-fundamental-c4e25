dictionary = {
    "hello" : "chao",
    "goodbye" : "tam biet",
    "football" : "bong da",
    "study" : "hoc",
    "home" : "nha",
    "parent": "bo me"
}
n = input("Enter english word: ")

# while True:
#     if n not in dictionary:
#         print("Invalid Word")
#         n = input("Enter english word: ")
#     else:
#         print("English: ", n) 
#         print("Vietnamese: ",dictionary[n])
#         n = input("Enter english word: ")


if n in dictionary:
    print("English: ", n)
    print("Vietnamese: ",dictionary[n])
    upd = input("Do you want to update(Y/N) ?")
    if upd == "N":
        n = input("Enter english word: ")
    elif upd == "Y":
        new_trans = input("Enter new translation: ")
        dictionary[n] = new_trans
        print(dictionary)
        print("English: ", n)
        print("Vietnamese: ",dictionary[n])
elif n not in dictionary:
    print("Word doesnt exist",end='')
    con = input("Do you want to contribute(Y/N)?" )
    if con == "Y":
        new_word = input("Enter Your Word: ")
        new_translate = input("Enter Your Translation: ")
        dictionary[new_word] = new_translate
        print("English: ", n)
        print("Vietnamese: ",dictionary[n])
    elif con == "N":
        n = input("Enter english word: ")
    else:
        pass
else:
    pass