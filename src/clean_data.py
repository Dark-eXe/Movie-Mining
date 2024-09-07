"""
Cleans data via pandas dataframe manipulation methods.
Creates 'movies_cleaned.csv' in same directory.
"""
import pandas as pd

df = pd.read_csv('movies.csv')

def clean_year(y):
    # removes parantheses
    return y[1:5]

def clean_rtscore(rts):
    # creates numerical values from percent value as raw string
    # e.g. '99%' -> 99
    return int(rts[0:2])

def clean_consensus(con):
    # removes header "Critic Consensus: " from each consensus value
    return con[19:]

def clean_synopsis(syn):
    # removes header "Synopsis: " and tail " [More]" from each synopsis value
    return syn[10:-7]

def clean_cast(cast):
    # removes header "Cast: " from each cast value
    return cast[10:]

# Apply all data cleaning
df['Year'] = df['Year'].apply(clean_year)

df['Rotten Tomatoes Score (%)'] = df['Rotten Tomatoes Score'].apply(clean_rtscore)
df = df.drop('Rotten Tomatoes Score', axis=1)

df['Critic Consensus'] = df['Critic Consensus'].apply(clean_consensus)

df['Synopsis'] = df['Synopsis'].apply(clean_synopsis)

df['Cast'] = df['Cast'].apply(clean_cast)

# Sets title as index
df = df.set_index('Title')

df.to_csv('movies_cleaned.csv')
print("Success! 'movies_cleaned.csv' created in same directory.")