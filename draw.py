#!/usr/bin/env python
"""
Draws one ore more Y axes on a copy of the input image.
With the input image, provide the corresponding JSON file.
E.g. for input.png write a input.png.json with example contents:
{
  "points": [(0, 0), (0, 200)],
  "lengths" [200, 240]
}
"""

import argparse
import cv2
import json
import os

def add_y_axis(input_filename, output_filename, points, lengths):
  im = cv2.imread(input_filename)
  # TODO: move to args.
  segments = 20
  tick_length = 5
  text_distance = 3
  text_y_offset = 5

  for i, point in enumerate(points):
    p = tuple(point)
    length = lengths[i]
    delta = length / segments
    cv2.line(im, p, (p[0], p[1] + length), color=(0, 0, 0))
    for perc in range(0, 101, 10):
      x = p[0] + tick_length + text_distance
      perc_val = 100 - perc # Invert
      y = int(p[1] + (perc / 100.0) * length)
      cv2.putText(im, "%d" % perc_val, (x, y + text_y_offset),
                  cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0))
      cv2.line(im, (p[0], y), (p[0] + tick_length, y), color=(0, 0, 0))

  cv2.imwrite(output_filename, im)

if __name__ == '__main__':
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--image", required=True, dest="image",
                  help="Path to the input image.")
  ap.add_argument("-o", "--output", default="out.png",
                  dest="output",
                  help="Path to the output image.")
  args = ap.parse_args()
  json_file = args.image + ".json"
  if not os.path.exists(json_file):
    raise Exception("Missing input json file " + json_file)

  with open(json_file, "r") as f:
    data = json.load(f)
  add_y_axis(args.image, args.output, data["points"], data["lengths"])
