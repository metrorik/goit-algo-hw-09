def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [{} for _ in range(amount + 1)]
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                coin_count[i][coin] = coin_count[i].get(coin, 0) + 1
    
    return coin_count[amount]

# Приклад використання:
amount = 113
print(find_min_coins(amount))
