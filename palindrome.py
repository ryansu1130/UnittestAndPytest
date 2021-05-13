
def testPalindrome(userString):
    tempstring = userString
    k = len(userString)

    for i in range(0,len(userString)):
        if userString[i] == tempstring[k - 1]:
            k -= 1
            if k == 0:
                print("Yes, The String Is A Palindrome")
                print("===============================")
        else:
            print("No, The String Is Not A Palindrome")
            print("==================================")
            break
    return

userString = input("Enter a string:" )

testPalindrome(userString)
