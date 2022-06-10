# fastapi_sentiment_analysis_dockerized

A sentiment analysis API using fastAPI, containerized using docker. The model used was distilbert.

There are two modes to use this API.
1) Put the text in the path after /pred
   Example: https:127.0.0.1:8000/pred/'world is doomed'
 
2) Use the post command
   Example: curl -X 'POST' 'http://127.0.0.1:8000/pred?text=I%20wanna%20die' -H 'accept: application/json' -d ''
   
   or use the http://127.0.0.1:8000/docs and type out the sentence
   
   
