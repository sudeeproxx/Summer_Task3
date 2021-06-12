{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bf347902",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\gupta\\anaconda3\\lib\\site-packages\\numpy\\_distributor_init.py:30: UserWarning: loaded more than 1 DLL from .libs:\n",
      "C:\\Users\\gupta\\anaconda3\\lib\\site-packages\\numpy\\.libs\\libopenblas.GK7GX5KEQ4F6UYO3P26ULGBQYHGQO7J4.gfortran-win_amd64.dll\n",
      "C:\\Users\\gupta\\anaconda3\\lib\\site-packages\\numpy\\.libs\\libopenblas.PYQHXLVVQ7VESDPUVUADXEVJOBGHJPAY.gfortran-win_amd64.dll\n",
      "C:\\Users\\gupta\\anaconda3\\lib\\site-packages\\numpy\\.libs\\libopenblas.WCDJNK7YVMPZQ2ME2ZZHJJRJ3JIKNDB7.gfortran-win_amd64.dll\n",
      "  warnings.warn(\"loaded more than 1 DLL from .libs:\\n%s\" %\n"
     ]
    }
   ],
   "source": [
    "import socket\n",
    "import numpy as np\n",
    "import cv2\n",
    "\n",
    "cap=cv2.VideoCapture(0)\n",
    "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n",
    "ip=\"192.168.56.1\"\n",
    "port=1237\n",
    "s.bind((ip,port))\n",
    "s.listen()\n",
    "session,add=s.accept()\n",
    "\n",
    "while True:\n",
    "    data=session.recv(90456)\n",
    "    arg=np.fromstring(data,dtype=np.uint8)\n",
    "    photo=cv2.imdecode(arg,cv2.IMREAD_COLOR)\n",
    "    ret,frame=cap.read()\n",
    "    fi=cv2.resize(frame,(200,150),3)\n",
    "    if type(photo) is type(None):\n",
    "        pass\n",
    "    else:\n",
    "        photo[:150,:200]=fi\n",
    "        cv2.imshow('server',photo)\n",
    "        if cv2.waitKey(1)==13:\n",
    "            break\n",
    "    \n",
    "    videosend=cv2.imencode('.jpg',frame)[1].tobytes()\n",
    "    session.sendall(videosend)\n",
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
