import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv("./csv_files/sp_500_stocks.csv")