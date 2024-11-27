import os
import pandas

def load(path: str) -> pandas.DataFrame:
    try:
        if not os.path.exists(path) or not path.lower().endswith('.csv'):
            raise AssertionError(f"Invalid path or file type: {path}")
        load = pandas.read_csv(path)
        print(load)
        return load

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None