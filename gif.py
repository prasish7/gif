
import imageio.v3 as iio
file_name = ['dino1.png', 'dino2.png', 'dino3.png', 'dino4.png']
images = []
for file in file_name:
    images.append(iio.imread(file))

iio.imwrite('dino.gif', images, duration=500 , loop=0)

