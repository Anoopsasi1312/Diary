import streamlit as st
import plotly.express as px
import glob
import re
from datetime import datetime
import nltk
import pandas as pd
nltk.download('vader_lexicon')


# Create app title

st.title("Diary Tone")

# Extract filepaths

filenames = glob.glob('**/*.txt', recursive=True)

date_objs = []

# Create positivity and negativity part


# Create blank list to store the scores after every iteration of for loop
positive_scores = []
negative_scores = []

for filename in filenames:
    with open(filename, 'r') as file:
        entry = file.read()

        # Use regex to extract the pattern of date from the filename
        date_pattern = r'\d{4}-\d{2}-\d{2}'
        date_str = re.search(date_pattern, filename).group(0)
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        # Use nltk to conduct sentiment analysis
        from nltk.sentiment import SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(entry)
        positive_score = scores['pos']
        negative_score = scores['neg']

# Append the date object and positive score to their respective lists
        date_objs.append(date_obj)
        positive_scores.append(positive_score)
        negative_scores.append(negative_score)

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Date': date_objs,
    'Positive_Score': positive_scores
})

df1 = pd.DataFrame({
    'Date': date_objs,
    'Positive_Score': negative_scores
})

st.header("Positivity")

# Plot the positive graph
figure = px.line(data_frame=df, x=date_objs, y=positive_scores)
st.plotly_chart(figure)

st.header("Negativity")

# Plot the negative graph
figure1 = px.line(data_frame=df, x=date_objs, y=negative_scores)
st.plotly_chart(figure1)
#This is a test