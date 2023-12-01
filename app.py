import cv2

def show_camera():
    window_title = "CSI Camera"
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    video_capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    video_capture.set(cv2.CAP_PROP_BRIGHTNESS, 34)
    print("BRIGHTNESS",video_capture.get(cv2.CAP_PROP_BRIGHTNESS))
    video_capture.set(cv2.CAP_PROP_CONTRAST, 34)
    print("CONTRAST",video_capture.get(cv2.CAP_PROP_CONTRAST))
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, frame = video_capture.read()
                # Check to see if the user closed the window
                # Under GTK+ (Jetson Default), WND_PROP_VISIBLE does not work correctly. Under Qt it does
                # GTK - Substitute WND_PROP_AUTOSIZE to detect if window has been closed by user
                frameR = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    cv2.imshow(window_title, frameR)
                else:
                    break 
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    show_camera()
