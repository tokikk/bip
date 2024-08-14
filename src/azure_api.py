import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from . import infomation

# **** parameter ******************************************
API_KEY = infomation.key
ENDPOINT_URI = infomation.endpoint
IMAGE_PATH = "559_3about:blank#blocked_818_544.jpg"
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
        gender_neutral_caption=True,     )
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

    elif VisualFeatures.PEOPLE in VISUAL_FEATURES:

    elif VisualFeatures.TAGS in VISUAL_FEATURES:

   
if __name__=='__main__':
    client = getAnalysisClient()
    result = getAnalysingResult()
    showResult(result)