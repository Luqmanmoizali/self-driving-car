# Self-Driving Car Project

## Overview
A self-driving car using Arduino Uno, HC-05, L298 motor driver, and a mobile camera for route visualization. Utilized Python for real-time image processing, lane detection, and autonomous navigation. Integrated machine learning for obstacle detection and control commands.

## Setup
### Hardware Requirements:
- Arduino Uno
- HC-05 Bluetooth Module
- L298 Motor Driver
- Motors and Wheels
- Power Supply
- Chassis for the car
- Mobile phone with IP Webcam app installed

### Software Requirements:
- Python 3.x
- OpenCV
- Pygame
- Scikit-learn
- Joblib
- NumPy
- Scikit-image

### Steps:
1. **Hardware Assembly:**
   - Connect the motors to the L298 motor driver.
   - Connect the L298 motor driver to the Arduino Uno.
   - Connect the HC-05 Bluetooth module to the Arduino Uno.
   - Assemble all components on the car chassis.
   - Power up the Arduino and the motor driver.

2. **Install Software:**
   - Install the required Python libraries:
     ```bash
     pip install opencv-python pygame scikit-learn joblib numpy scikit-image
     ```

3. **IP Webcam Setup:**
   - Install the IP Webcam app on your mobile phone.
   - Start the server and note the IP address it provides.

4. **Clone the Repository:**
   - Clone this GitHub repository to your local machine:
     ```bash
     git clone https://github.com/yourusername/self-driving-car.git
     cd self-driving-car
     ```

## Usage
1. **Train the Model:**
   - Run the `trainsdc.py` script to train the machine learning model:
     ```bash
     python trainsdc.py
     ```

2. **Run the Self-Driving Car:**
   - Start the IP Webcam app on your mobile phone and ensure it’s broadcasting.
   - Update the `url` variable in `sdc.py` and `drivercar.py` to match the IP address from the IP Webcam app.
   - Run the `sdc.py` script to start the real-time control interface:
     ```bash
     python sdc.py
     ```
   - Run the `drivercar.py` script to start the autonomous navigation:
     ```bash
     python drivercar.py
     ```

3. **Control Commands:**
   - Use the keyboard to control the car manually when running `sdc.py`:
     - UP arrow: Move forward
     - DOWN arrow: Move backward
     - LEFT arrow: Turn left
     - RIGHT arrow: Turn right
     - 'z': Capture image for red light
     - 'g': Capture image for green light
     - 'p': Capture image for stop sign
     - 's': Stop the car

## License
This project is licensed under the MIT License - see the LICENSE file for details.
