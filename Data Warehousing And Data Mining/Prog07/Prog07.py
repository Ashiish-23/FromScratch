import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
import time

def run_algo(df, algo, name):
    """Runs given algorithm and prints frequent itemsets, rules, and time."""
    start = time.time()
    items = algo(df, min_support=0.1, use_colnames=True)
    rules = association_rules(items, metric="confidence", min_threshold=0.6)
    print(f"\n{name} Itemsets:\n", items)
    print(f"\n{name} Rules:\n", rules[['antecedents', 'consequents', 'lift']])
    print(f"{name} Time: {time.time() - start:.4f} sec")
    return items, rules

data = pd.DataFrame({
    "Milk": [1, 0, 1, 1, 0],
    "Bread": [1, 1, 0, 1, 1],
    "Butter": [0, 1, 1, 1, 0]
}, dtype=bool)

run_algo(data, apriori, "Apriori")
run_algo(data, fpgrowth, "FP-Growth")
