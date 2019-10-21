import datetime
import pandas as pd
import geopandas as gp
import numpy as np
import zipfile
import os
import matplotlib.pyplot as plt

# Analytical
#import networkx as nx
#import community

today = datetime.datetime.today()
today_str = "_".join([str(x) for x in [today.day, today.month, today.year]])

cwd = os.path.dirname(os.getcwd())

data_dir = os.path.join(cwd, 'data')
processed_dir = os.path.join(data_dir, 'processed')
shapefile_dir = os.path.join(data_dir, 'shapefiles')
denue_dir = os.path.join(data_dir, 'denue') 

reports_dir = os.path.join(cwd, 'reports')
fig_dir = os.path.join(reports_dir, 'figures')

data_dir = os.path.join(cwd, 'data')
denue_dir = os.path.join(data_dir, 'denue') 
