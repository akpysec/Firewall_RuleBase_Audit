import pandas as pd
import xlsxwriter
import colored
from colored import fg, attr, stylize
import openpyxl
from openpyxl.workbook import Workbook
from openpyxl.styles import PatternFill, Font
import datetime

""" Common field Variables """

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

""" Coloring Scheme """

BOLD_RED = colored.fg("red") + colored.attr("bold")
BOLD_GREEN = colored.fg("green") + colored.attr("bold")
BOLD_ORANGE = colored.fg("dark_orange_3a") + colored.attr("bold")

""" Generic Functions """


def df_to_low_case(dataframe: pd.DataFrame):
    return dataframe.applymap(lambda x: x.lower() if isinstance(x, str) else x)


def convert_to_single_convention(data_series: pd.Series, change_from: str, change_to: str):
    return data_series.apply(lambda x: x.replace(change_from, change_to) if isinstance(x, str) else x)


def paint_em(file_name, sheet_name, dataframe, column_name):

    wb = openpyxl.load_workbook(file_name)
    ws = wb[sheet_name]
    paint_red = Font(name='Segoe UI',
                     size=11,
                     bold=True,
                     italic=True,
                     vertAlign=None,
                     underline='none',
                     strike=False,
                     color='00FF0000')

    sheet_number = dataframe.columns.get_loc(column_name)

    for row in ws.iter_rows(min_row=2):
        row[sheet_number].font = paint_red
    wb.save(file_name)


def creating_excel_sheet(output_name: str, fw_type: str, policy_file_path: str, sheet_name="Flags"):

    writer = pd.ExcelWriter(output_name, engine='xlsxwriter')
    base_info = {
        'Date': [datetime.datetime.today()],
        'Firewall Type': [fw_type.upper()],
        'Policy Path': [policy_file_path]
    }
    base_frame = pd.DataFrame(base_info)
    base_frame.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.close()


""" Checks Functions """

# def disabled(dataframe: pd.DataFrame, file_name: str, sheet: str):
def disabled(dataframe: pd.DataFrame, file_name: str, sheet_name: str):

    if not dataframe.empty:
        dataframe = dataframe.loc[
            (dataframe[FIELDS[6]] == 'disabled')
        ]

        # Dropping empty columns ------------- FIND A WAY to DROP COLUMNS with 'nan' values
        # dataframe.dropna(how='all', axis=1, inplace=True)

        if not dataframe.empty:
            with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
                dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

            paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=FIELDS[6])

            print(stylize(f'{sheet_name} \tFINDING', BOLD_RED))

            return dataframe

        elif dataframe.empty:
            print(stylize(f'{sheet_name} \tPASS', BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")


def track_logs(dataframe: pd.DataFrame, file_name: str, sheet_name: str):

    if not dataframe.empty:
        dataframe = dataframe.loc[
            (dataframe[FIELDS[6]] != 'disabled') &
            (dataframe[FIELDS[8]] != 'log')
            ]

        # Dropping empty columns ------------- FIND A WAY to DROP COLUMNS with 'nan' values
        # dataframe.dropna(how='all', axis=1, inplace=True)

        if not dataframe.empty:
            with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
                dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

            paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=FIELDS[8])

            print(stylize(f'{sheet_name} \tFINDING', BOLD_RED))

            return dataframe

        elif dataframe.empty:
            print(stylize(f'{sheet_name} \tPASS', BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")


def any_src(dataframe: pd.DataFrame, file_name: str, sheet_name: str):

    rows_ids = list()
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
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=FIELDS[2])

        print(stylize(f'{sheet_name} \tFINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print(stylize(f'{any_src.__name__.upper().replace("_", " ")} \tPASS', BOLD_GREEN))
    else:
        print(stylize("Something else happened", BOLD_ORANGE))


def any_dst(dataframe: pd.DataFrame, file_name: str, sheet_name: str):

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
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=FIELDS[3])

        print(stylize(f'{sheet_name} \tFINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print(stylize(f'{sheet_name} \tPASS', BOLD_GREEN))
    else:
        print(stylize("Something else happened", BOLD_ORANGE))


def any_srv(dataframe: pd.DataFrame, file_name: str, sheet_name: str):

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
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=FIELDS[4])

        print(stylize(f'{sheet_name} \tFINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print(stylize(f'{sheet_name} \tPASS', BOLD_GREEN))
    else:
        print(stylize("Something else happened", BOLD_ORANGE))


def worst_rules(dataframe: pd.DataFrame, file_name: str, sheet_name: str):
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
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
            dataframe.to_excel(writer, sheet_name=worst_rules.__name__.upper().replace("_", " "), index=False)

        print(stylize(f'{worst_rules.__name__.upper().replace("_", " ")} \tFINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print(stylize(f'{worst_rules.__name__.upper().replace("_", " ")} \tPASS', BOLD_GREEN))
    else:
        print(stylize("Something else happened", BOLD_ORANGE))


def crossed_rules(dataframe: pd.DataFrame, file_name: str, sheet_name: str):

    # Maybe needs reverse - cross check: DO MORE TESTING
    if not dataframe.empty:
        rows_ids = list()
        if not dataframe.empty:
            for row_id, status, action in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]]):
                if status != 'disabled' and action == 'allow':
                    rows_ids.append(row_id)

        # Selecting range of indexes of enabled and allowed rules
        dataframe = dataframe.iloc[rows_ids, 0:]

        crossed = pd.DataFrame(columns=dataframe.columns)

        for i, fz, tz, a, b, c, d in zip(
                dataframe.index,
                dataframe.iloc[0:]['from zone'],
                dataframe.iloc[1:]['to zone'],
                dataframe.iloc[0:]['source'],
                dataframe.iloc[1:]['destination'],
                dataframe.iloc[0:]['service'],
                dataframe.iloc[1:]['service'],
        ):
            src_dst = list(set(a).intersection(set(b)))

            if src_dst and fz == tz:
                # Service comparing
                if c == d:
                    # print(i, a, i + 1, b, c, d)
                    # print(type(i))
                    crossed = crossed.append(dataframe.loc[[i, i + 1]])

        if not crossed.empty:
            with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
                crossed.to_excel(writer, sheet_name=crossed_rules.__name__.upper().replace("_", " "), index=False)

            print(stylize(f'{crossed_rules.__name__.upper().replace("_", " ")} \tFINDING', BOLD_RED))

            return crossed

        elif crossed.empty:
            print(stylize(f'{crossed_rules.__name__.upper().replace("_", " ")} \tPASS', BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))

