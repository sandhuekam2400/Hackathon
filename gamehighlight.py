import pyautogui
import time
import keyboard
import os  
import sys 
import queue
from PIL import Image
x=0 
current_directory = os.getcwd()
q=queue.Queue(maxsize=18000)
if not os.path.exists(current_directory+ '/frames'):
    os.makedirs(current_directory+ '/frames')

while True:
    # implementing a queue for the screenshots
    
    
    while keyboard.is_pressed('q') == True:
        screenshot =pyautogui.screenshot('screenshot.png')
        x+=1
        screenshot.save(os.path.join(current_directory+ '/frames','screenshot_{:06d}.png'.format(x)))
        q.put((current_directory+ '/frames/screenshot_{:06d}.png'.format(x)))
        
        # time.sleep(0.00000000000000016)
        if x>1800:
            x=0
            break
    if keyboard.is_pressed('a'):break
import cv2
# import os
# import queue

def images_to_video_from_queue(image_queue, video_name, fps):
    if image_queue.empty():
        raise ValueError("The image queue is empty")
    
    # Fetch the first image to get the dimensions
    first_image_path = image_queue.get()
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Write the first image
    video.write(frame)

    # Write remaining images
    while not image_queue.empty():
        image_path = image_queue.get()
        video.write(cv2.imread(image_path))
    video.release()
# Example usage
image_folder = current_directory+ '/frames'
image_queue = queue.Queue()

# Enqueue image paths
# for img in sorted(os.listdir(image_folder)):
#     if img.endswith(".png") or img.endswith(".jpg"):
#         image_queue.put(os.path.join(image_folder, img))

video_name = 'output_video.avi'
fps = 60  # Frames per second

images_to_video_from_queue(q, video_name, fps)
