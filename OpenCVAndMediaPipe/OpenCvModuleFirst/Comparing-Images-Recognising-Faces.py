import cv2
import face_recognition
import os

# Set up the directories for capturing and saving images
capture_directory = 'All_Images'
os.makedirs(capture_directory, exist_ok=True)

# Load the pre-trained face recognition model
known_face_encodings = []
known_face_names = []

# Function to capture and save an image
def capture_and_save_image():
    # Open a connection to the default camera (0)
    cap = cv2.VideoCapture(0)

    # Capture a single frame
    ret, frame = cap.read()

    # Generate a unique filename for the captured image
    image_filename = os.path.join(capture_directory, f'captured_image_{len(known_face_encodings)}.jpg')

    # Save the captured image
    cv2.imwrite(image_filename, frame)

    # Release the camera
    cap.release()

    return image_filename

# Function to recognize and compare faces
def recognize_faces(target_image_path):
    # Load the target image
    target_image = face_recognition.load_image_file(target_image_path)

    # Find face locations and encodings in the target image
    target_face_locations = face_recognition.face_locations(target_image)
    target_face_encodings = face_recognition.face_encodings(target_image, target_face_locations)

    # Compare with known faces
    for i, encoding in enumerate(target_face_encodings):
        results = face_recognition.compare_faces(known_face_encodings, encoding)
        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in results:
            index = results.index(True)
            name = known_face_names[index]

        print(f"Face {i+1}: {name}")

# Capture and save an image
captured_image_path = capture_and_save_image()

# For demonstration purposes, assume the captured image is a known face
known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(captured_image_path))[0])
known_face_names.append("Captured Face")

# Recognize and compare faces in the captured image
recognize_faces(captured_image_path)
