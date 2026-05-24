from wand.image import Image

X_STEP = 116 #117
Y_STEP = 115

X_OFFSET = 192
Y_OFFSET = 30

REDUCTION_X = 8
REDUCTION_Y = 6


NUM_X = 8
NUM_Y = 6

SIZE = 85
SOURCE_FILE = 'sculpt-icons.jpg'

def crop(src_img, out_img, xn, yn):
  left = X_OFFSET + (xn * X_STEP) + REDUCTION_X
  top = Y_OFFSET + (yn * Y_STEP) + REDUCTION_Y

  ny = Image(filename = src_img)
  ny.crop(left, top, width=SIZE-REDUCTION_X, height=SIZE-REDUCTION_X)
  ny.save(filename = out_img)


if __name__ == "__main__":
  for xn in range(NUM_X):
    for yn in range(NUM_Y):
      out = "out_" + str(xn) + "_" + str(yn) + ".png"
      crop(SOURCE_FILE, out, xn, yn)

