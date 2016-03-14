# Time-stamp: <2016-03-14 Mon 20:09:56 Shaikh>
poem = """\
Programming is fun
When the work is done
if you wanna make your work also fun
    use Python!
"""


# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a new line
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()
