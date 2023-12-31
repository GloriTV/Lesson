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
    max_np=0
    min_np=10
    x_el=len(vectors)
    
    for x in range(x_el-1):
        for y in range(x+1,x_el):
            var=np.linalg.norm(vectors[x] - vectors[y])
            if var<min_np: min_np=var
            if var>max_np: max_np=var
    return (min_np,max_np)

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

print(min_max_dist(vec1, vec2, vec3))
# (5.196152422706632, 10.392304845413264)
