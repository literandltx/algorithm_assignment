from src.LinkedList import LinkedList

if __name__ == '__main__':
    input_data = [10, 20, 30, 40]
    linked_list = LinkedList()

    linked_list.insert_array(input_data)
    print("Original list: ", linked_list.to_list())

    linked_list.reverse()
    output_data = linked_list.to_list()
    print("Reversed list: ", output_data)
