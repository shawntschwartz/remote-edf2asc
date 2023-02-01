"""
@Title: example.py
@Author: Shawn T. Schwartz 
@Email: stschwartz@stanford.edu
@Date: 1/30/2023
@Links: https://shawnschwartz.com
@Description: Example using this utility to remotely yank EDFs from an EyeLink Host PC and convert them to plain-text ASCII (ASC) on the fly.
@Notes: Run from within the PsychoPy runner to get the automatic (correct) pylink import (works on MacOS)
"""

import importlib
remote_edf2asc = importlib.import_module("remote-edf2asc")

id = "XXX"

suffix_study_one = ["e1os", "r1os", "r2os", "r3os", "r4os", "r5os"]
suffix_study_two = ["abst", "abte", "acst", "acte", "bcpt", "gts"]

if __name__ == '__main__':
    study_one_fnames = [(id + f + ".EDF") for f in suffix_study_one]

    el_one = remote_edf2asc.RemoteEDF2ASC(
        fname = study_one_fnames,
        asc = True
    )
    
    study_two_fnames = [(id + f + ".EDF") for f in suffix_study_two]
    
    el_two = remote_edf2asc.RemoteEDF2ASC(
        fname = study_two_fnames,
        asc = True
    )
    
    el_one.yank_edf()
    el_two.yank_edf()
