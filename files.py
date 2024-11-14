import os
import urllib.request

# Create a directory for the YOLO files if it doesn't exist
os.makedirs("yolo", exist_ok=True)

# URLs for the files needed
files = {
    "yolo/yolov3.weights": "https://pjreddie.com/media/files/yolov3.weights",
    "yolo/yolov3.cfg": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
    "yolo/coco.names": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
}

# Function to download files
def download_file(filepath, url):
    print(f"Downloading {filepath}...")
    urllib.request.urlretrieve(url, filepath)
    print(f"Downloaded {filepath}")

# Download each file
for filepath, url in files.items():
    if not os.path.exists(filepath):
        download_file(filepath, url)
    else:
        print(f"{filepath} already exists, skipping download.")

print("All files are downloaded and ready!")
