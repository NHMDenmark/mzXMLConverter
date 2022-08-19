# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:29:00 2022

@author: Kim Steenstrup Pedersen, NHMD

Copyright 2022 Natural History Museum of Denmark (NHMD)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
from pyteomics import mzxml  #, auxiliary
import pandas as pd
from pathlib import Path


def prepare_dataframe(mz_list, intensity_list):
    record = pd.DataFrame({
        "m/z": mz_list,
        "intensity": intensity_list
    })
    return record

def main():
    """The main function of this script."""
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser(description="Convert mzXML files to simple two column text files.")
    ap.add_argument("-i", "--input", required=True, action="extend", nargs="+", type=str,
                    help="file name for and path to input image")
    ap.add_argument("-o", "--output", required=False, default="output",
                    help="path and filename for output text file (tab separated CSV).")
    ap.add_argument("-v", "--verbose", required=False, action='store_true', default=False,
                    help="If set the program is verbose and will print out debug information")

    args = vars(ap.parse_args())


    # Loop over a list of images
    for inputfilename in args["input"]:
        with mzxml.read(inputfilename) as reader:
            try:
                counter = 0
                while True: # Loop over all items in the mzXML file
                    next_item = next(reader)
                    #auxiliary.print_tree(next_item)

                    # Prepare Pandas dataframe for output
                    df = prepare_dataframe(next_item["m/z array"], next_item["intensity array"])
                    #print(df.head())

                    # Write CSV file with TAB as separator
                    outpath = Path(args["output"]).joinpath(Path(Path(inputfilename).name).stem +  "_Files" + str(counter) + ".txt")
                    print(str(outpath))
                    # TODO: Remember to write out float numbers with 6 decimals
                    df.to_csv(str(outpath), sep="\t", header=False, index=False)

                    counter += 1
            except StopIteration:
                print("End of file")


if __name__ == '__main__':
    main()


