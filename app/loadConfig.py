'''
This script loads the yaml file, which holds all 
configuration information.
'''

import yaml, os

#For Logging
import logging

def load_config(file):
    with open(file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg