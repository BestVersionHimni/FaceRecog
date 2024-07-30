# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import time
import sys

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Aleksandr\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 3")
chrome_options.add_argument("--lang=en-US")
chrome_options.add_experimental_option("detach",True)

PATH = r"C:\\Users\\Aleksandr\\Desktop\\download photos\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
driver_service = Service(executable_path=PATH)#
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

ru_months = {
    'янв': 'Jan',
    'фев': 'Feb',
    'мар': 'Mar',
    'апр': 'Apr',
    'мая': 'May',
    'июн': 'Jun',
    'июл': 'Jul',
    'авг': 'Aug',
    'сен': 'Sep',
    'окт': 'Oct',
    'ноя': 'Nov',
    'дек': 'Dec'
}

def Get_Albums_Data():
    with open("dic_album.txt", "r", encoding="utf-8") as file:
        text = file.readline().split(";")

    album_dic = [element.strip("[]").split(", ") for element in text]
    album_dic = [[item.strip("'") for item in sublist] for sublist in album_dic]

    return album_dic


def Get_Album_Date(album):

    driver.get(album)

    time.sleep(3)

    amount = Get_photos_amount()
    time.sleep(1)

    photos = driver.find_elements(By.CSS_SELECTOR,".vkuiDiv a")
    photos[0].click()

    time.sleep(3)

    date_use = driver.find_element(By.CSS_SELECTOR, ".rel_date").text.split(" ")
    date_use[1] = ru_months[date_use[1]]


    driver.find_element(By.CSS_SELECTOR, ".pv_close_btn").click()


    date_use = str("-".join(date_use))
    return date_use, amount

def Get_URLs_Photos():
    n=1
    src=[]
    
    urls = driver.find_elements(By.CSS_SELECTOR, ".PhotosPagePhotoGridVirtualItem-module__img--Qdmgl")

    last_height = driver.execute_script("return document.body.scrollHeight")
    current_height = driver.execute_script("return window.pageYOffset + window.innerHeight")

  
    while last_height - current_height > 300:
            
        urls = driver.find_elements(By.CSS_SELECTOR, ".PhotosPagePhotoGridVirtualItem-module__img--Qdmgl")
        for element in urls:
            src.append(element.get_attribute("src"))


        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
        current_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
        last_height = driver.execute_script("return document.body.scrollHeight")
    duplicates = src
    unique_urls = list(set(duplicates))

    if len(unique_urls) == 0:
        urls = driver.find_elements(By.CSS_SELECTOR, ".PhotosPagePhotoGridVirtualItem-module__img--Qdmgl")
        for element in urls:
            src.append(element.get_attribute("src"))
        duplicates = src
        unique_urls = list(set(duplicates))

    return unique_urls

def Download_Photos(urls, name_directory, name_of_files):

    directory = name_directory
    name_prefix = name_of_files

    os.makedirs(directory, exist_ok=True)

    # Download each image
    for n, image_url in enumerate(urls):
        # Send a GET request to the image URL
        
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Define the file path using the index
            file_path = os.path.join(directory, f'{name_prefix}-{n}.jpg')
            
            # Open a file in binary write mode
            with open(file_path, 'wb') as file:
                # Write the content of the response (i.e., the image) to the file
                file.write(response.content)
        # print(f'Image {n} successfully downloaded and saved as {file_path}')
        else:
            print(f'Failed to retrieve image {n}. Status code: {response.status_code}')

    return

def Get_photos_amount():
    
    photos_amount = driver.find_element(By.CSS_SELECTOR, "h4").text
    return photos_amount

albums = Get_Albums_Data()


for album in albums:

    Date_of_album, photos_amount = Get_Album_Date(album=album[0])
    Name_of_album = f"{album[1]}-{photos_amount}"
    URLs_photos = Get_URLs_Photos()
    Download_Photos(urls=URLs_photos,name_directory=Name_of_album,name_of_files=Date_of_album)

    



