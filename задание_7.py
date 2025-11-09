N, K, M = map(int, input().split())
direct = abs(M - K) #модуль берём, тк считаем сначала расстояние по часовой
reverse = N - direct #а тут против часовой
min_path = min(direct, reverse)
print(min_path - 1)