import os
import face_recognition
import pickle
from PIL import Image
import numpy as np
import shutil


def get_embeddings(target_dir,source_dir):

    if any(os.scandir(target_dir)):
        pass
    else:
        os.makedirs(target_dir, exist_ok=True)
        for filename in os.listdir(source_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                
                image_path = os.path.join(source_dir, filename)
                
                image = face_recognition.load_image_file(image_path)

                face_locations = face_recognition.face_locations(image,3)
                
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

def get_encodings_selected_face(source_dir):
    face_encodings = []
    for filename in os.listdir(source_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(source_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                face_encodings.append(encodings[0])
            else:
                pass
                #print(f"No face found in {filename}")
    if not face_encodings:
        raise ValueError("No face encodings found in the specified directory.")
    return face_encodings


def find_matches(embed_dir, reference_embeddings, tolerance_threshold):
    if not isinstance(embed_dir, list):
        matches = []
        for filename in os.listdir(embed_dir):
            encoding_path = os.path.join(embed_dir, filename)
            with open(encoding_path, 'rb') as file:
                face_encoding = pickle.load(file)
            results = [face_recognition.compare_faces([face_encoding], ref_encoding, tolerance=tolerance_threshold) for ref_encoding in reference_embeddings]
            results = [result[0] for result in results]
            if any(results):
                original_photo = "_".join(filename.split("_")[:-1])
                matches.append(original_photo)
        matches = list(set(matches))
    else:
        for face_encoding in embed_dir:
            results = [face_recognition.compare_faces([face_encoding], ref_encoding, tolerance=tolerance_threshold) for ref_encoding in reference_embeddings]
            results = [result[0] for result in results]
            if any(results):
                original_photo = "_".join(filename.split("_")[:-1])
                matches.append(original_photo)
            matches = list(set(matches))

        return matches

def pull_together_photos():
    for album in os.listdir(origin_photos_dir):
        old_photos_path = []
        new_photos_path = []
        old_photos_path = [f"{origin_photos_dir}{album}/{photo_path}" for photo_path in os.listdir(os.path.join(origin_photos_dir,album))]
        new_photos_path = [f"{all_photos}{photo_path}" for photo_path in os.listdir(os.path.join(origin_photos_dir,album))]
        for n in range(len(old_photos_path)):
            shutil.copy(old_photos_path[n],new_photos_path[n])
            
#Here we define all the directories that can be used. 
origin_photos_dir = "backup/"#This is the directory with all 6 000 photos 
small_batch_photos_dir = "TestingRecog2/" '''This is directory with the small batch
                                             with only 50 photos.Ensured there are 
                                             my faces in some of those'''
             
photos_face_example_dir = "face_examples/" # Directory with the extracted faces
embeddings_dir = "embeddings/"
found_face_photos = "FoundFaceExamples/"
selected_face_dir = "my_face/"
testing_faces_dir = "testing_batch/"
testing_embed_dir = "testing_batch/embeddings_testing/"
all_photos = "all_photos/"


tolerance_threshold = 0.5

