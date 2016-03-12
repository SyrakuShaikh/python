# Time-stamp: <2016-03-12 Sat 00:12:08 Shaikh>
import os
import sys
import time
import zipfile
from itertools import chain


def zipfs_error(sys_args):
    """Function that deals with ERROR and gets the option.
    """
    opt_num = 0                     # the number of options
    del sys_args[0]                 # remove 0th argument
    for args in sys_args:
        if args.startswith('-'):
            if (args == '-v') | (args == '-q'):
                opt_num += 1
                opts = args          # record the option
            else:
                print("Error! Only \
                '-v for verbose | -q for quiet' \
                are allowed options.")
                quit()
        elif os.path.exists(args):
            source.append(args)
        else:
            print("Error! Wrong arguments : {}".format(args))
            quit()

    # check for multi-options error
    if opt_num > 1:
        print("Error! Multiple Options.")
        quit()
    elif opt_num == 1:
        return opts


def zipfs(source, target, sys_args):
    """Function that zip files inside different directories.
    """
    # Deal with errors and get option
    opts = zipfs_error(sys_args)
    # Create target zip file
    zipf = zipfile.ZipFile(target, 'a', zipfile.ZIP_STORED)
    # First recover every path to its absolute path.
    # Rearrange the files or paths in 'source'.
    for path in source:
        id = source.index(path)
        abs_path = os.path.abspath(path)
        del source[id]
        source.insert(id, abs_path)
    print(os.walk(path) for path in source)

    # Because there may be many files which locate in different
    # directories, the target '.zip' archive needs keep the
    # recursively directory structure.
    com_base = os.path.commonpath(source)
    com_base_len = len(com_base)+1

    # check which option are input.
    if opts == '-q':
        for bases, dirs, files in chain.from_iterable(os.walk(path)
                                                      for path in source):
            for name in files:
                file_t = os.path.join(bases, name)
                file = os.path.abspath(file_t)
                # print(file)
                zipf.write(file, file[com_base_len:])
    elif opts == '-v':
        print('Verbose')
    else:
        print('None')


# 1. The files and directories to be backed up are
# specified in a list.
# Example on Mac OS X and Linux:
source = ['/home/shaikh/Downloads/repo']


# 2. The backup must be stored in a
# main backup directory
# Example on Mac OS X and Linux:
target_dir = '/home/shaikh/Downloads/texnonfreefont'


# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
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


# Run the backup
zipfs(source, target, sys.argv)
# print("Zip command is:")
# print("Running:")
# print('Successful backup to', target)
# print('Backup FAILED!')
# End here.
