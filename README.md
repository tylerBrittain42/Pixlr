# Pixlr

## TODO
1. Separate main.py into module
2. Begin Solution 2

## Solution One
**Concept:** To generate an image consisting of *n* pixels, we will divide the image into *n* squares and set each pixel within a given square to the average rgb value of all pixels in this square.


**Results:** Does not produce intended results. Even for squares that consist of a single color, it is inaccurate.
## Solution 2 (Mipmapping)
**Concept:** Start at smallest pixel and take average of it alongside any adjacent pixels. 

**Results:** Much better than Solution 1. Image is accurately pixelated. However, coloring can appear odd after an extreme number of iterations

**Sources:** http://number-none.com/product/Mipmapping,%20Part%201/index.html




