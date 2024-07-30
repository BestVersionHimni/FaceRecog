import face_recognition
from PIL import Image
import os



directories_to_extract = os.listdir("backup/")

for directory in directories_to_extract:
        
        faces_orig_dir = "".join(("backup/",directory))
        output_dir = "face_examples/"
        os.makedirs(output_dir, exist_ok=True) 

        for faces_file in os.listdir(faces_orig_dir):
            if faces_file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(faces_orig_dir, faces_file)
                
                image = face_recognition.load_image_file(image_path)
                
                
                face_locations = face_recognition.face_locations(image)
                print(f"Detected {len(face_locations)} face(s) in {faces_file}")
                for i, face_location in enumerate(face_locations):
                    
                    top, right, bottom, left = face_location                    
                    pil_image = Image.fromarray(image)
                    face_image = pil_image.crop((left, top, right, bottom))
                    
                    face_filename = f"{os.path.splitext(faces_file)[0]}_face_{i}.jpg"
                    face_image_path = os.path.join(output_dir, face_filename)

                    face_image.save(face_image_path)
                    print(f"Saved face image as {face_image_path}")
