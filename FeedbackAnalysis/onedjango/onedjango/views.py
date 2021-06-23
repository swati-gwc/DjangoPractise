from django.http import HttpResponse
from django.shortcuts import render
import joblib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from json import dumps

def home(request):
    return render(request,"home.html")

def result(request):
    ans = sentiment_scores(request.GET['feedback'])
    dataJSON = dumps(ans)
    return render(request,"result.html",{'ans':dataJSON})


def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    result = []
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Sentence Overall Rated As", end = " ")

    result.append(sentiment_dict['neg']*100)
    result.append(sentiment_dict['neu']*100)
    result.append(sentiment_dict['pos']*100)
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
        overallans = "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
        overallans =  "Negative"
 
    else :
        print("Neutral")
        overallans =  "Neutral"
    
    result.append(overallans)
    print(result)
    return result
    