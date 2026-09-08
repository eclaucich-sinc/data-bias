import math

def erf(x):
    return math.erf(x)

def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# target AUC
target_auc_y = 0.90
target_auc_s = 0.85

def find_sigma(target_auc):
    best_sigma = 0
    min_diff = 1.0
    for i in range(1, 30000):
        sigma = i / 10000.0
        # z = 1 / (sigma * sqrt(2))
        z = 1.0 / (sigma * math.sqrt(2))
        auc = phi(z)
        diff = abs(auc - target_auc)
        if diff < min_diff:
            min_diff = diff
            best_sigma = sigma
    return best_sigma

print(f"Sigma for Global Feature Predictivity (target AUC 0.90): {find_sigma(target_auc_y):.4f}")
print(f"Sigma for Proxies (target AUC 0.85): {find_sigma(target_auc_s):.4f}")
