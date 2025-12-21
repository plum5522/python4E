# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end 
# of the line below. 
# Convert the extracted value to a floating point number and print it out.

# text = "X-DSPAM-Confidence:    0.8475"
# pos = text.find('0')
# num = float(text[pos:pos+6])
# print(num)

# *****************************************************************

# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# try:
#     fname = input("Enter file name: ")
#     fh = open(fname)
# except:
#     print("File not found.")
#     quit()

# for line in fh:
#     print(line.rstrip().upper())

# *****************************************************************

# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below. Do not use the sum() 
# function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name

# fname = input("Enter file name: ")
# fh = open(fname)
# average = 0
# count = 0

# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     count += 1
#     pos = line.find('0')
#     average += float(line[pos:pos+6])

# average /= count
# print("Average spam confidence:", average)

# *****************************************************************

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of 
# words using the split() method. The program should build a list of words. For each word on each line 
# check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in 
# the desired output.

# fname = input("Enter file name: ")
# fh = open(fname)

# lst = []

# for line in fh:
#     for word in line.split():
#         if not word in lst:
#             lst.append(word)
# lst.sort()
# print(lst)

# *****************************************************************

# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' 
# like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0

# for line in fh:
#     if not "From " in line:
#         continue
#     print(line.split()[1])
#     count += 1

# print("There were", count, "lines in the file with From as the first word")
