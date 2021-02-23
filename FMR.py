#problem statement
#program which accepts n number from user , & filter out only even number
#then increament all event number by 2
#then after increamenting perform summation of that modified numbers

#example,
#Input[1,3,2,4,6,5,4]

#after filter[2,4,6,4]
#after map[4,6,8,6]
#after reduce 24

import functools #module in python3
        
def main():
    arr=[] #list
    print("Enter the number of elements")
    size= int(input())
    
    for i in range(size):
        print("Enter element number:",i+1)
        no= int(input())
        arr.append(no)
        
    print("Your entered data is:",arr)
    print(functools.reduce(lambda a,b : a+b, list(map(lambda no : no + 2, list(filter(lambda no : (no %2 == 0),arr))))))


if __name__=="__main__":
    main()
