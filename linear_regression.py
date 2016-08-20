import numpy as np
import matplotlib.pyplot as plt


def linear_regr(data_set,featr,rate,iter_num):
    params=np.array([1.0]*(featr+1))
    params_temp=np.array([1.0]*(featr+1))
    data_set=np.insert(data_set,0,1.0,1)
    print(data_set)
    for k in range(0,iter_num):
        for i in range(0,featr+1):
            sum_diff=0
            for j in range(0,(data_set.shape)[0]):
                sum_diff2=0
                sum_diff2=np.sum(params*np.transpose((data_set[j][:featr+1])))
                sum_diff2=sum_diff2-data_set[j][featr+1]
                sum_diff2=sum_diff2*(data_set[j][i])
                sum_diff=sum_diff+sum_diff2
            something=params[i]-(rate*sum_diff)
            params_temp[i]=something
            
            
        params=params_temp
        
    x=[]
    y=[]
    for i in range(0,5):
        x.append(i)
        y.append(params[1]*x[i]+params[0])
    plt.plot(x,y)
    x1=[]
    y1=[]
    for i in range(0,data_set.shape[0]):
        x1.append(data_set[i][1])
        y1.append(data_set[i][2])
    plt.plot(x1,y1,'ro')
    plt.show()
    print(params)
    
    
    

a=np.array([[1.0,1.0],[2.0,10.0],[3.0,10.0],[4.0,10.0]])
linear_regr(a,1,0.01,200)

