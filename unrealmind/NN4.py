import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2
 
#load trained model
model=load_model("digit_model.h5")

# Custom preprocessing function
def preprocess_digit(img_path):
    # Load image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Invert if necessary (assuming digit is black on white mainly, but we want white on black)
    # Check the corner pixel; if it's bright, invert.
    if img[0,0] > 127:
        img = 255 - img
        
    # Threshold to clear noise
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Find bounding box of the digit
    coords = cv2.findNonZero(img)
    x, y, w, h = cv2.boundingRect(coords)
    
    # Crop the digit
    digit = img[y:y+h, x:x+w]
    
    # Resize preserving aspect ratio to fit in 20x20 box
    if w > h:
        scale = 20.0 / w
        new_w = 20
        new_h = int(h * scale)
    else:
        scale = 20.0 / h
        new_h = 20
        new_w = int(w * scale)
        
    resized_digit = cv2.resize(digit, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    # Create valid 28x28 black canvas
    final_img = np.zeros((28, 28), dtype=np.uint8)
    
    # Calculate centering offsets
    x_offset = (28 - new_w) // 2
    y_offset = (28 - new_h) // 2
    
    # Paste the digit
    final_img[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_digit
    
    return final_img

# Process the image
processed_image = preprocess_digit("my_digit.png")

# Save debug image
cv2.imwrite("debug_input.png", processed_image)

# Normalize and reshape
image = processed_image / 255.0
image = image.reshape(1, 28, 28, 1) # Ensure channel dimension is present

# Predict
prediction = model.predict(image)
digit = np.argmax(prediction)

print("Prediction probabilities:", prediction)
print("Predicted digit:", digit)
