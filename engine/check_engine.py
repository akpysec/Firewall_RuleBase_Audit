import pandas as pd
import colored
from colored import stylize
import openpyxl
from openpyxl.styles import Font
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
BOLD_YELLOW = colored.fg("yellow_3b") + colored.attr("bold")

colorize = ["black",  # 0
            "blue",  # 1
            "brown",  # 2
            "cyan",  # 3
            "gray",  # 4
            "green",  # 5
            "lime",  # 6
            "magenta",  # 7
            "navy",  # 8
            "orange",  # 9
            "pink",  # 10
            "purple",  # 11
            "red",  # 12
            "silver",  # 13
            "white",  # 14
            "yellow"  # 15
            ]

""" Generic Functions """


def printing_to_console(msg: str):
    print(stylize("-" * 26, BOLD_YELLOW))
    print(stylize(msg, BOLD_YELLOW))
    print(stylize("-" * 26, BOLD_YELLOW))


def df_to_low_case(dataframe: pd.DataFrame):
    return dataframe.applymap(lambda x: x.lower() if isinstance(x, str) else x)


def convert_to_single_convention(data_series: pd.Series, change_from: str, change_to: str):
    return data_series.apply(lambda x: x.replace(change_from, change_to) if isinstance(x, str) else x)


def paint_em(file_name: str, sheet_name: str, dataframe: pd.DataFrame, column_name: list, color='00FF0000'):
    wb = openpyxl.load_workbook(file_name)
    ws = wb[sheet_name]
    paint_red = Font(name='Segoe UI',
                     size=11,
                     bold=True,
                     italic=True,
                     vertAlign=None,
                     underline='none',
                     strike=False,
                     color=color)
    for col in column_name:
        sheet_number = dataframe.columns.get_loc(col)

        for row in ws.iter_rows(min_row=2):
            row[sheet_number].font = paint_red

    wb.save(file_name)


def creating_excel_sheet(file_name: str, fw_type: str, policy_file_path: str, sheet_name="Flags"):
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    base_info = {
        'Date': [datetime.datetime.today()],
        'Firewall Type': [fw_type.upper()],
        'Policy Path': [policy_file_path]
    }
    base_frame = pd.DataFrame(base_info)
    base_frame.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.close()


""" Checks Functions """


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

            paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=[FIELDS[6]])

            print('- ' + sheet_name, stylize('\t | FINDING', BOLD_RED))

            return dataframe

        elif dataframe.empty:
            print('- ' + sheet_name, stylize('\t | PASS', BOLD_GREEN))
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

            paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=[FIELDS[8]])

            print('- ' + sheet_name, stylize('\t | FINDING', BOLD_RED))

            return dataframe

        elif dataframe.empty:
            print('- ' + sheet_name, stylize('\t | PASS', BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))

    elif dataframe.empty:
        print("DataFrame is Empty")
    else:
        print("Something else happened")


def any_src(dataframe: pd.DataFrame, file_name: str, sheet_name: str):
    rows_ids = list()
    if not dataframe.empty:
        for row_id, status, action, source in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]],
                                                  dataframe[FIELDS[2]]):
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

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=[FIELDS[2]])

        print('- ' + sheet_name, stylize('\t | FINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print('- ' + sheet_name, stylize('\t | PASS', BOLD_GREEN))
    else:
        print(stylize("Something else happened", BOLD_ORANGE))


def any_dst(dataframe: pd.DataFrame, file_name: str, sheet_name: str):
    rows_ids = list()
    if not dataframe.empty:
        for row_id, status, action, destination in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]],
                                                       dataframe[FIELDS[3]]):
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

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=[FIELDS[3]])

        print('- ' + sheet_name, stylize('\t | FINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print('- ' + sheet_name, stylize('\t | PASS', BOLD_GREEN))
    else:
        print(stylize("Something else happened", BOLD_ORANGE))


def any_srv(dataframe: pd.DataFrame, file_name: str, sheet_name: str):
    rows_ids = list()
    if not dataframe.empty:
        for row_id, status, action, service in zip(dataframe.index, dataframe[FIELDS[6]], dataframe[FIELDS[7]],
                                                   dataframe[FIELDS[4]]):
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

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=[FIELDS[4]])

        print('- ' + sheet_name, stylize('\t | FINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print('- ' + sheet_name, stylize('\t | PASS', BOLD_GREEN))
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
            dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

        paint_em(file_name=file_name, sheet_name=sheet_name, dataframe=dataframe, column_name=[
            FIELDS[2],
            FIELDS[3],
            FIELDS[4]])

        print('- ' + sheet_name, stylize('\t | FINDING', BOLD_RED))

        return dataframe

    elif dataframe.empty:
        print('- ' + sheet_name, stylize('\t | PASS', BOLD_GREEN))
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

        source = list(dataframe[FIELDS[2]])
        destination = list(dataframe[FIELDS[3]])
        service = list(dataframe[FIELDS[4]])
        suid = list(dataframe[FIELDS[9]])

        uid_set = set()

        # Looping
        for r in range(0, len(source)):
            for src, dst in zip(source, destination):
                for s, d in zip(src, dst):
                    if s in destination[r] and d in source[r]:
                        for s_srv, d_srv in zip(service[source.index(src)], service[destination.index(dst)]):
                            if s_srv in service[destination.index(destination[r])]:
                                # print(f"service match\nSource:{s_srv}\nDestination:{service[destination.index(destination[r])]}")
                                uid_set.add(suid[source.index(src)])
                                uid_set.add(suid[destination.index(destination[r])])
                                uid_set.add(suid[destination.index(dst)])
                                uid_set.add(suid[source.index(source[r])])

        dataframe = dataframe.loc[dataframe[FIELDS[9]].isin(uid_set)]
        # print(dataframe[FIELDS[9]])
        # print(dataframe.sort_values(FIELDS[4]))

        if not dataframe.empty:
            with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
                dataframe.to_excel(writer, sheet_name=sheet_name, index=False)

            paint_em(file_name=file_name,
                     sheet_name=sheet_name,
                     dataframe=dataframe,
                     column_name=[FIELDS[2]],
                     color='00FF00FF')
            paint_em(file_name=file_name,
                     sheet_name=sheet_name,
                     dataframe=dataframe,
                     column_name=[FIELDS[3]],
                     color='0000FF00')
            paint_em(file_name=file_name,
                     sheet_name=sheet_name,
                     dataframe=dataframe,
                     column_name=[FIELDS[4]])

            print('- ' + sheet_name, stylize(' | FINDING', BOLD_RED))

            return dataframe

        elif dataframe.empty:
            print('- ' + sheet_name, stylize(' | PASS', BOLD_GREEN))
        else:
            print(stylize("Something else happened", BOLD_ORANGE))
