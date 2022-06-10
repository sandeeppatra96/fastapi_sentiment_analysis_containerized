from fastapi import FastAPI, HTTPException
from transformers import pipeline

appi = FastAPI()


@appi.get("/pred/{text}")
async def read_item(text: str):
    #return "Welcome to my sentiment analysis app, fuckers!\nUse the post method or just type out the string to check the sentiment"
    classifier = pipeline("sentiment-analysis")
    ver = classifier(text)
    return {'text': text, 'verdict' : ver}

@appi.post("/pred")
def cli(text):

    if(not(text)):
        raise HTTPException(status_code=400, 
                            detail = "Please Provide a valid text message")

    classifier = pipeline("sentiment-analysis")
    ver = classifier(text)
    return {'text': text, 'verdict' : ver}

        