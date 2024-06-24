import json
import pandas as pd
from datetime import date, timedelta
from configparser import ConfigParser


def get_date_range(dfs):
    min_dates = []
    for _, df in dfs.items():
        min_dates.append(date.fromisoformat(df.index.values.min()))
    min_date = min(min_dates)

    dates = []
    for i in range((date.today() - min_date).days + 1):
        dates.append((min_date + timedelta(days=i)).isoformat())

    return dates


def main():
    dimensions = {
        'cases': {'csv': 'ncumul_conf', 'xlsx': 'Cases'},
        'fatalities': {'csv': 'ncumul_deceased', 'xlsx': 'Fatalities'},
        'hospitalized': {'csv': 'ncumul_hosp', 'xlsx': 'Hospitalized'},
        'icu': {'csv': 'ncumul_ICU', 'xlsx': 'ICU'},
        'vent': {'csv': 'ncumul_vent', 'xlsx': 'Ventilated'},
        'released': {'csv': 'ncumul_released', 'xlsx': 'Released'}
    }
    parser = ConfigParser()
    parser.read("sources.ini")

    cantons = list(map(str.upper, parser["cantonal"]))

    dfs = {}
    last_updated = {}
    for canton in cantons:
        df = pd.read_csv(parser["cantonal"][canton.lower()])
        d = df.iloc[-1]["date"]
        t = df.iloc[-1]["time"]

        if type(t) == float or type(t) == pd.np.float64:
            t = "00:00"

        last_updated[canton] = {"Date": d, "Time": t}
        dfs[canton] = df.groupby(["date"]).max()

    df_last_updated = pd.DataFrame(last_updated).T
    df_last_updated.to_csv("last_updated.csv", index_label="Canton")

    # Append empty dates to all
    dates = get_date_range(dfs)
    df_by_dimension = {dimension: pd.DataFrame(float("nan"), index=dates, columns=cantons) for dimension in dimensions}

    for canton, df in dfs.items():
        for d in dates:
            if d in df.index:
                for dimension in dimensions:
                    df_by_dimension[dimension][canton][d] = df[dimensions[dimension]['csv']][d]

    # Fill to calculate the correct totals for CH
    df_total = {dimension: df.fillna(method="ffill") for dimension, df in df_by_dimension.items()}

    for dimension in dimensions:
        df_by_dimension[dimension]['CH'] = df_total[dimension].sum(axis=1)

    # Create a summery with the most important values in json to allow web devs to grab it
    summary = {
        "totals": {dimension: df["CH"][-1] for dimension, df in df_by_dimension.items()},
        "changes": {dimension: df["CH"][-1] - df["CH"][-2] for dimension, df in df_by_dimension.items()},
        "updated_cantons": ",".join(
            [
                canton
                for canton in df_by_dimension['cases']
                if canton != "CH" and not pd.np.isnan(float(df_by_dimension['cases'][canton][-1]))
            ]
        ),
    }

    with open("summary.json", "w") as f:
        json.dump(summary, f)

    # Store as CSV
    for dimension in dimensions:
        df_by_dimension[dimension].to_csv(f"covid19_{dimension}_switzerland_openzh.csv", index_label="Date")

    # Store as json
    for dimension, df in df_by_dimension.items():
        df.to_json(f"covid19_{dimension}_switzerland_openzh.json")

    with pd.ExcelWriter("covid_19_data_switzerland.xlsx") as writer:
        for dimension, df in df_by_dimension.items():
            df.to_excel(writer, index_label="Date", sheet_name=dimensions[dimension]['xlsx'])


if __name__ == "__main__":
    main()
