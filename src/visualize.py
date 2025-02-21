import pandas as pd

def generate_visuals(df):
    # Generate metrics for Power BI, e.g., trends in customer feedback, sentiment analysis scores
    df['sentiment'] = df['feedback'].apply(lambda x: sentiment_analysis(x))  # Example sentiment function
    df.to_csv('data/customer_feedback_visual.csv', index=False)

def sentiment_analysis(text):
    # A placeholder sentiment analysis function (you could use pre-built libraries)
    return 'positive' if 'good' in text else 'negative'

# Example usage
df = pd.read_csv('data/processed_data.csv')
generate_visuals(df)
