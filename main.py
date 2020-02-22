#!/usr/bin/env python3

import argparse
import hashlib
from pathlib import Path


def show_result(original, double):
    """Show the path of the files that already exist.

    :param original list: List with all the files.
    :param double list: List with exclusively the doublon files.
    """
    print("....... {} files founded ........".format(len(original)))
    print("................................")

    if double:
        print('{} files already exist'.format(len(double.keys())))
        for copied_file, original_file in double.items():
            print('original : {} \n---> duplicate : {}'.format(original_file,
                                                              copied_file))
    else:
        print('0 double. Congrats !')


def sha256(filename):
    """Hash the content file.

    :param path str: path to the file.
    :return: Return a byte object.
    """
    # I choose sha256 to maximum avoid hash collision.
    m = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read chunks of 4096 bytes sequentially to be memory efficient.
       for chunk in iter(lambda: f.read(4096), b""):
           m.update(chunk)
    return m.digest()


def analyse_content(gen):
    """Parse the content of all files."""
    all_files = [file for file in gen]
    all_digest = {}
    double = {}

    for file in all_files:
        file_obj = Path(file)

        if file_obj.is_file():
            pathname = file_obj.__str__()
            digest = sha256(pathname)

            if digest not in all_digest.values():
                all_digest[pathname] = digest
            else:
                double[pathname] = next(
					source_path 
					for source_path, source_dig in all_digest.items()
					if digest == source_dig
					)

    show_result(all_files, double)



def main():
    parser = argparse.ArgumentParser(
        prog='DoIexist ?',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""Check if a file already exists.

        examples:
        - Check actual folder and sub directories
        $ ./main.py -r
        - Check files in specific folder
        $ ./main.py --path /home/user/dir
        """)
    parser.add_argument('--path',
                        help='Enter the path where you want to search',
                        type=str)
    parser.add_argument('-r', action='store_true', help='Enable recursivity')
    args = parser.parse_args()
    path = args.path
    recursive = args.r

    # Check the path given by the user.
    if path:
        p = Path(path)
    else:
        p = Path('.')

    # if recursive, we search across all folders from the given path.
    if recursive:
        gen = p.glob('**/*')
    else:
        gen = p.glob('*')

    print('................................')
    print('......... processing ...........')
    print('................................')
    print('......wait for the result.......')
    print('................................')
    analyse_content(gen)


if __name__ == "__main__":
    main()
