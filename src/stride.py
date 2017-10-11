#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import re
import os
import sys
import string
import random
import subprocess


class Stride():
    input_file = ""
    output_file = None
    path = None
    binary = "stride"
    binpath = None
    ss = []

    remove_files = True

    def __init__(self, input_file=None, output_file=None):
        if input_file is not None:
            self.input_file = input_file

        if output_file is not None:
            self.remove_files = False
            self.output_file = output_file

        if self.path is not None and self.binary is not None:
            self.binpath = self.path + "/" + self.binary

    def change_path(self, path):
        self.path = path
        if self.path is not None and self.binary is not None:
            self.binpath = self.path + "/" + self.binary

    def change_binary(self, name):
        self.binary = name
        if self.path is not None and self.binary is not None:
            self.binpath = self.path + "/" + self.binary

    def set_input_file(self, name):
        self.input_file = name

    def assign(self):
        if self.output_file is None:
            def randomword(length):
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(length))

            self.output_file = randomword(32)
        else:
            self.remove_files = False

        subprocess.call([self.binpath, self.input_file, "-f" + self.output_file])

        with open(self.output_file, "r") as f:
            self.ss = []
            while True:
                line = f.readline()

                if line == "":
                    break

                line = re.sub("\s\s+", " ", line)
                tokens = line.split(" ")

                if tokens[0] == "REM":
                    continue
                elif tokens[0] == "ASG":
                    self.ss.append(tokens[5])

        if self.remove_files:
            os.remove(self.output_file)

    def get_ss(self):
        return self.ss


if __name__ == "__main__":
    stride = Stride()
    stride.set_input_file("1crn.pdb")
    stride.change_path("/home/h3nnn4n/Downloads/stride")
    stride.assign()
    print("".join(stride.get_ss()))
