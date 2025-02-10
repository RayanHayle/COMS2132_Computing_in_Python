def binary_search(arr, target):
    count = 0
    
    left, right = 0, len(arr) - 1 
    
    while left <= right:
        mid = (left + right) // 2
        
        #return mid, just set the mid no need to return it 
   
        
        if arr[mid] == target:
            count +=1
            print(f'The Count: {count}')
            return mid  
            
        elif arr[mid] < target:
            count +=1
            left = mid + 1 
        else:
            right = mid - 1 
            count +=1
            
    print(f'the Count: {count}')
    return -1
    

def is_sorted(arr):
    if arr ==  sorted:# used is instead of  == works here but is for memory location and == is to check equality 
        print('The List Sorted')
    else:
        print('The List Not sorted')


if __name__ == "__main__": 
    li = [1, 15, 27, 45, 89, 121]

    x = 89
    index = binary_search(li, x)
    

    if index == -1: 
        print(x, "not found")
    else: 
         print("found", x, "at index", index)    
    is_sorted(li)
