def discrete_log_attack(G, H, Q):

    m = int(Q**0.5) + 1
    precomputed = {pow(G, j, Q): j for j in range(m)}

    G_inv_m = pow(pow(G, m, Q), -1, Q)

    for i in range(m):
        candidate = (H * pow(G_inv_m, i, Q)) % Q
        if candidate in precomputed:
            return i * m + precomputed[candidate]

G, H, Q = map(int, input().split())

X = discrete_log_attack(G, H, Q)

print(X)
