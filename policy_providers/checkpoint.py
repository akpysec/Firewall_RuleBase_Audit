""" In Progress """

import pandas as pd
import os
from engine import check_engine
from engine.check_engine import FIELDS


def files_reader_and_parser(path_to_files: str, file_extension: str, encoding_files: str):

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
            df = check_engine.df_to_low_case(main_frame)

            # df[FIELDS[6]] = check_engine.convert_to_single_convention(
            #     data_series=df[FIELDS[6]],
            #     change_from='disable',
            #     change_to='disabled')
            # Action field
            # df[FIELDS[7]] = check_engine.convert_to_single_convention(
            #     data_series=df[FIELDS[7]],
            #     change_from='accept',
            #     change_to='allow')


            return df
