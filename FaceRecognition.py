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


def find_matches(pool, reference_embeddings, tolerance_threshold):
        matches = []
        i=0
        for encoding in pool:
            results = [face_recognition.compare_faces(reference_embeddings,encoding[0],tolerance_threshold)]
            #print(results,0)
            results = [result[0] for result in results]
            #print(results,1)
            if any(results):
                
                matches.append(encoding[1])
            i += 1
        matches = list(set(matches))
        print(i)
        return matches

def read_embeddings(embed_dir, reference_embeddings):
    target_face_embeddings = []
    pool_embeddings = []
    pool_photos = []
    for filename in os.listdir(embed_dir):
            encoding_path = os.path.join(embed_dir, filename)
            with open(encoding_path, 'rb') as file:
                face_encoding = pickle.load(file)
            pool_embeddings.append(face_encoding)
            original_photos = "_".join(filename.split("_")[:-1])
            pool_photos.append(original_photos)
    combined_list = [[x,y] for x,y in zip(pool_embeddings,pool_photos)]
    
    for filename in os.listdir(reference_embeddings):
            encoding_path = os.path.join(reference_embeddings, filename)
            with open(encoding_path, 'rb') as file:
                face_encoding = pickle.load(file)
            target_face_embeddings.append(face_encoding)
            
    return target_face_embeddings, combined_list
    

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
             
selected_face_dir = "my_face/" #Here all photos of my face are stored
all_photos = "all_photos/" #Here all photos are stored
all_embed = "all_embeddings/" #Here embeddings of all photos are stored
matched_photos_dir = "FoundPhotos/" #This is the directory for the found photos
my_face_embed = "my_face/my_face_embed" #Here all embeddings of my face a stored, so I can faster run the code




#0- is the most specific 1 is the most broad
tolerance_threshold = 0.54
#It turned out there are more than 13000 photos, so i will firstly get embeddings.
get_embeddings(my_face_embed,selected_face_dir)
print("Went to reading")
target_face_encodings, all_photos_embeddings = read_embeddings(embed_dir=all_embed,reference_embeddings=my_face_embed)

matched_photos = find_matches(all_photos_embeddings,target_face_encodings,tolerance_threshold)
    
print("Went to coping")
copy_matched_photos(matched_photos_dir,matched_photos,all_photos)
