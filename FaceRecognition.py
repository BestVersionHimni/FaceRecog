import os
import face_recognition
import pickle
from PIL import Image

# Directory containing photos
photos_dir = "TestingRecog2/"
# Directory to store face embeddings
embeddings_dir = "embeddings/"
os.makedirs(embeddings_dir, exist_ok=True)

# Threshold for face matching
threshold = 0.6


for filename in os.listdir(photos_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Load the image
        image_path = os.path.join(photos_dir, filename)
        image = face_recognition.load_image_file(image_path)
        
        # Detect faces in the image
        face_locations = face_recognition.face_locations(image)
        
        # Get the face embeddings
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        # Save each face encoding to a file
        for i, encoding in enumerate(face_encodings):
            encoding_path = os.path.join(embeddings_dir, f"{filename}_{i}.pkl")
            with open(encoding_path, 'wb') as file:
                pickle.dump(encoding, file)

# Step 2: Load and encode the specific face image
specific_face_image_path = "Spicific_Face.png"
specific_image = face_recognition.load_image_file(specific_face_image_path)
specific_face_encoding = face_recognition.face_encodings(specific_image)[0]

# Step 3: Compare the specific face with stored embeddings
matches = []
for filename in os.listdir(embeddings_dir):
    encoding_path = os.path.join(embeddings_dir, filename)
    
    # Load the stored face encoding
    with open(encoding_path, 'rb') as file:
        face_encoding = pickle.load(file)
    
    # Compare the specific face encoding with the current encoding
    results = face_recognition.compare_faces([face_encoding], specific_face_encoding, tolerance=threshold)
    
    # If a match is found, add the photo to the results
    if results[0]:
        # Extract the original photo filename
        original_photo = "_".join(filename.split("_")[:-1])
        matches.append(original_photo)

# Remove duplicates
matches = list(set(matches))

# Step 4: Display the results
#print("Photos containing the specific face:")
images = []
for match in matches:
    #print(match)
    image_path = os.path.join(photos_dir, match)
    images.append(match)
with open("found_faces_in_photos.txt", "w") as file:
    file.write("\n".join(images))
    