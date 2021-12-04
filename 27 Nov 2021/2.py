DNA = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
ans = []
for i in range(len(DNA)-15):
    if all([DNA[x] == DNA[x+10] for x in range(i, i+5)]):
        ans.append(DNA[i:i+10])
print(ans)