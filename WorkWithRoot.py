import sys
sys.path.append('/Applications/root/lib/')

from ROOT import TFile

import numpy as np
import pandas as pd
import rootpy as rp
from rootpy.plotting import Hist, Hist2D, Graph, Efficiency, Legend, Canvas
from rootpy.tree import Tree, TreeModel, FloatCol, IntCol, ShortCol
from rootpy.io import root_open
from rootpy.memory import keepalive

rootfile = rp.io.root_open('ntuple_l1NtupleMC_L1_data3.root')

tree = rootfile.ntupler.tree

nparray = tree.to_array()

np.save('data3.npy', nparray)

print "ready"

# df = pd.DataFrame(nparray)

# df.to_csv("data2.csv")

# f = open("myfile.csv", "w")
# tree.csv(stream = f)