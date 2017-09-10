"""Lists defines simple list related operations"""

def get_first_item(li):
    """Return the first item from the list"""
    return li[0]

def get_last_item(li):
    """Return the last item from the list"""
    return li[-1]

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    secondItem = li[1]
    thirdItem = li[2]
    newList = [secondItem,thirdItem]
    return newList

def get_sum(li):
    """Return the sum of the list items"""


    sumOfList = 0
    for i in li :
        sumOfList = sumOfList + i
    return sumOfList

def get_avg(li):
    """Returns the average of the list items"""
    avg = get_sum(li)/len(li)
    return avg
