% file: get_zstack.m
% Date: 18.06.2015
% Version: 0.1

% Read Z-Stack from CZI image data into array 

function out = get_zstack(filename, seriesID, timepoint)

if ~exist('seriesID', 'var')
    seriesID = 1;
end

if ~exist('timepoint', 'var')
    timepoint = 1;
end

% Get OME Meta-Information
MetaData = GetOMEData(filename);

% Initialize BioFormtas Reader
reader = bfGetReader(filename);

% add progress bar
h = waitbar(0,'Processing Data ...');
totalframes = MetaData.SizeC * MetaData.SizeZ;
framecounter = 0;

% Preallocate array with size (Series, SizeC, SizeZ, SizeT, SizeX, SizeY) 
imgZStack = zeros(MetaData.SeriesCount, MetaData.SizeT, MetaData.SizeZ,  MetaData.SizeC, MetaData.SizeY, MetaData.SizeX);


% set reader to current series
reader.setSeries(seriesID-1);
for zplane = 1: MetaData.SizeZ
    for channel = 1: MetaData.SizeC

        framecounter = framecounter + 1;
         % update waitbar
        wstr = {'Reading Z-Stack for all Channels: ', num2str(framecounter), ' of ', num2str(totalframes),'Frames' };
        waitbar(framecounter / totalframes, h, strjoin(wstr))

        % get linear index of the plane (1-based)
        iplane = loci.formats.FormatTools.getIndex(reader, zplane - 1, channel - 1, timepoint -1) +1;
        % get frame for current series
        imgZStack(seriesID, timepoint, zplane, channel, :, :) = bfGetPlane(reader, iplane);

    end
end

% close waitbar
close(h)

% close BioFormats Reader
reader.close();

% store image data and meta information in cell array
out = {};
out{1} = imgZStack;
out{2} = MetaData;
    




