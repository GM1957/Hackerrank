if __name__ == '__main__':
    n = int(input())
    arr1 = []
    arr2 = []
    arr3= []
    arr4 = []
    def brother(arr1):
        arr2.append(arr1)

        for i in range(n):
        name = input()
        score = float(input())
        arr1.append(name)
        arr1.append(score)
        brother(arr1)
        arr1 =[] 
    
    for j in range(n-1):
        arr3.append(arr2[j][1])

    arr3.sort()
    p = arr3[1]

    for k in range(n-1):
        if (arr2[k][1] == p):
            arr4.append(arr2[k][0])

    arr4.sort() 
    for t in range(2):
        print(arr4[t])       
