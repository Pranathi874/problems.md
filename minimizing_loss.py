def minimize_loss(prices):
    n = len(prices)
    min_loss = float('inf')
    buy_year = -1
    sell_year = -1

    for i in range(n):  
        for j in range(i + 1, n):  
            if prices[j] < prices[i]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1  
                    sell_year = j + 1

    if buy_year == -1:
        print("No loss possible.")
    else:
        print(f"Buy in year {buy_year}, sell in year {sell_year}, loss = {min_loss}")
n = int(input("Enter number of years: "))
print("Enter the prices separated by space:")
prices = list(map(int, input().split()))


if len(prices) != n:
    print("Error: Number of prices does not match number of years.")
else:
    minimize_loss(prices)