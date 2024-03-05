"""
@Title: example.py
@Author: Shawn T. Schwartz 
@Email: stschwartz@stanford.edu
@Date: 3/5/2024
@Links: https://shawnschwartz.com
@Description: Example file to remotely yank EDFs from an EyeLink Host PC and convert them to plain-text ASCII (ASC) on the fly.
"""

import argparse, importlib
from os.path import expanduser, join
from shutil import move

remote_edf2asc = importlib.import_module("remote-edf2asc")

parser = argparse.ArgumentParser(prog='remote-edf2asc',
                                 description='automatically yank and convert EDF files to ASC from EyeLink Host PC')
parser.add_argument('-p', type=str, action='store', help='participant id')
parser.add_argument('-f', default='all', type=str, action='store', help='yank `all` EDF files or just a specific one')
parser.add_argument('-d', default='stmw', type=str, action='store', help='destination for the downloaded files, defaults to `stmw`')
parser.add_argument('-s', default='mw', type=str, action='store', help='EDF filename suffix, defaults to `mw`')
args = parser.parse_args()

id = args.p

if args.f == 'all':
    prefixes = ["st1", "te1", "st2", "te2", "st3", "te3", "st4", "te4"]
else:
    prefixes = [args.f]

if __name__ == '__main__':
    fnames = [(id + f + args.s + '.EDF') for f in prefixes]

    edf2asc = remote_edf2asc.RemoteEDF2ASC(
        fname = fnames,
        asc = True
    )
    
    edf2asc.yank_edf()
    
    for file in fnames:
        for ext in ['EDF', 'asc']:
            src = join('yanked_edfs', file[:-4] + '.' + ext)
            dst = join(expanduser('~'), 'Desktop', args.d, 'data', id, 'eyetracking')
            move(src, dst)
