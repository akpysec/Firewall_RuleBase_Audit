import pandas as pd

FIELDS = [
    'from zone',
    'to zone',
    'source',
    'destination',
    'service',
    'application identity',
    'rule status',
    'action',
    'track',
    'securetrack rule uid',
    'service negated'
]

""" Generic Functions """


def df_to_low_case(dataframe: pd.DataFrame):
    return dataframe.applymap(lambda x: x.lower() if isinstance(x, str) else x)


def convert_to_single_convention(data_series: pd.Series, change_from: str, change_to: str):
    return data_series.apply(lambda x: x.replace(change_from, change_to) if isinstance(x, str) else x)


""" Checks Functions """


def disabled(dataframe: pd.DataFrame):
    if not dataframe.empty:
        disabled_rules = dataframe.loc[
            (dataframe[FIELDS[6]] == 'disabled')
        ]

        # Dropping empty columns
        disabled_rules.dropna(how='all', axis=1, inplace=True)

        return disabled_rules

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")


def track(dataframe: pd.DataFrame):
    if not dataframe.empty:
        track_log = dataframe.loc[
            (dataframe[FIELDS[6]] != 'disabled') &
            (dataframe[FIELDS[8]] != 'log')
            ]

        # Dropping empty columns
        track_log.dropna(how='all', axis=1, inplace=True)

        return track_log

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")


def any_src(dataframe: pd.DataFrame):
    rows_ids = list()
    if not isinstance(dataframe['source'], str):
        print(dataframe['source'])

    if not dataframe.empty:
        for row_id, status, action, source in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]], dataframe[FIELDS[2]]):
            if status != 'disabled' and action == 'allow':
                if isinstance(source, list):
                    if 'any' in source:
                        rows_ids.append(row_id)

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")

    # Selecting range of indexes of findings
    dataframe = dataframe.iloc[rows_ids, 0:]

    if not dataframe.empty:
        return dataframe


def any_dst(dataframe: pd.DataFrame):
    rows_ids = list()
    if not dataframe.empty:
        for row_id, status, action, destination in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]], dataframe[FIELDS[3]]):
            if status != 'disabled' and action == 'allow':
                if isinstance(destination, list):
                    if 'any' in destination:
                        rows_ids.append(row_id)

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")

    # Selecting range of indexes of findings
    dataframe = dataframe.iloc[rows_ids, 0:]

    if not dataframe.empty:
        return dataframe


def any_srv(dataframe: pd.DataFrame):
    rows_ids = list()
    if not dataframe.empty:
        for row_id, status, action, service in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]], dataframe[FIELDS[4]]):
            if status != 'disabled' and action == 'allow':
                if isinstance(service, list):
                    if 'any' in service:
                        rows_ids.append(row_id)

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")

    # Selecting range of indexes of findings
    dataframe = dataframe.iloc[rows_ids, 0:]

    if not dataframe.empty:
        return dataframe


def worst(dataframe: pd.DataFrame):
    rows_ids = list()
    if not dataframe.empty:
        for row_id, status, action, source, destination, service in zip(
                dataframe.index,
                dataframe[FIELDS[6]],
                dataframe[FIELDS[7]],
                dataframe[FIELDS[2]],
                dataframe[FIELDS[3]],
                dataframe[FIELDS[4]]
        ):
            if status != 'disabled' and action == 'allow':
                if isinstance(source, list) and isinstance(destination, list) and isinstance(service, list):
                    if 'any' in source and 'any' in destination and 'any' in service:
                        rows_ids.append(row_id)

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")

    # Selecting range of indexes of findings
    dataframe = dataframe.iloc[rows_ids, 0:]

    if not dataframe.empty:
        return dataframe


def crossed(dataframe: pd.DataFrame):
    return
