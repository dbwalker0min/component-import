
import glob
import pandas as pd

def main():
    all_dataframes = []
    for filename in glob.glob("chip_resistor__*.csv"):
        print(f"Processing {filename}")
        all_dataframes.append(pd.read_csv(filename))

    combined_df = pd.concat(all_dataframes, ignore_index=True)

    res_values = combined_df["Resistance"]
    for i, r in enumerate(res_values):
        if r.endswith(" kOhms"):
            r_text = r[:-6] + 'k'
            r = float(r[:-6]) * 1000
        elif r.endswith(" MOhms"):
            r_text = r[:-6] + 'M'
            r = float(r[:-6]) * 1000000
        elif r.endswith(" Ohms"):
            r_text = r[:-6]
            r = float(r[:-5])
        else:
            raise ValueError(f"Unknown resistance unit in {r}")
        combined_df.at[i, "RVal"] = r
        combined_df.at[i, "Resistance"] = r_text
    combined_df.to_excel("combined_chip_resistor_data.xlsx", index=False)


if __name__ == "__main__":
    main()
