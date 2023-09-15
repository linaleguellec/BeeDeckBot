# Presentation 

# Files organization 
- main.py : main file to run 
- tesYOLOv8 : only an algorithm to test the identification method with YOLOv8 instead of my identification method while keeping trajectory tracking with DeepSort. 
- detector.py : contains my own bee detection method.  
- tracker.py : contains a class written by [this developer] (https://github.com/computervisioneng/object-tracking-yolov8-deep-sort.git) to make it easier to use DeepSort in the main.py file. 
-deep_sort : contains [this pakedge](https://github.com/computervisiondeveloper/deep_sort) = trajectory tracking algorithms. 
 
# User guide 
- Open the main.py file.
- In the code, specify the path to your bee video in MP4 format. 
- Run code.
- A window appears with the first frame of your video. Select the area of interest like [this example : ](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/recadrage.jpg)
- Press enter when you are sure of your zone selection. 
- The window will disappear and a [second window](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/separation.jpg) will be opened. It's the first cropped image of your video. 
- Delimit the upper and lower parts of the flight chamber by clicking on the metal bar separating the 2 parts (as shown in this example). The upper part is the image reflected by the mirror.  
- When you are sure of your boundary, press enter.  
- Tracking's calculations will begin. At the end of the calculations, graphics and 3D animation of the bee's trajectory will appear. You can press escape at any time if the calculation time is too long. In this case, the trajectory shown on the final graph will be only a part of the entire trajectory.
- Press the p key on the keyboard to pause calculations. Press p again to resume. 
- Set the DEBUG variable to 1 if you want to see the bee identification steps. If not, set DBUG to 0.  




# Sources 

I took inspiration from [this project](https://github.com/computervisioneng/object-tracking-yolov8-deep-sort.git). 

This project tracks objects using YOLOv8 for identification and deepSort for trajectory tracking. 
My project tracks bees using deepSort but not YOLOv8. 
So I took the structure of this project and replaced the YOLOv8 part of my own method of bee identification. 

      
## Deep Sort

The developer of [this project](https://github.com/computervisioneng/object-tracking-yolov8-deep-sort.git) is working on [this fork](https://github.com/computervisiondeveloper/deep_sort) from deep sort official implementation.


# The main problems with my algorithms 

# How to improve my algorithms ?  


