import os
import face_recognition
import pickle
from PIL import Image
import numpy as np
import shutil

def get_embeddings(target_dir,source_dir):
    os.makedirs(target_dir, exist_ok=True)
    for filename in os.listdir(source_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            
            image_path = os.path.join(source_dir, filename)
            
            image = face_recognition.load_image_file(image_path)

            face_locations = face_recognition.face_locations(image)
            
            face_encodings = face_recognition.face_encodings(image, face_locations)
            
            for i, encoding in enumerate(face_encodings):
                encoding_path = os.path.join(target_dir, f"{filename}_{i}.pkl")
                with open(encoding_path, 'wb') as file:
                    pickle.dump(encoding, file)

def copy_matched_photos(target_dir,matched_photos,source_photos_dir):
    image_paths = []
    for match in matched_photos:
        image_path = os.path.join(source_photos_dir, match)
        new_image_path = os.path.join(target_dir, match)
        shutil.copy(image_path, new_image_path)
        image_paths.append(image_path)#store the paths just to check manually
        with open("found_faces_in_photos.txt", "w") as file:
            file.write("\n".join(image_paths))

def get_mean_selected_face(source_dir):
    for filename in os.listdir(source_dir):

        if filename.endswith(('.jpg', '.jpeg', '.png')):
            specific_image_path = os.path.join(source_dir, filename)
            specific_image = face_recognition.load_image_file(specific_image_path)
            encodings = face_recognition.face_encodings(specific_image)
            print(encodings)
            if encodings:
                specific_face_encodings.append(encodings[0])

        if specific_face_encodings:
            specific_face_encoding = np.mean(specific_face_encodings, axis=0)
        else:
            raise ValueError("No face encodings found in the specific faces directory.")
    return specific_face_encoding


def find_matches(embed_dir, target_face, tolerance_threshold):

    matches=[]
    for filename in os.listdir(embed_dir):
        encoding_path = os.path.join(embed_dir, filename)

        with open(encoding_path, 'rb') as file:
            face_encoding = pickle.load(file)
        
        results = face_recognition.compare_faces([face_encoding], target_face, tolerance=tolerance_threshold)
        
        if results[0]:

            original_photo = "_".join(filename.split("_")[:-1])
            matches.append(original_photo)


    matches = list(set(matches))

    return matches



origin_photos_dir = "TestinngRecog/"#This is the directory with all 6 000 photos 
small_batch_photos_dir = "TestingRecog2/" '''This is directory with the small batch
                                             with only 50 photos.Ensured there are 
                                             my faces in some of those'''
             
photos_face_example_dir = "face_examples/" # Directory with the extracted faces
embeddings_dir = "embeddings/"
found_face_photos = "FoundFaceExamples/"

selected_face_dir = "my_face/"

threshold = 0.6
specific_face_encodings = []


