from skimage import io
import joblib
import time
import serial
import numpy as np
import threading
from os import listdir
from os.path import isfile, join
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import cv2

def detect_lanes(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    
    edges = cv2.Canny(blur, 50, 150)
    
    
    height, width = image.shape[:2]
    mask = np.zeros_like(edges)
    roi = np.array([[
        (0, height),
        (width/2, height/2),
        (width, height)
    ]], dtype=np.int32)
    cv2.fillPoly(mask, roi, 255)
    masked_edges = cv2.bitwise_and(edges, mask)
    
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)
    
   
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    return image

def process_frame(img):
    
    img_with_lanes = detect_lanes(img)

    img_with_lanes = cv2.resize(img_with_lanes, (320, 240))
    
    
    cv2.imshow('Lanes', img_with_lanes)
    cv2.waitKey(1)

def drive():
    url = "http://192.168.0.101:8080/shot.jpg"  
    s = serial.Serial('COM3', 9600)  
    time.sleep(2)

    x = []
    y = []

    files_name = [f for f in listdir('Images') if isfile(join('Images', f))]

    for name in files_name:
        img = cv2.imread(join('Images', name))
        img = cv2.blur(img, (5, 5))
        retval, img = cv2.threshold(img, 201, 255, cv2.THRESH_BINARY)
        img = cv2.resize(img, (24, 24))
        image_as_array = np.ndarray.flatten(np.array(img))
        x.append(image_as_array)
        y.append(name.split('_')[0])

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    scaler.fit(xtrain)
    xtrain = scaler.transform(xtrain)
    xtest = scaler.transform(xtest)

    alg = MLPClassifier(solver='lbfgs', alpha=100.0, random_state=1, hidden_layer_sizes=50, max_iter=1000)

    alg.fit(xtrain, ytrain)
    print(alg.score(xtest, ytest))

    f = 'mymodel.mkl'
    joblib.dump(alg, f)
    alg = joblib.load(f)

    def process_image():
        while True:
            img = io.imread(url)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            process_frame(img)

    def control_car():
        while True:
            img = io.imread(url)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            process_frame(img)

            img_copy = img.copy()

            img_copy = cv2.resize(img_copy, (320, 240))

            cv2.imshow('Detections', img_copy)
            cv2.waitKey(1)

            img = cv2.blur(img, (5, 5))
            _, img = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
            img = cv2.resize(img, (24, 24))
            _, img = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
            image_as_array = np.ndarray.flatten(np.array(img))

            result = alg.predict([image_as_array])[0]

            if result == 'forward':
                s.write(b'f')
                time.sleep(1)
                s.write(b's')
            elif result == 'right':
                s.write(b'r')
                time.sleep(1)
                s.write(b's')
            elif result == 'left':
                s.write(b'l')
                time.sleep(1)
                s.write(b's')
            elif result == 'redlight':
                s.write(b's')  
            elif result == 'greenlight':
                s.write(b'f')  
                time.sleep(1)
            elif result == 'stopsign':
                s.write(b's')  
                time.sleep(5)  
            else:
                s.write(b's')
                time.sleep(1)

            print(result)

    
    image_thread = threading.Thread(target=process_image)
    image_thread.daemon = True
    image_thread.start()

   
    control_thread = threading.Thread(target=control_car)
    control_thread.daemon = True
    control_thread.start()

    
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    s.close()
    cv2.destroyAllWindows()

print("Start Driving")
drive()