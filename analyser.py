from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

print("AI Sentiment Analyzer (type 'exit' to stop)\n")

while True:
    text = input("Enter text: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    result = sentiment_analyzer(text)[0]

    label = result['label']
    score = result['score']

    print(f"Sentiment: {label}")
    print(f"Confidence: {round(score, 2)}\n")