import cv2
import argparse
import os
import sys
import glob
import ntpath
from pathlib import Path

import progress_bar

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

parser = argparse.ArgumentParser()
parser.add_argument('--input-folder', type=str, default=ROOT, help='input folder path')
parser.add_argument('--output-folder', type=str, default=ROOT, help='output folder path')

args = parser.parse_args()


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def extract_frames(input_folder_path, output_folder_path):
    video_files = glob.glob(os.path.join(input_folder_path, "*.mp4"))

    for video_file in video_files:
        video_name = path_leaf(video_file).split('.')[0]
        cap = cv2.VideoCapture(video_file)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        extract_frame_rate = fps * 2

        print()
        print("Video name: {}".format(video_name))
        
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            progress_bar.progressBar(frame_count, total_frame)

            if frame_count % extract_frame_rate == 0:
                output_video_path = os.path.join(output_folder_path, "{}_frame{}.jpg".format(video_name, frame_count))
                cv2.imwrite(output_video_path, frame)

            frame_count += 1


        cap.release()

        print()



    


if __name__ == "__main__":
    input_folder = args.input_folder
    output_folder = args.output_folder
    extract_frames(input_folder, output_folder)