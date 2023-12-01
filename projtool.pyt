# -*- coding: utf-8 -*-

import arcpy
from arcpy.sa import *


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [VARIClassificationTool]


class VARIClassificationTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "VARI-based Classification"
        self.description = "Classify raster based on VARI range"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions."""
        params = [
            arcpy.Parameter(
                displayName="Input Raster",
                name="input_raster",
                datatype="DERasterDataset",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Definition Classification File",
                name="classdef_file",
                datatype="DEFile",
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Number of Classes",
                name="num_classes",
                datatype="GPLong",
                parameterType="Required",  # This line specifies that the parameter is required
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Output Raster",
                name="output_raster",
                datatype="DERasterDataset",
                parameterType="Required",
                direction="Output"
            )
        ]
        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""
        try:
            # Get input parameters
            input_raster = parameters[0].valueAsText
            classdef_file = parameters[1].valueAsText
            num_classes = parameters[2].value
            output_raster = parameters[3].valueAsText

            # Perform VARI-based classification
            arcpy.AddMessage("Performing VARI-based Classification...")
            out_classified_raster = Classify(input_raster, None, classdef_file)

            # Save the output raster
            out_classified_raster.save(output_raster)
            arcpy.AddMessage(f"Classification complete. Output saved to {output_raster}")

        except Exception as e:
            arcpy.AddError(str(e))
