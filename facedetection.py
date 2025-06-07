import cv2

yaziTipi = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webCam = cv2.VideoCapture(0)

if not webCam.isOpened():
    print("Kamera Algilanamadi")
    exit()

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video", 1600, 900)

cikis = False
fullscreen_toggle = False
while not cikis:
    ret, cam = webCam.read()

    if ret:

        cam = cv2.resize(cam, (1600, 900))

        cam = cv2.flip(cam, 1)

        renkCevir = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
        font = yaziTipi.detectMultiScale(renkCevir, scaleFactor=1.3, minNeighbors=2)

        for (x, y, w, h) in font:
            cv2.rectangle(cam, (x, y), (x + w, y + h), (0, 255, 0), 2)

        yazi = "Algilanan Yuz Sayisi = " + str(len(font))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(cam, yazi, (20, 30), font, 0.5, (255, 0, 0), 1)

        cv2.imshow("Video", cam)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cikis = True
            break

webCam.release()
cv2.destroyAllWindows()
