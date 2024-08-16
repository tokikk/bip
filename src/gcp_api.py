import io
import os
import glob
from google.cloud import vision
from google.oauth2 import service_account


# **** parameter ******************************************
IMAGE_PATH = "../img/00.jpg"
KEY_PATH = "../cred/my_key.json"
# *********************************************************

credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = vision.ImageAnnotatorClient(credentials=credentials)

with io.open(IMAGE_PATH, 'rb') as image_file:
    content = image_file.read()  
    image = vision.Image(content=content)

    response =  client.object_localization(image=image).localized_object_annotations
    print(f"Number of objects found: {len(response)}")
    for object in response:
        print(f"\n{object.name} (confidence: {object.score})")
        print("Normalized bounding polygon vertices: ")
        for vertex in object.bounding_poly.normalized_vertices:
            print(f" - ({vertex.x}, {vertex.y})")