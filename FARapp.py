from flask import Flask, request, render_template
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/TakePic', methods=['POST'])
def TakePic():


    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # 0 is the default camera index

    # Check if the camera is opened
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Capture an image
    ret, frame = cap.read()

    # Save the image to a file
    cv2.imwrite("image.jpg", frame)

    # Release the camera
    cap.release()

  

if __name__ == '__main__':
    app.run(debug=True)