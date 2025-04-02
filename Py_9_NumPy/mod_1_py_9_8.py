import numpy as np

mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

print(mystery.shape)
elem_5_3=mystery[4,2]
print(elem_5_3)
last=mystery[-1,-1]
print(last)
line_4=mystery[3]
print(line_4)
col_2=mystery[:,-2]
print(col_2)
part=mystery[1:4,2:5]
print(part)
rev=(mystery[:,-1])[::-1]
print(rev)
trans=mystery.transpose()
print(trans)

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

nans_index=np.isnan(mystery)
print(nans_index)
# n_nan=0
# for i in nans_index:
#     if i: n_nan+=1
n_nan=sum(nans_index)
print(n_nan)
mystery_new=mystery.copy()
# mystery_new[np.isnan(mystery_new)]=0
mystery_new[nans_index]=0
print(mystery_new)

mystery_int=mystery.copy()
mystery_int=np.int32(mystery_int)

print(mystery_int.dtype)
array=np.sort(mystery)
print(array)
table=array.reshape((5,3),order='F')
print(table)
col=table[:,1]
print(col)
