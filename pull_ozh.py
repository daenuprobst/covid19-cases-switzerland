import numpy as np
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
    parser = ConfigParser()
    parser.read("sources.ini")

    cantons = list(map(str.upper, parser["cantonal"]))

    dfs = {}
    last_updated = {}
    for canton in cantons:
        df = pd.read_csv(parser["cantonal"][canton.lower()])
        d = df.iloc[-1]["date"]
        t = df.iloc[-1]["time"]

        if type(t) == float or type(t) == np.float64:
            t = "00:00"

        last_updated[canton] = {"Date": d, "Time": t}
        dfs[canton] = df.groupby(["date"]).max()

    df_last_updated = pd.DataFrame(last_updated).T
    df_last_updated.to_csv("last_updated.csv", index_label="Canton")

    # Append empty dates to all
    dates = get_date_range(dfs)
    df_cases = pd.DataFrame(float("nan"), index=dates, columns=cantons)
    df_fatalities = pd.DataFrame(float("nan"), index=dates, columns=cantons)
    df_hospitalized = pd.DataFrame(float("nan"), index=dates, columns=cantons)
    df_icu = pd.DataFrame(float("nan"), index=dates, columns=cantons)
    df_vent = pd.DataFrame(float("nan"), index=dates, columns=cantons)
    df_released = pd.DataFrame(float("nan"), index=dates, columns=cantons)

    for canton, df in dfs.items():
        for d in dates:
            if d in df.index:
                df_cases[canton][d] = df["ncumul_conf"][d]
                df_fatalities[canton][d] = df["ncumul_deceased"][d]
                df_hospitalized[canton][d] = df["ncumul_hosp"][d]
                df_icu[canton][d] = df["ncumul_ICU"][d]
                df_vent[canton][d] = df["ncumul_vent"][d]
                df_released[canton][d] = df["ncumul_released"][d]

    # Fill to calculate the correct totals for CH
    df_cases_total = df_cases.fillna(method="ffill")
    df_fatalities_total = df_fatalities.fillna(method="ffill")
    df_hospitalized_total = df_hospitalized.fillna(method="ffill")
    df_icu_total = df_icu.fillna(method="ffill")
    df_vent_total = df_vent.fillna(method="ffill")
    df_released_total = df_released.fillna(method="ffill")

    df_cases["CH"] = df_cases_total.sum(axis=1)
    df_fatalities["CH"] = df_fatalities_total.sum(axis=1)
    df_hospitalized["CH"] = df_hospitalized_total.sum(axis=1)
    df_icu["CH"] = df_icu_total.sum(axis=1)
    df_vent["CH"] = df_vent_total.sum(axis=1)
    df_released["CH"] = df_released_total.sum(axis=1)

    df_cases.to_csv("covid19_cases_switzerland_openzh.csv", index_label="Date")
    df_fatalities.to_csv(
        "covid19_fatalities_switzerland_openzh.csv", index_label="Date"
    )
    df_hospitalized.to_csv(
        "covid19_hospitalized_switzerland_openzh.csv", index_label="Date"
    )
    df_icu.to_csv("covid19_icu_switzerland_openzh.csv", index_label="Date")
    df_vent.to_csv("covid19_vent_switzerland_openzh.csv", index_label="Date")
    df_released.to_csv("covid19_released_switzerland_openzh.csv", index_label="Date")

    with pd.ExcelWriter("covid_19_data_switzerland.xlsx") as writer:
        df_cases.to_excel(
            writer, index_label="Date", sheet_name="Cases",
        )
        df_fatalities.to_excel(
            writer, index_label="Date", sheet_name="Fatalities",
        )
        df_hospitalized.to_excel(
            writer, index_label="Date", sheet_name="Hospitalized",
        )
        df_icu.to_excel(
            writer, index_label="Date", sheet_name="ICU",
        )
        df_vent.to_excel(
            writer, index_label="Date", sheet_name="Ventilated",
        )
        df_released.to_excel(
            writer, index_label="Date", sheet_name="Released",
        )


if __name__ == "__main__":
    main()
