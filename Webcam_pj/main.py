#!/usr/bin/env python3
"""
Webcam project
"""

import cv2
import sys

def main():
    print("face detection program")
    print("press esc to exit")
    
    cap = None
    try:
        # 웹캠 연결
        print("connect webcam")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("failed open ewbcam")
            return -1
        
        # 메모리 누수 방지: 버퍼 크기 최소화
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        
        print("success open webcam!")
        
        # 얼굴 검출기 로드
        face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')
        if face_cascade.empty():
            print("can`t load face detector")
            return -1
        
        print("success program")
        
        # 창 생성 및 설정
        window_name = 'Webcam project'
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 640, 480)
        cv2.moveWindow(window_name, 100, 100)
        
        while True:
            # 프레임 읽기
            ret, frame = cap.read()
            if not ret:
                print("error frame")
                break
            
            # 얼굴 검출
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 3, minSize=(30, 30))
            
            # 얼굴에 사각형 그리기
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, 'FACE', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            # 프레임 표시
            cv2.imshow(window_name, frame)
            
            # 키 입력 처리
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                print("exit program")
                break
            elif key == ord('s'):  # S키로 스크린샷
                filename = f"screenshot.jpg"
                cv2.imwrite(filename, frame)
                print(f"Capture: {filename}")
            elif key != 255:
                print(f" {chr(key) if 32 <= key <= 126 else key}")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return -1
    
    finally:
        # 리소스 해제 보장 (예외 발생 시에도 실행)
        if cap is not None:
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    sys.exit(main()) 