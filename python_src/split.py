import math
import sys

import ffmpeg


def main(file_path, duration):
    duration = math.ceil(float(ffmpeg.probe(file_path)['streams'][0]['duration']))
    current = 0
    idx = 1
    while current < duration:
        start = current
        stream = ffmpeg.input(file_path, ss=start, t=duration)
        stream = ffmpeg.output(stream, f"python_src/yolo_strong_sort/splited/tmp{idx:0>4}.mp4", c='copy')
        ffmpeg.run(stream)
        idx += 1
        current += duration


if __name__ == "__main__":
    args = sys.argv
    main(args[1], args[2])
