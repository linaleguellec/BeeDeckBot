# Presentation  
This README explains how to set up the electronics to control the motors. In particular, how to start and stop the robotic flower's motors using the manual switch and the RFID door switch. 


# User guide 
Once the metal structure has been assembled, install all the electronic circuits. Transfer the code in this folder to the Arduino UNO board. First, make sure that the electronic circuit without the RFID door is working. Press the manual switch once, the robotic flower target should move with random frequency and amplitude. Press a second time, and the target should stop and move to the position for the next start. 

## Electronics 
Here's the real and theoretical electronic circuit. I've placed the integrated switch of the RFID port and the manual switch in parallel. In this way, the motors of the robotic flower can be controlled either manually by the manual switch, or automatically by the RFID door switch. 
![](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/schemaElec.png)
![](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/elecGlobale.jpeg)
![](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/elecZoom.jpeg)

## RFID gate 
- Install the RFID door according to this [technical documentation.](https://github.com/linaleguellec/BeeDeckBot/tree/main/technicalDocumentation/RFIDgate)  

- Attach wires to the back of the RFID door controller as follows. These are the wires for the RFID door's built-in switch. Indeed, as soon as the RFID door detects a bee, the door controller quickly closes its switch. Here's the electronic design from the technical documentation.
![](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/RFID1.jpg)
![](https://github.com/linaleguellec/BeeDeckBot/blob/main/imgsForReadMe/RFID2.jpg)

- For more information about the technical operation of the RFID door, please refer to the ["technical documentation" folder.](https://github.com/linaleguellec/BeeDeckBot/tree/main/technicalDocumentation/RFIDgate)

## Robotic flower control
Please refer to my internship report for an explanation of the robotic flower's motor control algorithm. 

