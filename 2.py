import heapq

def merge_k_lists(lists):

    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, 0))  # (значення, індекс списку, індекс елемента в списку)

    result = []
    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        result.append(val)
        if element_index + 1 < len(lists[list_index]):
            heapq.heappush(heap, (lists[list_index][element_index + 1], list_index, element_index + 1))

    return result

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)