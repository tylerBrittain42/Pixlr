from audioop import avg
from itertools import count
from operator import ge, le
from tracemalloc import start
from turtle import width
from PIL import Image
import math

# box = x,y,height,length


def main():
    width = 3
    total_squares = width ** 2
    
    checker = Image.open('./sample/checker.jpeg')
    # pix = checker.load()
    # foo = checker.split()
    # print(pix[0,0])
    
    
    # print(im.size[0])

    # full image
    avg_color = average_pix(checker,[0,0,checker.height,checker.width])
    
    # partal(black)
    avg_color = average_pix(checker,[0,0,1,1])

    print(avg_color)

    # print(avg_color)
    # paint_box(checker,avg_color,[0,0,50,checker.width])
    # checker.show()

    
    paint_boxes(checker, total_squares)
    checker.show()

def paint_boxes(im,num):

    row_num = int(math.sqrt(num))
    col_num = int(math.sqrt(num))
    total_box = num
    
    # Using cur_box to keep track of box being filled
    # Assume we start at top right and work right then down
    cur_x = 1
    cur_y = 0

    i = 255
    j = 0
    
    box_width, box_height = get_box_size(im,row_num)
    

    for row in range(row_num):
        for col in range(col_num):
            box = [cur_x,cur_y, cur_x + box_width, cur_y + box_height]
            while box[2] >= im.width:
                box[2] -= 1
            print(box)
            print(im.width)
            cur_avg = average_pix(im,box)
            paint_box(im,cur_avg,box)
            # [i,j,0]
            # if i == 255:
            #     i = 0
            #     j = 255
            # else:
            #     i = 255
            #     j = 0
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


    
def get_box_size(im,box_num):
    box_width = im.width // box_num
    box_height = im.height // box_num
    return [box_width, box_height]


def paint_box(im, avg_color, box):
    # source = im.split()
    # r,g,b = 0,1,2
    # source[r].point(lambda i: avg_color)
    # im = Image.merge((im.mode,source))
    # im.show()

    start_x, start_y, width, height = box
    

    pix = im.load()
    for x in range(start_x,width):
        for y in range(start_y,height):
            pix[x,y] = (avg_color[0], avg_color[1],avg_color[2])
            # print('a')




# https://sighack.com/post/averaging-rgb-colors-the-right-way
def average_pix(im, box):

    # counters
    red = 0
    green = 0
    blue = 0

    # init setup
    pixels = im.load()
    # width = im.width
    # height = im.height

    start_x, start_y, width, height = box
    total_pix = width * height

    # gathering color totals
    for x in range(start_x,width):
        for y in range(start_y,height):
            # print(pixels[x,y])
            red += pixels[x,y][0]
            green += pixels[x,y][1]
            blue += pixels[x,y][2]
    
    # calculating average
    avg_squared = [red**2, green**2, blue**2]
    avg_rt =list(map(lambda x: int(math.sqrt(x)//total_pix), avg_squared))
    
    return(avg_rt)


    



if __name__ == '__main__':
    main()