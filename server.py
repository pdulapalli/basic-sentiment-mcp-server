from mcp.server.fastmcp import FastMCP
from textblob import TextBlob


mcp = FastMCP("Sentiment")


@mcp.tool()
def analyze_text_sentiment(text: str) -> dict:
    """Analyze the sentiment of a provided text"""
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.3:
        category = "positive"
    elif sentiment_score < -0.3:
        category = "negative"
    else:
        category = "neutral"

    return {
        "sentiment_score": sentiment_score,
        "sentiment_category": category,
    }


@mcp.resource("mood://{mood}")
def get_mood_support(mood: str) -> dict:
    """Get supportive content based on the user's mood"""

    responses = {
        "positive": "Wonderful! Keep that positive energy going!",
        "negative": "Have you tried listening to some music or finding a squirrel?",
        "neutral": "Why don't you try something new today?",
    }

    mood_lowercase = mood.lower()
    if mood_lowercase in responses:
        return responses[mood_lowercase]

    return responses["neutral"]


if __name__ == "__main__":
    mcp.run(transport="stdio")
