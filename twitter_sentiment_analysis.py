import tweepy
from textblob import TextBlob
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Step 1 - Authenticate
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'
access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to perform sentiment analysis and display results
def analyze_tweets():
    keyword = entry.get()
    if keyword:
        try:
            public_tweets = api.search_tweets(q=keyword, count=100)
            result_text.delete(1.0, tk.END)  # Clear previous results

            for tweet in public_tweets:
                tweet_text = tweet.text
                analysis = TextBlob(tweet_text)
                polarity = analysis.sentiment.polarity

                if polarity > 0:
                    sentiment = 'Positive'
                elif polarity < 0:
                    sentiment = 'Negative'
                else:
                    sentiment = 'Neutral'

                # Display the tweet and sentiment in the scrolled text widget
                result_text.insert(tk.END, f"Tweet: {tweet_text}\nSentiment: {sentiment}\nPolarity: {polarity:.2f}\n\n")

        except tweepy.TweepError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a keyword to search.")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Twitter Sentiment Analysis")

# Input field
tk.Label(root, text="Enter keyword to search tweets:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze_tweets)
analyze_button.pack(pady=5)

# ScrolledText widget to display results
result_text = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
