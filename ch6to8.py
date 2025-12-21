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

# *****************************************************************

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the 
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.

# fn = input("Enter file:")
# if len(fn) < 1:
#     fn = "mbox-short.txt"
# fh = open(fn)
# count_name = dict()

# for line in fh:
#     if "From " not in line:
#         continue
#     name = line.split()[1]
#     count_name[name] = count_name.get(name, 0) + 1

# max_count = None
# max_name = None

# for name in count_name:
#     if max_count is None or count_name[name] > max_count:
#         max_count = count_name[name]
#         max_name = name
    
# print(max_name, max_count)

# *****************************************************************

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of 
# the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# fn = input("Enter file:")
# if len(fn) < 1:
#     fn = "mbox-short.txt"
# fh = open(fn)

# hour_count = dict()

# for line in fh:
#     if "From " not in line:
#         continue
#     pos = line.find(':')
#     hour = line[pos-2:pos]
#     hour_count[hour] = hour_count.get(hour, 0) + 1

# sort_list = list()

# for k,v in hour_count.items():
#     sort_list.append((k,v))

# sort_list.sort()

# for v,k in sort_list:
#     print(v, k)