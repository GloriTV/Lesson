import numpy as np


# print(np.iinfo(np.int16))
def get_chess(a):
    result=np.zeros((a,a))
    result[1::2,::2]=1
    result[::2,1::2]=1
    return result
    
def shuffle_seed(array):
    seed_np=round(np.random.uniform(0,4294967295))
    np.random.seed(seed_np)
    array_cop = np.random.permutation(array)
    return (array_cop,seed_np)

# array = [1, 2, 3, 4, 5]
# print(shuffle_seed(array))

def min_max_dist(*vectors):
    min_max=list()
    x_el=len(vectors)
    
    for x in range(x_el-1):
        for y in range(x+1,x_el):
            min_max.append(np.linalg.norm(vectors[x] - vectors[y]))
            
    return (min(min_max),max(min_max))

# vec1 = np.array([1,2,3])
# vec2 = np.array([4,5,6])
# vec3 = np.array([7, 8, 9])

# print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)

def any_normal(*vectors): 
    x_el=len(vectors)
    
    for x in range(x_el-1):
        for y in range(x+1,x_el):
            if np.dot(vectors[x] , vectors[y]) == 0 :return True
         
    return False

# vec1 = np.array([2, 1])
# vec2 = np.array([-1, 2])
# vec3 = np.array([3,4])
# print(any_normal(vec1, vec2, vec3))
# True

def get_loto(num):
    result=np.zeros((num,5,5))
    workers=range(1,101)
    for x in range(num):
        result[x]=np.random.choice(workers, size=(5,5), replace=False)
        
    return result

# print(get_loto(3))
simplelist = [19, 242, 14, 152, 142, 1000]
arr=np.array(simplelist)
print(arr.mean())