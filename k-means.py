import numpy as np
import matplotlib.pyplot as plt


def dist(p1,p2):
    return ((p1[0]-p1[1])**2+((p1[0]-p2[0])**2))

def dist1(p1,list_c,k):
    a=[(dist(p1,list_c[j]),j) for j in range(k)]
    a=sorted(a,key=lambda s1:s1[0])
    #print(a,'and',a[0][1])
    return a[0][1]
    
    
def get_av(list_array_p):
    x1,y1=0,0
    for i in list_array_p:
        x1=x1+i[0]
        y1=y1+i[1]
    x1=x1/len(list_array_p)
    y1=y1/len(list_array_p)
    return (x1,y1)
        
def plot_points_norm(list_pts):
    color_set=['bo','ro','yo','co']
    for i in list_pts:
        plt.plot(i[0],i[1],'co')
    plt.show()

def plot_points(list_pts,k):
    color_set=['bo','ro','yo','co']
    for i in range(len(list_pts)):
        if (list_pts[i]!=[]):
            for j in list_pts[i]:
                plt.plot(j[0],j[1],color_set[i])
    plt.show()
                
def kmeans(data_set,k,iter1=3):
    
    start=np.random.rand(k,2)
    #print("this is start",start)
    #print(data_set.shape[0])
    plot_points_norm(data_set)
    for count in range(iter1):    
        list_belongs=[[] for c in range(k)]  
        for i in range(0,data_set.shape[0]):
            
            list_belongs[dist1(data_set[i],start,k)].append(data_set[i])
            #print(dist1(data_set[i],start,k))
           # print("this is data_set[i]",data_set[i],"intermediate list_belongs",list_belongs)
            
        for i in range(k):
            if(list_belongs[i]!=[]):
                start[i][0],start[i][1]=get_av(list_belongs[i])[0],get_av(list_belongs[i])[1]
        #print("intermediate",list_belongs)
    print(list_belongs)
    plot_points(list_belongs,k)
                
            
    
data_set=np.array([[1,1],[2,2],[3,3],[-1,-1],[-2,-2],[2,-2],[3,-3]])
kmeans(data_set,4,1000)