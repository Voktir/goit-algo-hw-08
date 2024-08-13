import heapq

def min_cost_merge(cables):
    heapq.heapify(cables)
    cost = 0
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        cost += cable1 + cable2
        heapq.heappush(cables, cable1 + cable2)
    return cost

# Приклад використання:
cables = [1,2,3,5,8,13,21,30]
print("Мінімальні витрати:", min_cost_merge(cables))