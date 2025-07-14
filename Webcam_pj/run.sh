#!/bin/bash

# OpenCV 설치 확인 및 자동 설치
python3 -c "import cv2" 2>/dev/null || pip install opencv-python

# 프로그램 실행
python3 main.py 