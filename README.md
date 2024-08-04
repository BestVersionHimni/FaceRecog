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
   5. I have run the code on all photos. This found 202 photos where 160 were correct. This brings our accurancy to 80 percent. 

Main problems: 
   1. As in my reference photos I have glasses on me, then sometimes any other person with similar glasses will tend to be validated as same face. That's why you can see there people with black or yellow glasses. 
   2. Small size of the images. Most images are only 5 540x360 this makes the recognition harder. 
   3. Threshold. I have tested different values and it seems 0.54 is the most suitable. I have thought if we can use dynamic threshold to compare faces but in any cases i would end up in the same position. As this threshold is only an error value for the final statistical test. Where let's say we manually set a threshold of p-value for H0. And basically playing with threshold for p-value will lead nowhere. 


      
P.S. I also attached a small batch of photos so you can try to run the code yourself without needing to find your own dataset.

Now in the repo you can also see the output of the code and the input faces with its encodings. 
