import os
import glob
import time
import datetime
from shutil import copy
import json


images = []
videos = []
path = ''
game_list = ''
game_list_dict = {}
subdirectory_paths = []


def get_path():
    global path
    path = input("Enter Path: ") + "/"
    global game_list
    game_list = input("Enter Game List JSON: ")
    with open(game_list, 'r') as f:
        json_str = f.read()
    global game_list_dict
    game_list_dict = json.loads(json_str)
    display_files_in_path(path)


def display_files_in_path(path):
    for entry in glob.glob(path + '*.jpg'):
        images.append(entry)
    for entry in glob.glob(path + '*.mp4'):
        videos.append(entry)
    check_entries()


def check_entries():
    for image in images:
        if image.endswith('_s.jpg') or image.endswith('_c.jpg'):
            copy_old_format_files(image)
        else:
            copy_files(image)

    for video in videos:
        if video.endswith('_s.mp4') or video.endswith('_c.mp4'):
            copy_old_format_files(video)
        else:
            copy_files(video)

def copy_files(file_path):
    file_path_old = file_path.split('-')[-1]
    id_name = os.path.splitext(file_path_old)[0]
    directory = id_name
    new_path = os.path.join(path, directory)
    add_subdirectory_path_to_array(new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path, exist_ok=True)

    file_name = file_path.split('/')[-1]
    if not os.path.exists(new_path + '/' + file_name):
        copy(file_path, new_path + '/' + file_name)
        print("copied " + file_name + " to subdirectory called: " + directory)
    else:
        print("File " + file_name + " already exists in subdirectory")


def copy_old_format_files(file_path):
    directory = 'Unknown'
    new_path = os.path.join(path, directory)#path + directory
    #add_subdirectory_path_to_array(new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path, exist_ok=True)

    file_name = file_path.split('/')[-1]
    if not os.path.exists(new_path + '/' + file_name):
        copy(file_path, new_path + '/' + file_name)
        print("copied " + file_name + " to subdirectory called: " + directory)
    else:
        print("File " + file_name + " already exists in subdirectory")


def add_subdirectory_path_to_array(path):
    global subdirectory_paths
    if path not in subdirectory_paths:
        subdirectory_paths.append(path)
    else:
        print(path + " already exists in subdirectory array")


def create_json():
    for entry in subdirectory_paths:
        path = entry
        for file_path in glob.glob(path + '/' + '*.jpg'):
            file_name_without_extension = os.path.splitext(file_path)[0]
            file = file_name_without_extension.split('/')[-1]


            file_id = file_name_without_extension.split('-')[-1]
            created_time = file.split('-')[0]
            formated_create_time = convert_to_datetime(created_time)


            print(check_game_list(file_id))
            #TODO: create import date variable out of loop so it doesn't need to call every for loop
            json_dict = {
                'id': file_id,
                'fileName': file,
                'type': 'image',
                'game': check_game_list(file_id),
                'importDate': time.time(),
                'takenDate': formated_create_time,
                }

            json_object = json.dumps(json_dict, indent=4)
            with open(file_name_without_extension + '.json', 'w') as outfile:
                outfile.write(json_object)
            print("file " + file_name_without_extension)

        for file_path in glob.glob(path + '/' + '*.mp4'):
            file = file_path.split('/')[-1]
            file_name_without_extension = os.path.splitext(file)[0]

            #file_id = file_name_without_extension.split('-')[-1]
            created_time = file.split('-')[0]
            formated_create_time = convert_to_datetime(created_time)

            json_dict = {
                'id': "null",
                'fileName': file,
                'type': 'image',
                'game': "null",
                'importDate': time.time(),
                'takenDate': formated_create_time,
            }

            json_object = json.dumps(json_dict, indent=4)
            with open(file_name_without_extension + '.json', 'w') as outfile:
                outfile.write(json_object)
            print("file " + file_name_without_extension)

def convert_to_datetime(time):
    return datetime.datetime(int(time[:4]), int(time[4:6]), int(time[6:8]), int(time[8:10]), int(time[10:12]), int(time[12:14]), int(time[14:16])).timestamp()


def check_game_list(game_id):
    id_key = game_id
    if id_key in game_list_dict:
        return game_list_dict[id_key]
    else:
        return "null"

def main():
    get_path()
    time.sleep(0.5)
    create_json()



if __name__ == '__main__':
    main()
