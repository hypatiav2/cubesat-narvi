# Hi, this is Team Narvi's repository for the 2021-2022 MIT BWSI x SWE Build a CubeSat Challenge

## What is a CubeSat? 
A CubeSat, or cube satellite, is a  a common type of nanosatellite, built in cube form with dimensions of 10 cm × 10 cm × 10 cm, 
with a mass of no more than 1.33 kilograms (2.9 lb) per unit.
This year's CubeSat mission objective was to design and build a prototype of a CubeSat that could scan the ocean from an aerial view and process pictures to detect macro-plastics.
We built our CubeSat using a Raspberry Pi 4 Model B, the Adafruit BNO055 IMU, PiCam, and standardized BWSI acrylic panels. In this repository is the code for our CubeSat mission, from launch to finish, 
as well as pictures from our test demo using everyday plastics at home. 

- Team Narvi, American High School in CA
- Award: Best Overall Presentation

## Challenge Materials
- [Design Review Presentation](https://docs.google.com/presentation/d/1-VkZVkaJapbH8x2QFXUjJGAdzKCbqDXV68sjaDp1dPQ/edit?usp=sharing)
- [Final Project Presentation](https://docs.google.com/presentation/d/1QwET54YE8lvtQUq55Y8uikWgzIASpIw4OvfZEroFX04/edit?usp=sharing)

### Our cubesat:
<img src="cubesat_picture.jpg" width="600" padding="10px"/>

### Plastic Detection Process
grayscale -> blur -> thresholding -> outlines -> bounding box (if rgb different from 'ocean' background)
<img src="detection_process_slide.jpg" width="600" padding="10px"/>



