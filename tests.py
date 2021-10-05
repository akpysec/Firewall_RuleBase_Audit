from engine import check_engine
from policy_providers import fortigate, tufin


# print(
#     check_engine.any_src(
#         fortigate.create_df(
#             rule_base_as_nested_dict=fortigate.rule_base_parsing(
#                 raw_dataframe=fortigate.files_reader(
#                     path_to_files="C:\\Users\\andreyk\\PycharmProjects\\Tests",
#                     file_extension="txt",
#                     encoding_files="windows-1256"
#                 )
#             )
#         )
#     )
# )
#
print(
    check_engine.worst(
        dataframe=tufin.files_reader_and_parser(
            path_to_files="C:\\Users\\andreyk\\PycharmProjects\\Tests\\tufin_reports\\test_csv_1",
            # path_to_files="K:\\Skarim\\Harel\\Psagot\\FW",
            file_extension="csv",
            encoding_files="windows-1256"
        )
    )
)

