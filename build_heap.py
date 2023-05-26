import os

def build_heap(data):
    heap_changes = []
    size = len(data)
    for i in range(size // 2, -1, -1):
        heapify(data, i, heap_changes)
    return heap_changes

def heapify(data, i, heap_changes):
    size = len(data)
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and data[left] < data[min_index]:
        min_index = left
    if right < size and data[right] < data[min_index]:
        min_index = right
    if min_index != i:
        heap_changes.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        heapify(data, min_index, heap_changes)
        
def main():
    user_input = input()
    if "I" in user_input:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in user_input:
        file_name = input()
        directory = './tests/'
        file_path = os.path.join(directory, file_name)
        with open(file_path, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    heap_changes = build_heap(data)
    print(len(heap_changes))
    for i, j in heap_changes:
        print(i, j)
        
if __name__ == "__main__":
    main()
