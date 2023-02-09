n=5  #Enter the number of rows Which you want
for i in range(0,n):
    for j in range(i+1):
        print("*",end=" ")
    print( )
for i in range(n,0,-1):
    for j in range(i-1):
         print("*",end=" ")
    print( )
    
    
#output:
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
