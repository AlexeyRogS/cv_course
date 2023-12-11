import os
import cv2
import pafy
import shutil
import os.path as osp
from pytube import YouTube



if __name__ == "__main__":
    # shutil.rmtree("input_files", ignore_errors=True)
    # os.makedirs("input_files")
    # url = 'https://youtu.be/BBJa32lCaaY'
    # video = pafy.new(url)
    # print(video)
    # best = video.getbest()
    # print(best.resolution, best.extension)

    # best.download(filepath=f'./input_files/video.{best.extension}')

    cap = cv2.VideoCapture(f'./input_files/video.mp4')

    i = 0
    while cap.isOpened():

        # Считываем новый кадр и success code.
        ret, frame = cap.read()
        if not ret:
            print("Hello")
            break
        else:
            print(frame.shape)
        # cv2.imshow('frame', frame)
        # cv2_imshow(frame)

        # if i == 3:
        #   break
        # i += 1

    cap.release()
    cv2.destroyAllWindows()