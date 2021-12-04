n = 5
x = 10
ans = 0 
stepen_n_v_k = 1
k_factorial = 1 
stepen_2_k = x + n

for k in range(1, n):
    stepen_n_v_k *= n 
    k_factorial *= k 
    stepen_2_k *= stepen_2_k
    ans = ((stepen_n_v_k+k_factorial)/stepen_2_k)
        
print(ans)