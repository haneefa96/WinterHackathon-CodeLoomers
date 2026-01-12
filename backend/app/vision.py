# from google.cloud import vision

# def analyze_image(image_bytes: bytes):
#     client = vision.ImageAnnotatorClient()

#     image = vision.Image(content=image_bytes)

#     label_response = client.label_detection(image=image)
#     object_response = client.object_localization(image=image)

#     labels = [label.description for label in label_response.label_annotations]
#     objects = [obj.name for obj in object_response.localized_object_annotations]

#     description = "Handcrafted product detected"
#     if labels:
#         description = f"Handcrafted {labels[0].lower()} product"

#     return {
#         "labels": labels[:5],
#         "objects": objects[:5],
#         "description": description
#     }

from google.cloud import vision

def analyze_image(image_bytes: bytes):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_bytes)

    labels = client.label_detection(image=image).label_annotations
    objects = client.object_localization(image=image).localized_object_annotations

    return {
        "labels": [l.description for l in labels[:5]],
        "objects": [o.name for o in objects[:5]],
        "description": "Handcrafted product detected"
    }
