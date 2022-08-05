# Pixlr

## TODO
1. Separate main.py into module
2. Begin Solution 2

## Solution One
**Concept:** To generate an image consisting of *n* pixels, we will divide the image into *n* squares and set each pixel within a given square to the average rgb value of all pixels in this square.


**Results:** Does not produce intended results. Even for squares that consist of a single color, it is inaccurate.
## Solution 2
**Concept:** Start at smallest pixel and take average of it alongside any adjacent pixels. 

## Solution 3
**Concept 3:** Looking into image downsampling

## Assorted notes
mipmapping
http://number-none.com/product/Mipmapping,%20Part%201/index.html



# Next time
investigate coordinates in iterate
Check with a single corner in paint box ie (0,0,100,100) to see if coordinates are being input in the correct order
Then verify using non-avgs as colors








