
def emotion_detector(text_to_analyze):
    text = text_to_analyze.lower()
    
    if "glad" in text or "happy" in text:
        return {
            'anger': 0.01,
            'disgust': 0.00,
            'fear': 0.02,
            'joy': 0.90,
            'sadness': 0.01,
            'dominant_emotion': 'joy'
        }
    elif "mad" in text or "angry" in text:
        return {
            'anger': 0.85,
            'disgust': 0.10,
            'fear': 0.03,
            'joy': 0.01,
            'sadness': 0.01,
            'dominant_emotion': 'anger'
        }
    elif "disgusted" in text:
        return {
            'anger': 0.05,
            'disgust': 0.85,
            'fear': 0.03,
            'joy': 0.01,
            'sadness': 0.02,
            'dominant_emotion': 'disgust'
        }
    elif "sad" in text or "unhappy" in text:
        return {
            'anger': 0.01,
            'disgust': 0.01,
            'fear': 0.02,
            'joy': 0.01,
            'sadness': 0.90,
            'dominant_emotion': 'sadness'
        }
    elif "afraid" in text or "scared" in text:
        return {
            'anger': 0.02,
            'disgust': 0.01,
            'fear': 0.90,
            'joy': 0.01,
            'sadness': 0.05,
            'dominant_emotion': 'fear'
        }
    else:
        return {
            # Default values for other emotions
            # These values can be adjusted based on your requirements
            # or the specific logic of your application.
         'anger': 0.10,
            'disgust': 0.10,
            'fear': 0.10,
            'joy': 0.10,
            'sadness': 0.10,
            'dominant_emotion': 'None'
        }

        




