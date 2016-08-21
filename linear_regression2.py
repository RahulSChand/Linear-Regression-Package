import numpy as np
import matplotlib.pyplot as plt

def linear_regr(data_set,featr,rate,iter_num,line):
    params=np.array([1.0]*(featr+1))
    params=np.insert(params,featr+1,-1.0)
    params_temp=np.array([1.0]*(featr+1))
    params_temp=np.insert(params_temp,featr+1,-1.0)
    data_set=np.insert(data_set,0,1.0,1)
    print(data_set)
    print(params)
    for k in range(0,iter_num):
        for i in range(0,featr+1):
            first_array=data_set*np.transpose(params)
            second_array=np.transpose(first_array)*data_set[:,i]
            sum_diff=np.sum(second_array)
            params_temp[i]=params[i]-(rate*sum_diff)
        params=params_temp

    print(params[:(featr+1)])
    x,y=[],[]
    for i in range(0,line):
        x.append(i)
    for i in range(0,line):
        y.append(params[1]*x[i]+params[0])
    plt.plot(x,y)
    x1,y1=[],[]
    for i in range(0,data_set.shape[0]):
        x1.append(data_set[i][1])
        y1.append(data_set[i][2])
    plt.plot(x1,y1,'ro')
    plt.show()


a=np.array([[1.0,2.0],[2.0,5.0],[3.0,6.0],[5.0,10.0],[6.0,12.0],[7.0,20.0]])
linear_regr(a,1,0.01,300,9)

            
    
