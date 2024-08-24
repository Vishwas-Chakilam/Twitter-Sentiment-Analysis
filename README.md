# Twitter-Sentiment-Analysis
Twitter Sentiment Analysis is a Python project that analyzes the sentiment of tweets based on a user-defined keyword. It uses Tweepy to fetch tweets from the Twitter API and TextBlob for sentiment analysis. The application features a user-friendly GUI with Tkinter, displaying tweet sentiment as positive, negative, or neutral.

# Twitter Sentiment Analysis

A Python-based application that analyzes the sentiment of tweets containing a specified keyword. It uses the Tweepy library to interact with the Twitter API and TextBlob for sentiment analysis. The application has a simple graphical user interface (GUI) built using Tkinter.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## Features

- **Real-time Sentiment Analysis**: Fetches tweets in real-time based on a user-defined keyword and analyzes their sentiment (positive, negative, neutral).
- **Simple GUI**: An easy-to-use graphical interface built with Tkinter.
- **Displays Sentiment and Polarity**: Shows the sentiment type and polarity score for each tweet.

## Prerequisites

To run this application, you need to have the following:

1. **Python 3.x**: Ensure Python is installed on your machine.
2. **Twitter Developer Account**: Create a Twitter Developer account to obtain API keys and tokens.
3. **Python Libraries**: Install the necessary Python libraries.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/twitter-sentiment-analysis.git
   cd twitter-sentiment-analysis
   ```

2. **Install Required Python Libraries**:

   Install the required libraries using `pip`:

   ```bash
   pip install tweepy textblob tkinter
   ```

3. **Configure Twitter API Keys**:

   Replace the placeholder values in the script with your actual Twitter API credentials:

   ```python
   consumer_key = 'CONSUMER_KEY_HERE'
   consumer_secret = 'CONSUMER_SECRET_HERE'
   access_token = 'ACCESS_TOKEN_HERE'
   access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'
   ```

## Usage

1. **Run the Application**:

   Run the Python script to start the application:

   ```bash
   python twitter_sentiment_analysis.py
   ```

2. **Use the GUI**:

   - Enter a keyword in the input field.
   - Click the **Analyze** button to fetch tweets and analyze their sentiment.
   - View the results in the scrollable text area.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any improvements or suggestions.


### Notes

- **Replace placeholders**: Make sure to replace any placeholders, like the GitHub repository link or Twitter API keys, with actual data relevant to your project.
- **Dependencies**: The `tkinter` library is usually included with Python, but its installation via `pip` is mentioned here for completeness.
- **License**: Include a `LICENSE` file if you choose to add licensing information to your project. The example assumes an MIT License, but you can adjust it as needed.
