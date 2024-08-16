import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# **** parameter ******************************************
API_KEY = config['AZURE']['API_KEY']
ENDPOINT_URI = config['AZURE']['ENDPOINT_URI']
IMAGE_PATH = "../img/00.jpg"
VISUAL_FEATURES = [VisualFeatures.OBJECTS]
# *********************************************************

def getAnalysisClient():
    client = ImageAnalysisClient(
        endpoint=ENDPOINT_URI,
        credential=AzureKeyCredential(API_KEY)
    )
    return client
     
def getAnalysingResult():
    result = client.analyze(
        open(IMAGE_PATH, "rb"),
        visual_features=VISUAL_FEATURES,
        gender_neutral_caption=True,
        language="ja")
    return result

def showResult(result):
    if VisualFeatures.OBJECTS in VISUAL_FEATURES:
        if result.objects is not None:
            for obj in result.objects.list:
                print(obj.tags[0])
    elif VisualFeatures.READ in VISUAL_FEATURES:
        for line in result.read.blocks[0].lines:
            print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
            for word in line.words:
                print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")
    elif VisualFeatures.CAPTION in VISUAL_FEATURES:
        print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")
    elif VisualFeatures.PEOPLE in VISUAL_FEATURES:
        for person in result.people.list:
            print(f"   {person.bounding_box}, Confidence {person.confidence:.4f}")
    elif VisualFeatures.TAGS in VISUAL_FEATURES:
        for tag in result.tags.list:
            print(f"   '{tag.name}', Confidence {tag.confidence:.4f}")

if __name__=='__main__':
    client = getAnalysisClient()
    result = getAnalysingResult()
    showResult(result)