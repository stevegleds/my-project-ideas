from sys import argv
from os.path import exists

"""
A Python script to take the content of a file containing skype chat and producing a file without date and time stamps
"""

"""
You should immediately notice that we import another handy command named exists. This returns True if a
file exists, based on its name in a string as an argument. It returns False if not. Weâ??ll be using this function in the
second half of this book to do lots of things, but right now you should see how you can import it.
"""

script, from_file, to_file = argv

def print_all(f):
	print(f.read())
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print("line:", line_count, "contains:", f.readline())

print("Copying from {} to {}" .format(from_file, to_file))

# we can do these 2 on one line - how?
input = open(from_file)
indata = input.read()
print("The input file is {} bytes long" .format(len(indata)))

print("Does the output file exist? {}" .format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input() not sure what this was supposed to do but it broke the script
output = open(to_file, 'w')
output.write(indata) 
print(indata)

print("Alright, all done.")

output.close()
input.close()

current_file = open(from_file)

print("First, let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
print("looping")
for line in range(1, 4):
	print_a_line(line, current_file)
	
