#!/usr/bin/env python3

import argparse
import hashlib
import multiprocessing 
from pathlib import Path


DIGEST = {}


def show_result(flipped):
    """Show the path of the files that already exist.

    :param flipped dict: each values are lists with duplicates files.
    """
    print("....... {} files founded ........".format(len(DIGEST.keys())))
    print("................................")

    for k, v in flipped.items():
        if len(v) > 1:
            print('Duplicate files founded :')
            for f in v:
                print(' - ',f)
    print(".............done................")


def comparate_digest():
    """Check and return duplicates files."""
    flipped = {}

    for key, value in DIGEST.items():
        print(key)
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key) 

    show_result(flipped)


def sha256(path):
    """Hash the content file.

    :param path str: path to the file.
    """
    # I choose sha256 to maximum avoid hash collision.
    m = hashlib.sha256()
    with open(path, "rb") as f:
        # Read chunks of 4096 bytes sequentially to be memory efficient.
       for chunk in iter(lambda: f.read(4096), b""):
           m.update(chunk)
    DIGEST[path] = m.digest()


def analyse_content(gen):
    """Execute hash for each selected files."""
    all_files = [file for file in gen]

    for file in all_files:
        file_obj = Path(file)

        if file_obj.is_file():
            pathname = file_obj.__str__()
            pr = multiprocessing.Process(target=sha256, args=(pathname,))
            pr.start()

    pr.join()
    comparate_digest()


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
