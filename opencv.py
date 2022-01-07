
import cv2
import numpy as np


#cap = cv2.VideoCapture('street.avi') # crèer un objet VideoCapture à partir d'un fichier

cap = cv2.VideoCapture(1) # crèer un objet VideoCapture à partir d'une caméra

# Arrêt si l'objet est null
if (cap.isOpened()== False):
    print("Erreur dans la lecture du flux video")

# Lire jusqu'à la fin d'un fichier video ou sans fin pour la caméra
while(cap.isOpened()):

    # Capture frame par frame
    ret, frame = cap.read()
    if ret == True:

        # Afficher le frame
        cv2.imshow('Frame', frame)

        # Tappez 'q' pour arreter la lecture
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # sortir de la boucle
    else:
        break

#liberer l'objet VideoCapture
cap.release()

# Fermer tous les frames
cv2.destroyAllWindows()
