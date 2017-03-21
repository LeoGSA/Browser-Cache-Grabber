# -*- coding: utf-8 -*-
# © LeoGSA - Sergey Grigoriev (leogsa@gmail.com)

## Mozilla (or any other browser) cache grabber by LeoGSA (leogsa@gmail.com)
##
## A tiny, but very usefull programm for grabbing cache folders of different browsers.
## It also can be used for file recovery processes, when you need to sort files with lost extentions.
##
## There are a few configuration parameters.

# EXPLANATIONS:

# from_folder:
# in from_folder specify the cache folder of your browser OR folder, containing files without extentions - do not put '/' at the end
# RUSSIAN: указывать без слеша в конце Ваня комп

# to_folder:
# to_folder - is the destination folder - the place where you want your recognized files - do not put '/' at the end
# RUSSIAN: указывать без слеша в конце  'I:/30'

# min_size:
# min_size - minimal file-size (in bits) in cache which you are interested in (files of smaller size than this will be deleted without analysis)
# RUSSIAN:минимальный размер файла в кэше (которые нас интересуют) 26000

# folder_list:
# in folder_list leave only those elements which you are interested in, always leave the fist blank element
# (file types which are not in this list will not be recognized)
# This is the example of maximum availiable list for the moment:
# folder_list = ['','/jpg',"/png","/gif_87","/gif_89","/video","/music",'/html',"/doc","/pdf","/zip", '/ico']
# At the monent:
# "/music" means .mp3 files
# "/video" means .mp4 .avi and .flv files
# e.g. if you want .mp3 and .jpg to be grabbed, your folder_list should be: folder_list = ['','/jpg',"/music"]

# save_unknown
# if this option is set to True, unknown (unrecognized) files with size
# bigger than min_size will be put to to_folder directly

# print_unknown_header:
# if this option is set to True, unknown file headers will be printed during execution

# clear_from_folder_afterall:
# deletes and re-creates (clesrs) from_folder after all work is done

from_folder='c:/Users/Ivan/AppData/Local/Mozilla/Firefox/Profiles/kp10flzc.default-1466620470116/cache2/entries'
# from_folder='i:/66'
to_folder='i:/30-new'
min_size=26000
folder_list = ['','/jpg',"/png","/gif_87","/gif_89","/video"]
# folder_list = ['',"/video",'/jpg']
save_unknown = True
print_unknown_header = False
clear_from_folder_afterall = True

#
# NO USER SERVICEABLE PARTS BELOW HERE...
#

import os
import shutil
import sys
from Magic_numbers import full_matrix
import binascii
import re

def make_folders(folder_list, to_folder):
    for i in folder_list:
        if os.path.isdir (to_folder+i)==False:
            os.mkdir (to_folder+i)

def analize_files(from_folder, folder_list):
    temp_matrix=[]
    for i in full_matrix:
        if i[0] in folder_list:
            temp_matrix.append(i)

    file_list=(d for d in os.listdir(from_folder))

    for i in file_list:
        if (os.path.getsize(from_folder+"/"+i))>min_size:
            with open (from_folder+"/"+i, "rb") as myfile:
                header=myfile.read(24)
                header = str(binascii.hexlify(header))[2:-1]
                # print (header)
            for y in temp_matrix:
                if re.match(y[1], header):
                    shutil.move (from_folder+"/"+i,to_folder+y[2]+i+y[3])
                    not_recognized = False
                    break
                not_recognized = True
            if not_recognized and print_unknown_header:
                print (header)
            if not_recognized and save_unknown:
                shutil.move (from_folder+"/"+i,to_folder+"/"+i)

def del_and_create_from_folder(from_folder):
    shutil.rmtree(from_folder)
    assert(os.path.isdir(from_folder) == False)
    os.mkdir (from_folder)

if __name__ == '__main__':
    print ("Started")
    make_folders(folder_list=folder_list, to_folder=to_folder)
    analize_files(from_folder=from_folder, folder_list=folder_list)
    if clear_from_folder_afterall:
        del_and_create_from_folder(from_folder=from_folder)
    print ("Done!")
