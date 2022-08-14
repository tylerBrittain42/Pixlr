from method_two import Pixlr


def main():
    print(f"Pixlr Demo")
    file_name = input("File name:")
    layer_choice = int(input("Layers:"))
    
    method_two_demo = Pixlr(f"./sample/{file_name}.jpeg")
    method_two_demo.multi_iteration(layer_choice)
    method_two_demo.show()

if __name__ == '__main__':
    main()