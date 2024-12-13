def checkPalindrome():
    string = input("enter a word: ")
    rev_string = string[::-1]
    if string == rev_string:
        print("word is a palindrom!")
    else:
        print("the word is not a palindrome")
checkPalindrome()