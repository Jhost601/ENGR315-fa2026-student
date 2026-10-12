import sys
"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###
# Question 1:
def main():
    
    # specify the path to the NYT data file
    file_path = 'data/covid/us-counties.csv'
    
    # parse the data using the function 
    data = parse_nyt_data(file_path)
    # state name search 
    state_name = "Virginia"
    # filtering by state
    filtered_function = get_state_data(state_name, data)
    # county search locations 1 and 2
    county1_name = "Rockingham"
    county2_name = "Harrisonburg city"
    
    # filtering by county
    county1_function = get_county_data(county1_name, filtered_function)
    # filtering by county
    county2_function = get_county_data(county2_name, filtered_function)
    # analyze county data
    analysis_result_1 = analyze_data(county1_function)
    # analyze 7 day set
    seven_day_analysis_1 = analyze_7day(county1_function)
    # analyze county data
    analysis_result_2 = analyze_data(county2_function)
    # analyze 7 day set
    seven_day_analysis_2 = analyze_7day(county2_function)
   
    # Prints Question 1 and 2
    print("Greatest daily increase date and amount for Rockingham with first occurrence:", analysis_result_1, )
    print("Greatest daily increase date and amount for Harrisonburg city with first occurrence:", analysis_result_2, )
    # Prints Question 3 
    print("Seven-Day period for Rockingham:", seven_day_analysis_1)
    print("Seven-Day period for Harrisonburg city:", seven_day_analysis_2)

# define function for state 
def get_state_data(state_name, data):
    # categorize the data by state 
    state = []
    
    # loop the data and filter by name
    for entry in data:
        if entry [2] == state_name:
            # adds record to state list
            state.append(entry)
  
    return state
# define function for county name 
def get_county_data(county_name, data):
    # define variable county
    county = []
    # loop data and filter by name
    for entry in data:
        if entry[1] == county_name:
            county.append(entry)

    return county
def analyze_data (cases):
    for entry in cases:
        if entry[4] > 0:
            first_case_date = entry[0]
            break
# Question 2:
    
    # Find the greatest number of new cases
    previous_cases = 0 
    greatest_new_cases = 0
    greatest_new_date = ""
    
    for entry in cases:
        # Find number of new cases since previous
        new_cases = entry[4] - previous_cases
        # Check if its the greatest number 
        if new_cases > greatest_new_cases:
            greatest_new_cases = new_cases
            greatest_new_date = entry[0]
        # Store the cumulative cases 
        previous_cases = entry[4]

    return greatest_new_date, greatest_new_cases, first_case_date  

def analyze_7day(data):
    greatest_7_day_cases = 0
    start_date = ""
    end_date = ""
    # Loop through possible 7 day periods 
    for i in range(7, len(data)):
        # Calculate cases during each period 
        seven_day_change = data[i][4] - data[i - 7][4]
        # Compare against cases
        if seven_day_change > greatest_7_day_cases:
            # Save dates when a new maximum is found
            greatest_7_day_cases = seven_day_change 
            start_date = data[i - 7][0]
        
            end_date = data [i][0]
    # for entry in data: # to check if the values between those dates equal max change
        # if entry[0] >= "2022-01-10" and entry[0] <= "2022-01-17":
            # print(entry)
    return start_date, end_date, greatest_7_day_cases
main()

