import matplotlib.pyplot as plt
class Pic():
    '''make pic'''
    def __init__(self):
        '''初始化'''

    def pic_hist(self,list,num):
        z = []
        for one in list:
            z.append(float(one))
        plt.hist(z,num)
        plt.show()
        plt.savefig('show_result/hist.png')
        plt.close()


