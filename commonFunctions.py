# Main import module
#def mainImport():
#  import pandas
#  import numpy as np
#  from scipy.spatial import distance

# Functions to read datafiles:
# Output will always be an array with columns frame - x - y - intensity
# Input can be ThunderSTORM file (readCSV) or rapidSTORM file (readTXT)
def readCSV(filename):
  import pandas
  #Determine which fields we want to read
  fields = ['x [nm]', 'y [nm]','frame', 'intensity [photon]']

  #Find those headers
  dataheaders = pandas.read_csv(filename, nrows=1)
  #Read the csv with only those headers
  data = pandas.read_csv(filename, header=None, skiprows=1, usecols=[1,2,3,5])
  #Convert the data to a regular array
  data = data.to_numpy()
  #Reorder to frame-x-y-int for consistency
  data = data[:,[0,1,2,3]]
  return data

def readTXT(filename):
  import pandas
  #Read the TXT as a CSV file, with tab-separated data, using only columns 1-4
  data = pandas.read_csv(filename, header=None, skiprows=1, sep=" ", usecols=[0,1,2,3])
  #Convert the data to a regular array
  data = data.to_numpy()
  #Reorder to frame-x-y-int for consistency
  data = data[:,[2,0,1,3]]
  return data

def progress_bar(iterated_object, progressbar_len=50):
    progress = (i+1)/len(iterated_object)
    block = int(progressbar_len*progress)
    clear_output(wait=True)
    text = "Progress: [{0}] {1:.1f}%".format( "#" * block + "-" * (progressbar_len - block), progress * 100)
    print(text)
