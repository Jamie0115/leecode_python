# string
print("Output #1: {0:s}".format('I\'m enjoying learning Python.'))
print("Output #2: {0:s}".format("This is a long string. Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in the text editor."))
print("Output #3: {0:s}".format('''You can use triple single quotes for multi-line comment strings.'''))
print("Output #4: {0:s}".format("""You can use triple double quotes for multi-line comment strings."""))
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #5: {0:s}".format(sentence))
print("Output #6: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #7: {0:d}".format(m))

# split
string3 = "My deliverable is due in May"
string3_list1 = string3.split()
string3_list2 = string3.split(" ",2)
print("Output #8: {0}".format(string3_list1))
print("Output #9: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
      .format(string3_list2[0], string3_list2[1], string3_list2[2]))
string4 = "My,deliverable,is,due,in,June"
string4_list = string4.split(",")
print("Output #10: {0}".format(string4_list))
print("Output #11: {0} {1} {2}".format(string4_list[1], string4_list[5], string4_list[-1]))

# join


# strip
