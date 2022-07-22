from audioop import avg
from operator import le
from tracemalloc import start
from turtle import width
from PIL import Image
import math

# box = x,y,height,length


def main():
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
    paint_box(checker,avg_color,[0,0,50,checker.width])
    checker.show()


def paint_box(im, avg_color, box):
    # source = im.split()
    # r,g,b = 0,1,2
    # source[r].point(lambda i: avg_color)
    # im = Image.merge((im.mode,source))
    # im.show()

    start_x, start_y, height, width = box
    

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

    start_x, start_y, height, width = box
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