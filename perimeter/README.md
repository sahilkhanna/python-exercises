# Provided

A short, straight-forward python program that contains a number of bugs.

# Goal

Fix the bugs in the program and make any other changes to the code that you
think would improve it

# Program purpose

The `perimeter.py` script should read in a list of point coordinates from a
CSV file and then print out the perimeter length of the polygon that is defined
by tracing the points in the listed order.
The polygon defined by the provided points can be irregular and possibly self
intersecting.

# Files

* `perimeter.py`: the buggy python script that needs to be fixed / improved
* `sample_data/*`: Some sample input data CSV files
* `run.sh`: simple bash script to run through all the sample files

# Running instructions

    $ chmod +x ./perimeter.py  # make sure the python file is executable
    $ ./perimeter.py ./sample_data/triangle.csv

To run script over all sample files, you can use the `run.sh` bash script.
