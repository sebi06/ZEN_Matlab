===============================
ZEN_Matlab
===============================

This example illustrates the possibility to control the ZEN Blue microscope control software from within a MATLAB script via the COM interface. This allows using the ZEN Python scripts as an integral part of an M-File. The ZEN OAD (Open Application Development) API can be imported into MATLAB and allows automating the complete workflow including the image acquisition from MATLAB. 

* ZEN is used as an image acquisition machine
* the experiment is started directly from within MATLAB
* the resulting CZI file is imported via BioFormats
* the image analysis is done in MATLAB

:Author: Sebastian Rhode

:Version: 2016.09.19

Notes
-----
The package is still under development and was mainly tested with CZI files. Currently the 5.1.10 version of bioformats_package.jar and its warpper for Matlab was used to test it.

Acknowledgements
----------------
*   The OME people for creating BioFormats.

References
----------
(1)  CZI - Image format for microscopes
     http://www.zeiss.com/czi
(2)  The OME-TIFF format.
     http://www.openmicroscopy.org/site/support/file-formats/ome-tiff

Disclaimer
----------
*   Remark: Please use at your own risk.
