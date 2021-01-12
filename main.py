import textblob as textblob



from textblob import TextBlob


def review(y):
    if y < 0:
        print("Negative")
    elif y == 0:
        print("Neutral")
    elif y > 0 and y <= 1:
        print("Positive")


x = input("Give Your Feedback: ")
t = TextBlob(x).polarity
review(t)