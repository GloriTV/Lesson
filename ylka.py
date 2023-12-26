from random import randint as r

star='*'
toy='o'

# height = int (input('\nEnter the number of height [2-20]: '))
height = 20
width=2*height-1

for i in range(1,width+1,2):
    tree = i * star
    tree_1 =tree.center(width,'_')
    if i ==7 or i==9 or i==19 or i==21 or i==31: i-=1
    elif i ==11 or i==23 or i==33 or i==35: i+=1
    
    if (i-3)%3==0:
        start = (width-i)//2
        end= start+i
        my_list=list(tree_1)
        my_list[r(start,end)]=toy
        tree_1=''.join(my_list)
    
        
    print(tree_1)