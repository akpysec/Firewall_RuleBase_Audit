import os
import pandas as pd
from engine import check_engine
from engine.check_engine import FIELDS


def files_reader_and_parser(path_to_files: str, file_extension: str, encoding_files: str):
    """ I - Checking input and looking for files with .csv extension """

    _path_to_files = []
    if len(path_to_files) >= 2:
        _path_to_files.append(path_to_files)

        # Iterate over .csv files in a path
        files = [x for x in os.listdir(path=_path_to_files[0]) if x.endswith(f"{file_extension}".lower())]

        dataframe_list = list()

        # Resolving "SettingWithCopyWarning"
        # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
        # SettingWithCopyWarning - Appeared when a .drop empty columns method was called before .to_excel method call
        pd.set_option('mode.chained_assignment', None)

        for f in files:
            # Reading files
            main_frame = pd.read_csv(_path_to_files[0] + "\\" + f, encoding=encoding_files.lower())

            # # Lowering case of all cells in the dataframe for unity
            main_frame = check_engine.df_to_low_case(main_frame)

            # Getting a row number of column set for rules
            for settings in main_frame.itertuples():
                if FIELDS[2] and FIELDS[3] and FIELDS[4] in settings:

                    # Changing main columns to the identified column for rules
                    main_frame.columns = main_frame.iloc[settings[0]]

                    # Selecting relevant rows from DataFrame (between rule base section)
                    main_frame = main_frame.iloc[settings[0] + 1: main_frame.last_valid_index() + 1]

                    for index, row in main_frame.iterrows():
                        # Appending to list for further creation of a DataFrame
                        dataframe_list.append(row.str.lower())

        # Creating a new DataFrame from a list
        df = pd.DataFrame(dataframe_list)

        # Removing duplicate Rules from a DataFrame
        df = df.drop_duplicates(subset=FIELDS[9], keep='first')

        # Splitting multiple values from df[series] - src, dst, srv for check convenience
        increment = 2

        # May cause an error if cell is not string - more attention needed later
        while increment <= 5:
            df[FIELDS[increment]].update(df[FIELDS[increment]].str.split('\n'))
            increment += 1

        # Action field
        df[FIELDS[7]] = check_engine.convert_to_single_convention(
            data_series=df[FIELDS[7]],
            change_from='accept',
            change_to='allow')

        # Adding numeric indexes
        df = df.reset_index()

        return df

