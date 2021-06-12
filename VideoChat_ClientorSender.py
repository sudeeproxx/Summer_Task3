{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a30e283",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "import socket\n",
    "import numpy\n",
    "import cv2\n",
    "\n",
    "cap=cv2.VideoCapture('https://192.168.29.160:8080/video')\n",
    "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n",
    "s.connect((\"192.168.56.1\",1237))\n",
    "\n",
    "while True:\n",
    "    ret,photo=cap.read()\n",
    "    cimg=cv2.resize(photo,(540,430))\n",
    "    simg=cv2.imencode(\".jpg\",cimg)[1].tobytes()\n",
    "    s.sendall(simg)\n",
    "    \n",
    "    data=s.recv(90456)\n",
    "    arg=numpy.fromstring(data,numpy.uint8)\n",
    "    img=cv2.imdecode(arg,cv2.IMREAD_COLOR)\n",
    "    fimg=cv2.resize(photo,(200,150),3)\n",
    "    if type(img) is type(None):\n",
    "        pass\n",
    "    else:\n",
    "        img[:150,:200]=fimg\n",
    "        cv2.imshow('client',img)\n",
    "        if cv2.waitKey(1)==13:\n",
    "            break\n",
    "cv2.destroyAllWindows()\n",
    "cap.release()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
