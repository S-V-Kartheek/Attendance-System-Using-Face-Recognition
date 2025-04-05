cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: No webcam found. Trying next index.")
    cap = cv2.VideoCapture(1)  # Try next device
    if not cap.isOpened():
        raise Exception("No webcam available.")