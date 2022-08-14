import math
from PIL import Image
from audioop import avg
from itertools import count
from operator import ge, le
from tracemalloc import start
from turtle import width


class Pixlr:
    
    def __init__(self, target):
        self.im = Image.open(target)
        self.stepper = 0
        self.doubler = 1

    def show(self):
        self.im.show()    
  
    def get_box_length(self,box_num):
        box_width = self.im.width // box_num
        box_height = self.im.height // box_num
        return [box_width, box_height]

    def paint_box(self, color, box):
        start_x, start_y, width, height = box
        pix = self.im.load()

        for x in range(start_x,width):
            for y in range(start_y,height):
                pix[x,y] = (color[0], color[1],color[2])


    # https://sighack.com/post/averaging-rgb-colors-the-right-way
    def average_pix(self, box):
        # init setup
        red = 0
        green = 0
        blue = 0
        pixels = self.im.load()
        start_x, start_y, width, height = box
        total_pix = 0

        # gathering color totals
        for x in range(start_x, width):
            for y in range(start_y, height):
                red += pixels[x, y][0]
                green += pixels[x, y][1]
                blue += pixels[x, y][2]
                total_pix += 1

        # accounting for nonsquare images
        if total_pix == 0:
            total_pix = width - start_x if (width - start_x) > (height - start_y) else height - start_y
            total_pix *= total_pix

        # calculating average
        avg_squared = [red**2, green**2, blue**2]
        avg_rt = list(map(lambda x: int(math.sqrt(x)//total_pix), avg_squared))

        return(avg_rt)

    def single_iteration(self, x, y, box_length):
        for x_axis in range(0, self.im.width, box_length):
            for y_axis in range(0, self.im.height, box_length):
                box = [x, y, x + box_length, y + box_length]
                while box[2] > self.im.width:
                    box[2] -= 1
                while box[3] > self.im.height:
                    box[3] -= 1
                avg = self.average_pix(box)
                self.paint_box(avg, box)
                y += box_length
            x += box_length
            y = 0

    def multi_iteration(self, num):
        """Performs 'num' instances of pixelation on a given image
        """
        if num < 1:
            self.im.show()
            return
        box_size = 1
        for count in range(0, num):
            box_size *= 2
            self.single_iteration(0, 0, box_size)