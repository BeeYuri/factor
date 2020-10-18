# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:21:10 2020

@author: fluo
"""

import os
import pickle
from pathlib import Path

__all__ = ['local_data']
file_path = '/nfs/BeeYuri/new_factor/new_factor/191data_updating/'
# file_path = str(Path(__file__).parent.joinpath("191data_updating"))
file_list = os.listdir(file_path)

local_data = {}
for file in file_list:
    field = file.replace(".pkl","")
    with open(file_path+'/'+file,'rb') as f:
        data = pickle.load(f)
    local_data[field] = data