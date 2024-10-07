from ultralytics import YOLO
import json

model = YOLO('best_covid19.pt')

def image_classification(image):

    results = model(image)
    probs = results[0].probs

    clasification = []
    if probs is not None:
        top5_indices = probs.top5
        top5_confidences = probs.top5conf

        for idx in top5_indices:
            label = model.names[idx] 
            confidence = top5_confidences[top5_indices.index(idx)].item()  
            clasification.append({
                "label": label,
                "confidence": round(float(confidence), 2)
            })
    
    return json.dumps(clasification, indent=4) 
