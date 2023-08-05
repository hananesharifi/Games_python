n, q, l = map(int, input().split())

data_dict = {}
for _ in range(n):
    s, c = input().split()
    data_dict[s] = c

queries = []
for _ in range(q):
    query = input()
    if query in data_dict:
        queries.append(data_dict[query])
    else:
        queries.append("Unknown")

for query_result in queries:
    print(query_result)