import pandas as pd

from pipeline.utils import generate_hash
def test_generate_hash():
    row = pd.Series({
        "id": 1,
        "amount": 500
    })

    result = generate_hash(row)
    assert result is not None
    assert isinstance(result, str)
