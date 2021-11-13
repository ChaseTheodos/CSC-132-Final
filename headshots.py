import cv2
import train_model

def headshots():
    # initial variable setup to store images under the current
    # users name that is being added to the dataset
    # currently set to Event for CSC132-Final exhibition
    name = 'Event'

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("press space to take a photo", cv2.WND_PROP_FULLSCREEN)
    cv2.resizeWindow("press space to take a photo", 500, 300)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab the frame.")
            break
        cv2.imshow("Press space to take a photo", frame)

        k = cv2.waitKey(1)
        if k%256 == 113:
            # Q pressed
            print("Closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = f"/home/pi/CSC132-Final/dataset/{name}/image_{img_counter}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            img_counter += 1

    # cleanup
    cam.release()
    cv2.destroyAllWindows()

    # call the train function from train_model.py
    train_model.train()
