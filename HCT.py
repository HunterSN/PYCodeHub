from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import csv


%matplotlib inline
np.set_printoptions(precision=5, suppress=True)

inputt = open("gscy.csv")

