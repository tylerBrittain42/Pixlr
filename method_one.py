from audioop import avg
from itertools import count
from operator import ge, le
from tracemalloc import start
from turtle import width
from PIL import Image
import math

# box = x,y,height,length


class Pixlr:
    
    def __init__(self, target,width):
        self.im = Image.open(target)
        self.width = width
        self.total_squares = self.width ** 2  

    def show(self):
        self.im.show()       

    def paint_boxes(self):
        num = self.total_squares
        row_num = int(math.sqrt(num))
        col_num = int(math.sqrt(num))
        total_box = num
        
        # Using cur_box to keep track of box being filled
        # Assume we start at top right and work right then down
        cur_x = 1
        cur_y = 0

        i = 255
        j = 0
        
        box_width, box_height = self.get_box_size(row_num)
        

        for row in range(row_num):
            for col in range(col_num):
                box = [cur_x,cur_y, cur_x + box_width, cur_y + box_height]
                while box[2] >= self.im.width:
                    box[2] -= 1
                print(box)
                print(self.im.width)
                cur_avg = self.average_pix(box)
                self.paint_box([i,j,0],box)
                # [i,j,0]
                if i == 255:
                    i = 0
                    j = 255
                else:
                    i = 255
                    j = 0
                print(f'row:{row} col:{col}\nx:{cur_x},y:{cur_y}\navg: {cur_avg}\n')
                cur_x += box_width
            cur_y += box_height
            cur_x = 0

        # for row in range(row_num):
        #     for col in range(col_num):
        #         box = [cur_x,cur_y, cur_x + box_width, cur_y + box_height]
        #         paint_box(im,[255,0,0],box)
        #         print(f'x:{cur_x} y:{cur_y}')
        #         cur_x += box_width
        #     cur_x = 0
        #     cur_y += box_height
        # print(im.width)
        print(box_width)


        
    def get_box_size(self,box_num):
        box_width = self.im.width // box_num
        box_height = self.im.height // box_num
        return [box_width, box_height]


    def paint_box(self, avg_color, box):

        start_x, start_y, width, height = box
        

        pix = self.im.load()
        for x in range(start_x,width):
            for y in range(start_y,height):
                pix[x,y] = (avg_color[0], avg_color[1],avg_color[2])
                # print('a')


    # https://sighack.com/post/averaging-rgb-colors-the-right-way
    def average_pix(self, box):

        # counters
        red = 0
        green = 0
        blue = 0

        # init setup
        pixels = self.im.load()
        start_x, start_y, width, height = box
        total_pix = width * height

        # gathering color totals
        for x in range(start_x,width):
            for y in range(start_y,height):
                red += pixels[x,y][0]
                green += pixels[x,y][1]
                blue += pixels[x,y][2]
        
        # calculating average
        avg_squared = [red**2, green**2, blue**2]
        avg_rt =list(map(lambda x: int(math.sqrt(x)//total_pix), avg_squared))

        return(avg_rt)


