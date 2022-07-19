# File handling
import argparse
import pathlib

# Simply sets all CLI arguements
def __get_args():
    passArgs = argparse.ArgumentParser()
    passArgs.add_argument(
        '-file', '-f',
        help='The exact filename you want to parse',
        action='store',
        default='*.txt',
        type=open
        )
    passArgs.add_argument(
        '-path', '-p',
        help='The actual path to the file you want to parse',
        action='store',
        type=pathlib.Path
        )
    passArgs.add_argument(
        '-debug', '-d',
        help='Intended to enable debugging functions',
        action='store_true',
        default=False,
        type=bool
        )
    passArgs.add_argument(
        '-modded_file', '-MOD',
        help='The file name you wish to use for your mod',
        action='store',
        default=passArgs.parse_args(['-file']) + 'modded',
        type=argparse.FileType('w+', encoding=('UTF-8'))
    )

    CommandLineArgs = passArgs.parse_args()

    return CommandLineArgs

CommandLine = __get_args()