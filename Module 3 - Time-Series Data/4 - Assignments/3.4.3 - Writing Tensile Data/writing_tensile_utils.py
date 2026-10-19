import math

import numpy as np


def parse_tensile_file(path_to_file):
    file = open(path_to_file)
    # required meta-data
    gage_diameter = -1
    maximum_force = - 1
    maximum_strain = -1
    # determine when to begin reading into these files
    begin_reading = False
    time = []
    displacement = []
    force = []
    strain = []
    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == False:

            # gather various meta data
            if splits[0] == "Gage Diameter":
                cleaned = splits[2].replace('\"', '')
                gage_diameter = float(cleaned)
            if splits[0] == "Maximum Force":
                cleaned = splits[2].replace('\"', '')
                maximum_force = float(cleaned)
            if splits[0] == "Maximum Strain":
                cleaned = splits[2].replace('\"', '')
                maximum_strain = float(cleaned)

        else:
            # parse the actual data
            time.append(float(splits[0].replace('\"', '')))
            displacement.append(float(splits[1].replace('\"', '')))
            force.append(float(splits[2].replace('\"', '')))
            strain.append(float(splits[3].replace('\"', '')))

        # try to find start of data
        if splits[0] == "(s)":
            begin_reading = True
    file.close()

    return gage_diameter, np.asarray(time), np.asarray(displacement), np.asarray(force), np.asarray(strain)


# ---------------------------------------------------------------------------------------------
# The four functions below are the ones you wrote in the Tensile Testing assignment (3.4.2).
# Copy your completed versions from your tensile-strength-step4.py file into this file,
# replacing each placeholder function with your own. Do not change the function names.
#
# The Gradescope autograder for THIS assignment uses its own correct copy of these functions,
# so it only grades your generate_csv_file() function. You only need these to run locally.
# ---------------------------------------------------------------------------------------------


def calculate_stress(force, sample_diameter):
    """
    Calculate the stress (MPa) experienced by the test given a series of forces/loads (kN) and
    a sample diameter (mm)
    :param force: An array of forces/loads applied to the sample in Kilo Newtons (kN)
    :param sample_diameter: The diameter of the sample in millimeters (mm)
    :return: An array of stresses experienced by the sample in MegaPascals (MPa)
    """

    ### YOUR SOLUTION FROM STEP 1 TEMPLATE HERE ###

    # Calculate cross-sectional area (mm^2)
    c_s_area = np.pi * (sample_diameter / 2)**2

    # Calculate stress (MPa)
    stress = (force * 1000) / c_s_area

    return stress



def calculate_max_strength_strain(strain, stress):
    """
    Calculate the Ultimate Tensile Stress and Fracture Strain
    :param strain: An array of Strain data (mm/mm, dimensionless)
    :param stress: An array of Stress data
    :return:
    Ultimate Tensile Stress: the maximum stress experienced
    Fracture Strain: the maximum strain experienced before fracture
    """

    ### YOUR SOLUTION FROM STEP 2 TEMPLATE HERE ###
    # calculate the maximum stress experienced
    ultimate_tensile_stress = np.max(stress)
    
    # calculate the maximum strain experienced
    fracture_strain = np.max(strain)

    return ultimate_tensile_stress, fracture_strain

def calculate_elastic_modulus(strain, stress):
    """
        Given a set of stress strain data, use the Secant Modulus at 40% method to determine
        the elastic modulus
        :param strain:
        :param stress:
        :return:
        linear_index: the index within the strain/stress data that is the end of the linear region
        slope: the slope for the linear region of the strain/stress data
        intercept: y-intercept for linear region best fit of strain/stress data
    """

    # dummy variables the function should over write
    linear_index = None
    slope = None
    intercept = None

    ### YOUR SOLUTION FROM STEP 3 TEMPLATE HERE ###

    # Calculate ultimate tensile stress
    ultimate_tensile_stress = np.max(stress)

    # Find 40% of maximum stress
    secant_stress = 0.4 * ultimate_tensile_stress

    # Find the closest stress value to 40%
    diffs = np.abs(stress - secant_stress)
    linear_index = np.argmin(diffs)

    # Select the linear region
    linear_stress = stress[:linear_index]
    linear_strain = strain[:linear_index]

    # Calculate slope and intercept
    slope, intercept = np.polyfit(linear_strain, linear_stress, 1)

    return linear_index, slope, intercept

def calculate_percent_offset(slope, strain, stress):
    """
    Determine the 0.2% Offset Yield by identifying the intercept with the stress curve and a parallel line

    :param slope: Slope of the offset line. This should be the elastic modulus
    :param strain: An array of Strain data (mm/mm, dimensionless)
    :param stress: An array of Stress data
    :return:
    offset_line: the y-values for the 0.2% offset line
    intercept_index: The index where the offset line and the strain line intersect
    """
    # set the desired offset for the line
    offset = 0.002

    # calculate the offset line: y=m(x-0.002) + 0
    offset_line = slope * (strain - offset) + 0

    # measure distance from all points on graph to this line. Consider using the
    # abs() method to ensure values are positive
    distance = np.abs(stress - offset_line)

    # use argmin to find the index where the distance is minimal
    intercept_index = np.argmin(distance)

    return offset_line, intercept_index


def calculate_yield_strength(strain, stress, modulus):
    """
    Determine the yield strength (MPa) via the 0.2% offset method.
    This one is provided for you. It uses your calculate_percent_offset() above.
    """
    offset_line, intercept_index = calculate_percent_offset(modulus, strain, stress)

    if intercept_index == -1:
        return -1

    return stress[intercept_index]


class MaterialSample:
    """
    A simple class to hold results from materials tensile analysis
    """

    def __init__(self):
        self.name = ""
        self.material_type = ""
        self.tensile_strength = -1
        self.fracture_strain = -1
        self.elastic_modulus = -1
        self.yield_strength = -1
