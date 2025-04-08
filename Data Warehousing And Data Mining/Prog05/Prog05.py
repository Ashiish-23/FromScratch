import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def generate_rules(data, min_sup=0.3, metric='lift', threshold=1.0):
    te = TransactionEncoder()
    df = pd.DataFrame(te.fit(data).transform(data), columns=te.columns_)
    itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    rules = association_rules(itemsets, metric=metric, min_threshold=threshold)
    return itemsets, rules

dataset = [
    ['milk', 'bread', 'nuts', 'apple'],
    ['milk', 'bread', 'nuts'],
    ['milk', 'bread'],
    ['milk', 'apple'],
    ['bread', 'nuts', 'apple'],
    ['milk', 'bread', 'apple'],
    ['bread', 'nuts'],
]

freq_items, assoc_rules = generate_rules(dataset)
print("Frequent Itemsets:\n", freq_items)
print("\nAssociation Rules:\n", assoc_rules)
