from textblob import TextBlob

def sentiment_analysis_tool():
    print("Welcome to the Simple Sentiment Analysis Tool!")
    print("Type a sentence and I'll tell you its sentiment.")
    print("Type 'exit' to quit the tool.")
    
    while True:
        user_input = input("\nEnter a sentence: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Analyze sentiment
        analysis = TextBlob(user_input)
        sentiment = analysis.sentiment.polarity
        
        # Determine sentiment category
        if sentiment > 0:
            print("😊 Positive sentiment")
        elif sentiment < 0:
            print("😠 Negative sentiment")
        else:
            print("😐 Neutral sentiment")

# Run the tool
if __name__ == "__main__":
    sentiment_analysis_tool()
