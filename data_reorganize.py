# import the basic libraries
import os
import re
import cv2
import glob
import shutil
import random
import numpy as np
from shutil import copyfile
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the neccesary paths
from DATA_PATH import RED_EDGE_DICT_PATHS
INPUT_DATAPATH = RED_EDGE_DICT_PATHS["RED_EDGE_INPUT_PATH"]
OUTPUT_DATAPATH = RED_EDGE_DICT_PATHS["RED_EDGE_OUTPUT_PATH_3CH"]

# LIST ORTHOMOSAIC MAPS CONVENTION
LIST_ORTHO_TRAIN = ["000", "001", "002", "004"]
LIST_ORTHO_TEST = ["003"]


def orderListPaths(paths):
    paths.sort(key=lambda var: [int(x) if x.isdigit() else x
                                for x in re.findall(r'[^0-9]|[0-9]+', var)])
    return paths


def join_paths(LIST_ORTHO):

    images = list()
    labels = list()

    for ortho_folder in LIST_ORTHO:
        # read an orthomosaic folder and extract the tiles and the labels.
        groundtruth_paths_n = list(glob.glob(
            os.path.join(INPUT_DATAPATH,
                         ortho_folder,
                         "groundtruth",
                         "*GroundTruth_color.png")
        ))

        tiles_paths_n = list(glob.glob(
            os.path.join(INPUT_DATAPATH,
                         ortho_folder,
                         "tile/CIR",
                         "*.png")
        ))

        # order the lists
        groundtruth_paths_n = orderListPaths(groundtruth_paths_n)
        tiles_paths_n = orderListPaths(tiles_paths_n)

        # concatenate the lists
        images += tiles_paths_n
        labels += groundtruth_paths_n

    return images, labels


TRAIN_IMAGES_FULL, TRAIN_LABELS_FULL = join_paths(LIST_ORTHO_TRAIN)
X_TEST, Y_TEST = join_paths(LIST_ORTHO_TEST)

X_TRAIN, X_VAL, Y_TRAIN, Y_VAL = train_test_split(
    TRAIN_IMAGES_FULL, TRAIN_LABELS_FULL, test_size=0.2, random_state=42)

# take the paths and save in the output folders


def save_data(images, labels, folder="train"):
    ID = 0
    for i in range(len(images)):
        copyfile(images[i], os.path.join(OUTPUT_DATAPATH,
                                         folder, "images", "frame_" + str(ID) + ".png"))
        copyfile(labels[i], os.path.join(OUTPUT_DATAPATH,
                                         folder, "labels",  "label_" + str(ID) + ".png"))
        ID += 1


save_data(X_TRAIN, Y_TRAIN)
save_data(X_VAL, Y_VAL, folder="val")
save_data(X_TEST, Y_TEST, folder="test")
