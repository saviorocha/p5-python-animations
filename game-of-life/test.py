# import numpy as np
# a = int(input("Enter the number of rows:"))
# b = int(input("Enter the number of columns:"))
# print("Enter the number in a single line separated by space:")
# val = list(map(int, input().split()))
# matrix = np.array(val).reshape(a,b)
# print(matrix)
Var1 = 1
Var2 = 0
def function(): 
    global Var1, Var2
    if Var2 == 0 and Var1 > 0:
        print("Result One")
    elif Var2 == 1 and Var1 > 0:
        print("Result Two")
    elif Var1 < 1:
        print("Result Three")
    Var1 =- 1
function()