import pandas as pd

def test_groupby_aggregation():
    df = pd.DataFrame({
        "customer_id": [1, 1, 2],
        "amount": [100, 200, 300]
    })
    agg = df.groupby("customer_id").agg({
        "amount": "sum"
    })
    assert agg.loc[1, "amount"] == 300
