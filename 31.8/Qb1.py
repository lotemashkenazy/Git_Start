# sizes (tuple)
def create_tuple():
    length = int(input("Enter length:"))
    higth = int(input("Enter higth:"))
    wide = int(input("Enter wide:"))
    size_tuple = (length, higth, wide)
    return size_tuple


# sizes = create_tuple()


# closets (list)
def create_closets():
    closets_list = []
    amount_closets = int(input("Enter the amount of closets:"))
    for i in range(amount_closets):
        closets_list.append(create_tuple())
    return closets_list


# boxes (list)
def create_boxes():
    boxes_list = []
    amount_boxes = int(input("Enter the amount of boxes:"))
    for i in range(amount_boxes):
        boxes_list.append(create_tuple())
    return boxes_list


def compare_size(closets, boxes):
    good_box = []
    # sizes_good_box = []
    for this_closet in closets:
        index_min_box = ""                 #the index of good box min
        counter = 0
        min = 100000                      #compare with the size of good box
        for this_box in boxes:
            if this_closet[0] <= this_box[0] and this_closet[1] <= this_box[1] and this_closet[2] <= this_box[2]:
                size = this_box[0] * this_box[1] * this_box[2]
                if size < min:                  #if the auze of good box is lower then min
                    min = size                  #min is the new size
                    index_min_box = counter        #counter is the index that go up every for
                 #   min_counter = counter
            counter += 1
        if counter == len(boxes) and index_min_box == "":     #if this is the last box, and no box is good
            good_box.append("-1")
        else:
            good_box.append(index_min_box)             #swich the good box with 0,0,0
            boxes[index_min_box] = (0, 0, 0)

    return good_box


boxes = create_boxes()
# print("boxes:", boxes)
closets = create_closets()
# print("closets:", closets)

print(compare_size(closets, boxes))
