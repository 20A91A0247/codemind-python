n = int(input())
lst = list(map(int, input().split()))
new_lst = [abs(i) for i in lst]
lengths = [len(str(i)) for i in new_lst]
m = max(lengths)
print(lengths.count(m))