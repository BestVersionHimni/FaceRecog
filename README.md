I wanted to download all the photos from one website for personal analysis but had a problem: I couldn't download them in bulk from the website. I had to come up with my own script to download all of them.

   1. I extracted all the URLs of the albums with photos, so in the next step I could go through those to download the photos.
   2. I extracted the date of the uploaded images. This is used for naming and also as a time point to estimate my possible age in the photos.
   3. I also extracted the number of photos in each album so I could check if all the photos were downloaded.
   4. I created a script that retrieved the album and then extracted all the URLs of photos for the next download.
   5. I needed to find all the photos where I could see my face, but there are more than 5,000 photos in total. It would take a significant amount of time to process them manually.
   6. My friend advised me to create a face recognition script that would find all the photos of me and compile them.
   7. In the repository, you can now see the final solution that I used to perform all these steps and finally find all my photos.


   The main problem I encountered was my face at different ages. The photos cover a period of 5-6 years, so my appearance has changed significantly over time. I doubted the possibility of extracting all my photos using an example photo of me at 13 years old. I solved it as follows:
   
   1. I extracted all the faces from all the photos (more than 9,000 individual faces).
   2. I obtained embeddings of all the faces (this took a while 😅).
   3. I manually found four of my own faces to start with.
   4. I searched for similar faces throughout the entire directory of extracted faces to get more examples of my face. I repeated this step several times until I couldn't find any new photos of me. This allowed me to have the most accurate sample of my face.
   5. Now, I'm at the final step where I will use these samples to find all the photos with me and move them to a new directory.
      
P.S. I also attached a small batch of photos so you can try to run the code yourself without needing to find your own dataset.
