from audioop import avg
from itertools import count
from operator import ge, le
from tracemalloc import start
from turtle import width
from PIL import Image
import math



class Pixlr:
    
    # think i can remove width
    def __init__(self, target,width):

        # image attributes
        self.im = Image.open(target)
        self.stepper = 0
        self.doubler = 1

    def show(self):
        self.im.show()    


    def pixelate(self,n):
        n += 1

        
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
        total_pix = 0

        # gathering color totals
        for x in range(start_x,width):
            for y in range(start_y,height):
                # print(f'x:{x} y:{y}')
                red += pixels[x,y][0]
                green += pixels[x,y][1]
                blue += pixels[x,y][2]
                total_pix += 1
        
        # calculating average
        avg_squared = [red**2, green**2, blue**2]
        avg_rt =list(map(lambda x: int(math.sqrt(x)//total_pix), avg_squared))

        return(avg_rt)

    def iteration(self, x, y, box_size):
        for x_axis in range(0, self.im.height, box_size):
            for y_axis in range(0, self.im.width, box_size):
                box = [x,y, x + box_size, y + box_size]
                while box[2] > self.im.width:
                    box[2] -= 1
                while box[3] > self.im.height:
                    box[3] -= 1
                avg = self.average_pix(box)
                print(box)
                print(avg)
                print("-----------------")
                self.paint_box(avg,box)
                # print(f'x: {x}, y: {y}, {avg}')
                # print(f'x: {x}, y: {y}\n')
                # print(box)
                y += box_size
        
            x += box_size
            y = 0

def main():
    im = Pixlr('./sample/checker.jpeg',2)
    im.iteration(0,0,450)
    im.show()
    

if __name__ == '__main__':
    main()