def held_karp(cost):
    n = len(cost)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting from city 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if mask & (1 << v) == 0:
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            dp[mask][u] + cost[u][v]
                        )

    full_mask = (1 << n) - 1
    return min(dp[full_mask][u] + cost[u][0] for u in range(1, n))


##changign the x value in  dp[1][x] can give shortest path from any node/ city.  