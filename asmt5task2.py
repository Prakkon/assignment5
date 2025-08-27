
def task2():

    ol = [1,2,3,4,5,6,7,8,9,10]
    print("Orignial list: {}".format(ol))
    nl = ol[:5]
    print("Extracted first five elements: {}".format(nl))
    nl.reverse()
    print("Reversed extracted elements: {}".format(nl))

    return

task2()