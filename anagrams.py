# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("Yes")
    else:
        print("No")


# driver code
s1 = "Mary"
s2 = "Army"
check(s1, s2)
