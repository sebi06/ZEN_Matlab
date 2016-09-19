# Author: Sebastian Rhode
# Date: 26.03.2015
# Version: 1.2

# Send the current open image over to MATLAB using ReadImage6D.m --> has to be on the MATLAB path !!!
from System.Runtime.InteropServices import Marshal
from System.IO import Path, File, Directory, FileInfo
import os

CZIfiles_short = []
CZIdict = {}
# get all open documents
opendocs = Zen.Application.Documents
for doc in opendocs:
    image = Zen.Application.Documents.GetByName(doc.Name)
    if image.FileName.EndsWith('.czi'):
        # get the filename of the current document only when it ends with '.czi'
        CZIfiles_short.append(Path.GetFileName(image.FileName))
        CZIdict[Path.GetFileName(image.FileName)] = image.FileName

## Activate GUI
wd = ZenWindow()
wd.Initialize('Sent CZI to MATLAB',470,200,True,True)
## add components to dialog
wd.AddLabel('Sends selected CZI image to MATLAB.', '0', '0')
wd.AddLabel('Uses MATLAB wrapper (bfopen) for BioFormats.', '1', '0')
wd.AddDropDown('czi', 'Select CZI Image Data', CZIfiles_short, 0, '2','0')
## show the window
result=wd.Show()
## check, if Cancel button was clicked
if result.HasCanceled == True:
    sys.exit('Macro aborted with Cancel!')

## get the input values and store them
cziname = result.GetValue('czi')

try: 
    MATLAB = Marshal.GetActiveObject('MATLAB.Application.9.0')
    print 'ZEN-MATLAB bridge is OK.'
    MLOK = True
except:
    print 'MATLAB not running'
        
if MLOK == True:

    ## get current active document
    CZIfolder = os.path.dirname(CZIdict[cziname])
    print 'Transfer: ', CZIdict[cziname]
    ## create MATLAB variables
    MATLAB.execute("filename = '"+CZIdict[cziname]+"'")
    MATLAB.execute("CZIimage = ReadImage6D(filename);")
    
    print 'Done'
