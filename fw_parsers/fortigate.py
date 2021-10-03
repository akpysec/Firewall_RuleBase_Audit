import os
import pandas as pd
from engine import check_engine
from engine.check_engine import FIELDS


def files_reader(path_to_files: str, file_extension: str, encoding_files: str):
    """ I - Checking input and looking for files with .csv extension """
    _path_to_files = []
    if len(path_to_files) >= 1:
        _path_to_files.append(path_to_files + "\\")

    files = [x for x in os.listdir(path=_path_to_files[0]) if x.endswith(f".{file_extension}".lower())]

    data_frame = pd.DataFrame([])

    for file in files:
        data_frame = data_frame.append(pd.read_csv(_path_to_files[0] + file, encoding=encoding_files.lower()))

    # Return - DataFrame with lowered case of all cells with function make_same

    return check_engine.df_to_low_case(dataframe=data_frame)


def rule_base_parsing(raw_dataframe: pd.DataFrame):
    """ Part II - Parsing FW Rule Base DataFrame to a Dictionary """
    rule_base_dictionary = {}
    enumerated_rules = list()
    # Depending points - if sometimes those will change script will not work, so update accordingly.
    edit = list()
    _next = list()

    for i, row in zip(raw_dataframe.index, raw_dataframe[raw_dataframe.columns[0]]):
        enumerated_rules.append([i, row])
        if row.__contains__('edit'):
            edit.append(i)
        # Depending point - next
        if row.__contains__('next'):
            _next.append(i)

    increment = 0

    # Formatting the values and creating a dictionary
    # Check it out another Walrus :=
    while (increment := increment + 1) <= -1 + len(edit):
        rule_base_dictionary[
            enumerated_rules[edit[increment] - 1:_next[increment]][1][1].lstrip().strip('\n')] = [
            enumerated_rules[edit[increment]:_next[increment]][1:]
        ]

    for k, v in rule_base_dictionary.items():
        tmp_list = list()
        for r in range(0, len(v[0])):
            tmp_list.append(v[0][r][1].lstrip().strip('\n'))

        # Splitting settings into string objects
        tmp_list = [x.split() for x in tmp_list]

        # Uniting setting name into one object and else into another and:
        # - Converting to dictionary
        # - Striping extra - '"'
        tmp_list = [dict({' '.join(y[0:2]): list(map(lambda x: x.strip('"'), (y[2:])))}) for y in
                    tmp_list]
        # Converting multiple dictionaries in the list into ONE dictionary
        tmp_list = {k: v for x in tmp_list for k, v in x.items()}

        # Appending to dictionary
        rule_base_dictionary.update({k: tmp_list})

    return rule_base_dictionary


def create_df(rule_base_as_nested_dict: dict):
    """ Part III - Creating a New DataFrame in right format for engine to process """

    # Create DataFrame
    df = pd.DataFrame(rule_base_as_nested_dict)

    # Use Keys as row indexes & nested Keys as Columns
    df = df.transpose()

    # Adding numeric indexes
    df = df.reset_index()

    # Renaming columns to fit engine checker
    df.rename(columns={
        'index': 'rule number',
        'set name': 'rule name',
        'set uuid': 'securetrack rule uid',
        'set srcintf': 'from zone',
        'set dstintf': 'to zone',
        'set srcaddr': 'source',
        'set dstaddr': 'destination',
        'set action': 'action',
        'set status': 'rule status',
        'set service': 'service',
        'set logtraffic': 'track',
        # 'set application-list': 'Application Identity',
        'set groups': 'source user',
        'set comments': 'comment'
    },
        inplace=True)

    # Un-packing values from lists to strings
    df = df.applymap(lambda x: ' '.join(x) if isinstance(x, list) else x)

    # Creating new lines in service column for each protocol
    df[FIELDS[4]] = df[FIELDS[4]].apply(lambda x: x.replace(' ', '\n') if isinstance(x, str) else x)

    # There are different conventions withing the settings values in FortiGate FW
    # so here I am changing to make them same for sake of "check_engine" script, much lesser "if" statements.
    # Rule Status
    df[FIELDS[6]] = check_engine.convert_to_single_convention(
        data_series=df[FIELDS[6]],
        change_from='disable',
        change_to='disabled')
    # Source field
    df[FIELDS[2]] = check_engine.convert_to_single_convention(
        data_series=df[FIELDS[2]],
        change_from='all',
        change_to='any')
    # Destination fields
    df[FIELDS[3]] = check_engine.convert_to_single_convention(
        data_series=df[FIELDS[3]],
        change_from='all',
        change_to='any')
    # Service field
    df[FIELDS[4]] = check_engine.convert_to_single_convention(
        data_series=df[FIELDS[4]],
        change_from='all',
        change_to='any')
    # Action field
    df[FIELDS[7]] = check_engine.convert_to_single_convention(
        data_series=df[FIELDS[7]],
        change_from='accept',
        change_to='allow')
    # Track field
    df[FIELDS[8]] = check_engine.convert_to_single_convention(
        data_series=df[FIELDS[8]],
        change_from='all',
        change_to='log')

    # Resolving "SettingWithCopyWarning"
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    # SettingWithCopyWarning - Appeared when a .drop empty columns method was called before .to_excel method call
    pd.set_option('mode.chained_assignment', None)

    # Splitting multiple values from df[series] for check convenience
    increment = 0
    while increment <= 4:
        df[FIELDS[increment]].update(df[FIELDS[increment]].str.split())
        increment += 1

    return df

