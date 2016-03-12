# Time-stamp: <2016-03-11 Fri 10:49:02 Shaikh>
import os
import time


# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/home/shaikh/Downloads/repo']
# Notice we had to use double quotes inside the string
# for names with spaces in it.


# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/home/shaikh/Downloads/texnonfreefont'
# Remember to change this to which folder you will be using


# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
# today = target_dir + os.sep + time.strftime('%Y%m%d')
# # The current is the name of the zip archive.
# now = time.strftime('%H%M%S')

# # The name of the zip file
# target = today + os.sep + now + '.zip'
# join() method version?
target_seq = [
    target_dir,
    os.sep,
    time.strftime('%Y%m%d'),
    os.sep,
    time.strftime('%H%M%S'),
    '.zip'
]
today = ''.join(target_seq[:-3])
now = ''.join(target_seq[-2:])


# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) is 0:
    target = ''.join(target_seq)
else:
    target = ''.join(target_seq[:-1]) + '_' + \
             comment.replace(' ', '_') + '.zip'


# Create target directory if it is not present
if not os.path.exists(today):
    os.mkdir(today)        # make directory
    print('Successfully created directory', today)


# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target,
                                      ' '.join(source))


# Run the backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED!')
# End here.
