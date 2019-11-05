# CMS-ME0-upgrade
## Data
Root data can be transformed into numpy file using WorkWithRoot.py, which needs ROOT and rootpy installed in your environment. Also it's only usable in python2.

## Processing
Data processing is done in the jupyter notebook files. Details of model tuning not included.

The heavy-weight portion of the project is understanding and manipulating the complicated data structure. Model proformance have much to be desired.

Working with ROOT files in python does not have much material to reference. I hope this project can be of help to those who wants to quickly bridge the gap between ROOT and Python in their workflow.

## Special notice
In theory, the feature "vp_pt", aka the pt of gen particles, would always have a value. But in my data, there is a null value in all the 500000 events. I assume this is a result of a bug in the simulation process. Using my method of vstack all events, the missing value can be easily omitted, leaving the whole dataset misalign. The little bug left my models underperform for months.
