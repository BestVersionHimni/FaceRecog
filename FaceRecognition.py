import os
import face_recognition
import pickle
from PIL import Image


photos_dir = "TestingRecog2/"

embeddings_dir = "embeddings/"
os.makedirs(embeddings_dir, exist_ok=True)


threshold = 0.6


for filename in os.listdir(photos_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        
        image_path = os.path.join(photos_dir, filename)
        image = face_recognition.load_image_file(image_path)
        
        
        face_locations = face_recognition.face_locations(image)
        
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        for i, encoding in enumerate(face_encodings):
            encoding_path = os.path.join(embeddings_dir, f"{filename}_{i}.pkl")
            with open(encoding_path, 'wb') as file:
                pickle.dump(encoding, file)


specific_face_image_path = "Spicific_Face.png"
specific_image = face_recognition.load_image_file(specific_face_image_path)
specific_face_encoding = face_recognition.face_encodings(specific_image)[0]

matches = []
for filename in os.listdir(embeddings_dir):
    encoding_path = os.path.join(embeddings_dir, filename)
    
    
    with open(encoding_path, 'rb') as file:
        face_encoding = pickle.load(file)
    
    results = face_recognition.compare_faces([face_encoding], specific_face_encoding, tolerance=threshold)
    

    if results[0]:

        original_photo = "_".join(filename.split("_")[:-1])
        matches.append(original_photo)


matches = list(set(matches))

images = []
for match in matches:
    
    image_path = os.path.join(photos_dir, match)
    images.append(match)
with open("found_faces_in_photos.txt", "w") as file:
    file.write("\n".join(images))
    