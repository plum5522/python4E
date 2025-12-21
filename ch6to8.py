# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end 
# of the line below. 
# Convert the extracted value to a floating point number and print it out.

# text = "X-DSPAM-Confidence:    0.8475"
# pos = text.find('0')
# num = float(text[pos:pos+6])
# print(num)

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