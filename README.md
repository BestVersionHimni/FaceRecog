I wanted to download all the photos from one website for personal analysis but had a problem that i coundn't download in bulk from the website. 
I had to come up with own script that would download all of it. 

   1. I had extracted all the URLs of all the albums with photos, so in next step i can go through those to download photos.
   2. I extracted the date of the uploaded image(This is used for naming and also a time point to estimate possible age of me in the photos)
   3. I have also extracted how much photos are in each album so i can check if all the photos were downloaded
   4. I have created a script that was getting the album then extracting all the URLs of photos for next download.
   5. Here now I had to find all the photos where I could see my face but there are more than 5000 photos in total. So it would take significatnt amount of time to proccess it myself manually.
   6. My friend advised me to create a face recognition script that would find all the photos of me and pull it up together.
   7. In the repository now you can see the final solution that i have used to perform all these steps and finally find all my photos.


Main problem that i have met was the my face in different ages. Photos itself contain a period of 5-6 years so my faces has changed significantly over the time. 
I doubted the possibility to extract all my photos with example photo of me 13 years old.
  i have solved it as following:
    1. I have extracted all the faces from the all the photos(Extracted more then 9 000 individual faces).
    2. I got embeddings of all the faces(took a while😅)
    3. I manually found 4 my own faces to start with
    4. Searched for similar faces over the whole directory with all the extracted faces. so i can get more examples of my face. Then repeated this step several times until i could find any new face of me.(This allowed me to have the most accurate sample of my face)
    5. Now i'm at the final step where I will use this samples to find all the photos with me and move it to new directory. 

    
P.S. I also attached a small batch of photos so you can try to run code yourself without a need to find your own dataset. 
