# Author: Javad Amirian
# Email: amiryan.j@gmail.com


import json
import os
import sys

from loaders.loader_eth import load_eth
from loaders.loader_crowds import load_crowds
from loaders.loader_gcs import load_gcs


def load_metafile(opentraj_root, metafile):
    with open(metafile) as json_file:
        data = json.load(json_file)

    loader_name = data['loader']

    if loader_name == "loader_eth":
        traj_dataset = load_eth(os.path.join(opentraj_root, data['data_path']))

    elif loader_name == "loader_gc":
        traj_dataset = load_gcs(os.path.join(opentraj_root, data['data_path']))

    else:
        traj_dataset = None

    return traj_dataset


if __name__ == "__main__":
    opentraj_root = sys.argv[1]

    traj_dataset = load_metafile(opentraj_root, os.path.join(opentraj_root, "datasets/ETH/ETH.json"))
    if traj_dataset:
        print(traj_dataset.get_agent_ids())