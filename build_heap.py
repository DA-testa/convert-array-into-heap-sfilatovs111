#python3

def build_heap(arr):
    swaps = []
    n = len(arr)



    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        if left_child < n and arr[left_child] < arr[min_index]:
            min_index = left_child
        right_child = 2 * i + 2
        if right_child < n and arr[right_child] < arr[min_index]:
            min_index = right_child
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append((i, min_index))
            sift_down(min_index)
    for i in range(n // 2, -1, -1):
        sift_down(i)




    return swaps



def main():
    n = int(input())
    arr = list(map(int, input().split()))
    assert len(arr) == n
    swaps = build_heap(arr)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)




if __name__ == "__main__":
    main()
