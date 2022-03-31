# to upload to cloud
import creds
import cloudinary
import cloudinary.uploader
import cloudinary.api
from downloader import downloader
import os

cloudinary.config(
    cloud_name=creds.cloud_name,
    api_key=creds.api_key,
    api_secret=creds.api_secret
)

count = 148


with open(r'C:\Users\hardik\OneDrive\Documents\Python Scripts\discord clip poster\Scraper\db.txt') as file:
    lines = [line.rstrip('\n') for line in file]
    for reel in lines:
        downloader(reel, f'clip_{count}.mp4')
        print(f'downloaded reel number:{count}')
        try:
            cloudinary.uploader.upload_large(
                fr"C:\Users\hardik\OneDrive\Documents\Python Scripts\discord clip poster\ToCloud\download\clip_{count}.mp4", resource_type="video", public_id=f"clip-{count}")
            print(f'uploaded clip {count}')
        except Exception as e:
            print('oops')
        os.remove(
            fr"C:\Users\hardik\OneDrive\Documents\Python Scripts\discord clip poster\ToCloud\download\clip_{count}.mp4")
        print(
            f'remvoed clip-{count} to save space and it has been uploaded to the cloud!')
        count += 1

print(f'uploaded all {count} files succsesfully!')

assests = dict(cloudinary.api.resources(
    type="upload", resource_type='video', max_results=200))
url_file = open(
    r'C:\Users\hardik\OneDrive\Documents\Python Scripts\discord clip poster\ToCloud\secure_urls.txt', 'a+')
for item in assests['resources']:
    url_file.write(item['secure_url']+"\n")
print('done')
