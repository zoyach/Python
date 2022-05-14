greeting = "Hello!"
name = "John"
print(greeting + name)

#string Index
print(name[0])
print(name[1])
print(name[2])
print(name[3])

#String Slicing
# A string in Python can be sliced for getting a part of the string.
print(name[0:3])
print(name[:3])
print(name[0:])

''' Negative Indices:
 Negative indices can also be used.
  -1 corresponds to the (length-1) index, -2 to (length-2).'''
  
print(name[-4:-1])     #same as name[1:4]

#Slicing with skip value
# We can provide a skip value as a part of our slice like this:
name = "Fatima"
print(name[0::1])
print(name[0::2])
print(name[0::3])

#String Functions
story = '''once upon a time somewhere in a village, there was a farmer live.the farmer everday went
 to the nearby town for his business'''

 #1.len() function : It returns the length of the string.
print(len(story))
#2.endswith(“ss”) : This function tells whether the variable string ends with the string “ss”
print(story.endswith("ss"))  #return true or false
#3.count(“c”) : It counts the total number of occurrences of any character or string.
print(story.count("a"))
#4.capitalize() : This function capitalizes the first character of a given string.
print(story.capitalize())
#5.find(word) : This function finds a word and returns the index of first occurrence
#  of that word in the string.
print(story.find("the"))





