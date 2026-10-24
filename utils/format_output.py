import pandas as pd


def format_table(p_list, label="P_n"):
    """
    Format iteration output as a table.
    """
    df = pd.DataFrame(p_list)
    df.index.name = "n"
    df = df.reset_index()
    df.rename(columns={0: label}, inplace=True)

    return df.to_string(index=False, formatters={label: "{:.13f}".format})