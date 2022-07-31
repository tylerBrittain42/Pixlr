from method_one import Pixlr



def main():
    
    method_one_demo = Pixlr('./sample/checker.jpeg',11)
    method_one_demo.paint_boxes()
    method_one_demo.show()
   

    
    



if __name__ == '__main__':
    main()