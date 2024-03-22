import speech_recognition as sr
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pyttsx3

def voice_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language='en-US')
        print("You said: ", text)

    except Exception as e:
        print("Error: ", str(e))
        return None

    return text

# Analyze emotion using TextBlob
def analyze_emotion_textblob(text):
    try:
        analysis = TextBlob(text)
        emotions = analysis.sentiment.polarity

        if emotions > 0:
            return "Positive"
        elif emotions < 0:
            return "Negative"
        else:
            return "Neutral"

    except Exception as e:
        print("TextBlob Error: ", str(e))
        return "Error"

# Analyze emotion using VaderSentiment
def analyze_emotion_vader(text):
    try:
        analyzer = SentimentIntensityAnalyzer()
        compound_score = analyzer.polarity_scores(text)['compound']

        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    except Exception as e:
        print("VaderSentiment Error: ", str(e))
        return "Error"

# Convert to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = voice_recognition()

    if text:
        #emotion_textblob = analyze_emotion_textblob(text)
        emotion_vader = analyze_emotion_vader(text)

        #print(f"TextBlob: The emotional sentiment of your text is {emotion_textblob}.")
        print(f"VaderSentiment: The emotional sentiment of your text is {emotion_vader}.")

        # You can choose to use either TextBlob or VaderSentiment based on your preference.
        # For example, using TextBlob:
        #text_to_speech(f"The emotional sentiment of your text is {emotion_textblob}.")
        text_to_speech(f"The emotional sentiment of your text is {emotion_vader}.")

        # Or using VaderSentiment:
        # text_to_speech(f"The emotional sentiment of your text is {emotion_vader}.")