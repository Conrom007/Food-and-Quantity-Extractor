import pandas as pd
from fuzzywuzzy import process

def get_closest_match(input):
    # Load CSV file into a pandas dataframe
    df = pd.read_csv('nutrition.csv')

    # Get list of possible matches from the specified column
    choices = list(df['name'])

    # Find the closest match to the user input using the fuzzywuzzy library
    match = process.extractOne(input, choices)

    # Return the closest match and its score
    return match[0], match[1]

get_closest_match('Chicken')