"""This function is to merge two sorted list into single list"""
def sort_list(list1, list2):
    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    index1, index2 = 0, 0
    while index1 < len1 and index2 < len2:
        if list1[index1] < list2[index2]:
            new_list.append(list1[index1])
            index1 = index1 + 1
        elif list1[index1] > list2[index2]:
            new_list.append(list2[index2])
            index2 = index2 + 1
        else:
            new_list.append(list1[index1])
            index1 = index1 + 1
            index2 = index2 + 1
    while index1 < len1:
        new_list.append(list1[index1])
        index1 = index1 + 1
    while index2 < len2:
        new_list.append(list2[index2])
        index2 = index2 + 1
    return new_list
