import os
import numpy as np

import utils

def get_log_path(log_name):
    return os.path.join(utils.storage_dir(), "logs", log_name+".txt")

def synthesize(array):
    return np.mean(array), np.std(array), np.amin(array), np.amax(array)

class Logger:
    def __init__(self, log_name):
        self.path = get_log_path(log_name)
    
    def log(self, obj, to_print=True):
        obj_str = str(obj)

        if to_print:
            print(obj_str)

        utils.create_folders_if_necessary(self.path)
        with open(self.path, "a") as f:
            f.write(obj_str+"\n")
