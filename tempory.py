import math

lists = [69, 65, 90, 37, 92, 6, 28, 54]
print(lists)

'''insert_sort'''
# 将待排序元素与列表中在它序号后面的元素进行比较，并递增这一过程

#print(insert_sort(lists))
#print(insert_sort(lists))

    
'''shell_sort'''
# 将待排序列表中元素进行分组，然后比较

#print(shell_sort(lists))

#print(shell_sort_1(lists))

'''bubble_sort'''
#将待排序元素两两比较


#print(bubble_sort(lists))
                        
'''quick_sort'''
#通过一趟排序将列表元素分为两部分，其中一部分的数据比另外一部分的数据都要小\
#然后按照此方式再次排序


#print(quick_sort(lists))


'''select_sort'''
#第1趟：在待排序lists中比较lists[0]与lists[1:n]中的值，若lists[0]>lists[min],则交换，
#第2趟：在待排序lists中比较lists[1]与lists[2:n]中的值，若lists[1]>lists[min]，则交换，以此类推

#print(select_sort(lists))

'''heap_sort'''
#将待排序的序列构建成为一个完全二叉树，二叉树的每一个父节点均大于两个子节点，处于
#最上端的父节点是整个序列的最大值，第一趟将最上面的父节点提出放至list末尾，然后将
#整个树的最小子节点放至最大父节点，重新构建二叉树，依次类推。


'''merge_sort'''
#第一趟以长度为1分割排序，第二趟以3分割排序，直至最终以len(list)长度排序



class B(object):
    def fn(self):
        print('B fn')
    def __init__(self):
        print("B INIT")


class A(object):
    def fn(self):
        print('A fn')

    def __new__(cls,a):
        print("NEW", a)
        if a>10:
            return super(A, cls).__new__(cls)
        return B()

    def __init__(self,a):
        print("INIT", a)

a1 = A(5)
print(a1.fn)
a2 = A(20)
print(a2.fn)
    




