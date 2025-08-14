def maximumToys(prices, k):
    prices.sort()
    total = 0
    count = 0
    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    k = int(input[1])
    prices = list(map(int, input[2:2+n]))
    print(maximumToys(prices, k))



"""     To solve this problem, we need to determine the maximum number of toys Mark can buy without exceeding his budget. The key insight here is that Mark should prioritize buying the cheapest toys first to maximize the number of toys he can purchase. This approach ensures that we use the budget as efficiently as possible.

Approach
Sort the Prices: First, we sort the list of toy prices in ascending order. This allows us to consider the cheapest toys first.

Iterate and Sum: We then iterate through the sorted list, continuously adding the price of each toy to a running total until adding the next toy would exceed the budget.

Count the Toys: For each toy that can be added without exceeding the budget, we increment a counter. The counter will hold the maximum number of toys Mark can buy. """