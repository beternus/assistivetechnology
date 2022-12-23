//Aqui usamos a biblioteca OpenCV, uma biblioteca open source para visão computacional, para poder acessar a camera do celular

import cv2
video = cv2.VideoCapture()
ip = "" //inserir o IP que aparece na tela do celular quando iniciado o servidor
video.open(ip)

while True:
check, image = video.read()
cv2.imshow("image",image)
cv2.waitKey(1)

//Ao executar o programa, o  computador irá abrir uma tela no desktop replicando o que 
//aparece na tela do celular a partir da camera do celular
