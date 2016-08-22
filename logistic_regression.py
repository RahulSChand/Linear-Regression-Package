import numpy as np
import math
from sympy import plot_implicit,symbols,Eq
import matplotlib.pyplot as plt

def log_fun(val):
    if (math.fabs(val)>500):
        if val>0:
            return 1
        else:
            return 0
    return 1/(1+math.exp(-val))
def return_negative(val):
    return -val


def create_model2(data_set):
    col1,col2=data_set[:,1],data_set[:,2]
    y_input=data_set[:,3]
    data_set=np.delete(data_set,3,1)
    col3=col1*col2
    col3=np.transpose(np.array([col3]))
    col4=col1*col1
    col4=np.transpose(np.array([col4]))
    col5=col2*col2
    col5=np.transpose(np.array([col5]))
    np.append(data_set,col3,1)
    np.append(data_set,col4,1)
    np.append(data_set,col5,1)
    np.append(data_set,y_input,1)
    return data_set
def create_params_model1(model,featr):
    add=0
    if (model==1):
        add=3
    params=np.array([1.0]*(featr+1+add))
    params_temp=np.array([1.0]*(featr+1+add))
    return (params,params_temp)
def plot_points(data_set,params):
    x0,y0,x1,y1=[],[],[],[]
    for i in range(0,data_set.shape[0]):
        if (data_set[i][-1]==0.0):
            x0.append(data_set[i][1])
            y0.append(data_set[i][2])
        else:
            x1.append(data_set[i][1])
            y1.append(data_set[i][2])
    plt.plot(x0,y0,'ro')
    plt.plot(x1,y1,'bs')
    
    x,y=symbols('x y')
    p1=plot_implicit(Eq(params[0]+params[1]*x+params[2]*y,0))
    plt.show()
   
    
             


def logistic_regr(data_set,featr,rate,iter_num,model=0):
    add=0
    data_set=np.insert(data_set,0,1.0,1)
    if (model==1):
        data_set=create_model2(data_set)
        add=3
    params,params_temp=create_params_model1(model,featr)
    for k in range(0,iter_num):
        for i in range(0,featr+1+add):
            data_set_y=np.delete(data_set,3,1)
            first_array=np.dot(data_set_y,np.transpose(params))
            #print(first_array)
            vector_log=np.vectorize(log_fun,otypes=[np.float])
            first_array=vector_log(first_array)
            #print(first_array)
            vector_neg=np.vectorize(return_negative,otypes=[np.float])
            y_input_neg=np.array([vector_neg(data_set[:,featr+add+1])])
            
            first_array=np.append(np.transpose(np.array([first_array])),np.transpose(y_input_neg),1)
            first_array=np.sum(first_array,1)
            first_array=np.dot(first_array,np.transpose(data_set[:,i]))
            sum_diff=np.sum(first_array)
            params_temp[i]=params[i]-(rate*sum_diff)
        params=params_temp
    print(params[:featr+add+1])
    plot_points(data_set,params)
    
    
            
#Test Case            
data_set=np.array([[1.0,3.0,0.0],[1.0,6.0,0.0],[1.5,4.0,0.0],[2.5,5,0.0],[3.0,1.0,1.0],[4.0,2.0,1.0],[5.0,3.0,1.0],[6.0,1.0,1.0]])
logistic_regr(data_set,2,1,300,0)          
            
            
            
            
        
    
        
    
        

    