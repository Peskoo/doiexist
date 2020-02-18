#!/usr/bin/env python3
import argparse
from pathlib import Path


def show_analyse_content(double):
    print('------ complete analyse -------')
    print('-------------------------------')
    print('')
    if double:
        for file in double:
            print(file.__str__())
    else:
        print('no double file')

def analyse_content(gen):
    """Parse the content of all files."""
    # TODO // Comment savoir avec quel fichier c'est en double
    all_files = [file for file in gen]
    all_files_content = []
    double = []

    for file in all_files:
        if Path(file).is_file():
            pathname = Path(file).__str__()

            try:
                with open(pathname) as f:
                    lines = [line.rstrip() for line in f]

            except UnicodeDecodeError:
                pass

            finally:
                if lines not in all_files_content:
                    all_files_content.append(lines)
                else:
                    double.append(pathname)

    show_analyse_content(double)


def show_result(original, double):
    """Show the path of the files that already exist.

    :param original list: List with all the files.
    :param double list: List with exclusively the doublon files.
    """
    print("For {} files, you find ...".format(len(original)))

    if double:
        print('{} files already exist'.format(len(double)))
        for file in double:
            print(file.__str__())
    else:
        print('0 double. Congrats !')


def get_all_files(gen):
    """Filter all the existings files in a separate list."""
    all_files = [file for file in gen]
    list_without_double = []
    double = []
    for file in all_files:
        if Path(file).is_file():
            if file not in list_without_double:
                list_without_double.append(file.name)
            else:
                double.append(file)

    show_result(list_without_double, double)


def main():
    parser = argparse.ArgumentParser(
        prog='DoIexist ?',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""Check if a file already exists.

        examples:
        - Check all files from the actual folder
        $ ./main.py -r
        - Check files  in specific folder
        $ ./main.py --path /home/user/dir
        """)
    parser.add_argument('--path',
                        help='Enter the path where you want to search',
                        type=str)
    parser.add_argument('-r', action='store_true', help='Enable recursivity')
    parser.add_argument('-c', action='store_true', help='Check the content')
    args = parser.parse_args()
    path = args.path
    recursive = args.r
    content = args.c

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

    if content:
        analyse_content(gen)
    else:
        get_all_files(gen)



if __name__ == "__main__":
    main()
