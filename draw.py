import cv2

im = cv2.imread("graf.png")

points = [(15, 25), (15, 448)]

length = 355
segments = 20
tick_length = 5
text_distance = 3
text_y_offset = 5

delta = length / segments

for p in points:
  cv2.line(im, p, (p[0], p[1] + length), color=(0, 0, 0))
  for perc in range(0, 101, 10):
    x = p[0] + tick_length + text_distance
    perc_val = 100 - perc # Invert
    y = int(p[1] + (perc / 100.0) * length)
    cv2.putText(im, "%d" % perc_val, (x, y + text_y_offset), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0)) # , fontFace, fontScale, color
    cv2.line(im, (p[0], y), (p[0] + tick_length, y), color=(0, 0, 0))

cv2.imwrite("out.png", im)
