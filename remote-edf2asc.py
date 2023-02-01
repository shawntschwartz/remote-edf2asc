"""
@Title: remote-edf2asc.py
@Author: Shawn T. Schwartz 
@Email: stschwartz@stanford.edu
@Date: 1/30/2023
@Links: https://shawnschwartz.com
@Description: A utility to remotely yank EDFs from an EyeLink Host PC and convert them to plain-text ASCII (ASC) on the fly.
@Notes: Run from within the PsychoPy runner to get the automatic (correct) pylink import (works on MacOS)
"""

import os, time, subprocess, pylink

class RemoteEDF2ASC():
    '''
        fname -- can be a string or list of string names to yank as many files as desired
    '''
    def __init__(self, fname, asc=True):   
        self.fname = fname
        self.asc = asc
        self.ip = '100.1.1.1'
        self.download_dir = 'yanked_edfs'
        
    def _connect_eyelink(self):
        try:
            self.el_tracker = pylink.EyeLink(self.ip)
        except RuntimeError as error:
            print('ERROR:', error)
            
    def _disconnect_eyelink(self):
        if self.el_tracker.isConnected():
            time.sleep(.1)
            self.el_tracker.close()
        
    def _download_edf(self, fname):
        host_edf = fname
        local_edf = os.path.join(self.download_dir, fname)
        
        try:
            print("trying download of " + host_edf)
            self.el_tracker.receiveDataFile(host_edf, local_edf)
            print("success!")
        except RuntimeError as error:
            print('ERROR:', error)
            
    def _edf2asc(self, fname):
        os.chdir('utils')
        subprocess.run(["edf2asc", os.path.join("..", self.download_dir, fname)])
        os.chdir('..')
            
    def yank_edf(self):
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
   
        self._connect_eyelink()
        
        if isinstance(self.fname, str):
            files = []
            files.append(self.fname)
        else:
            files = self.fname
        
        for file in files:
            self._download_edf(file)
            
            if self.asc:
                self._edf2asc(file)
        
        self._disconnect_eyelink()
        
        print("done!")
