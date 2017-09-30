# Stride.py
-----------

A simple Python wrapper for STRIDE, a knowledge-Based protein secondary structure assignment algorithm.
The Stride binary is required and it can be found here: http://webclu.bio.wzw.tum.de/stride/

Usage
-----

Here is a simple example:

``` Python
    stride = Stride()
    stride.set_input_file("1crn.pdb")
    stride.change_path("/home/h3nnn4n/Downloads/stride") # Path to the Stride binary
    stride.assign()
    print("".join(stride.get_ss()))

```

LICENSE
-------

Checkout the LICENSE file.
