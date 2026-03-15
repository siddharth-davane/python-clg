string = input("Enter a string: ")
substr = input("Enter substring: ")

length = len(string)
reverse = string[::-1]

print("Length of string: ", length)
print("Reversed String: ", reverse)

if string == reverse:
    print("This String is a paliondrome")
else:
    print("This string is not a palindrome")

if substr in string:
    print("Substring is present")
else:
    print("substring is absent")

string2 = input("Enter 2nd string: ")
if string == string2:
    print("Strings are identical")
else:
    print("Strings are not identical")
