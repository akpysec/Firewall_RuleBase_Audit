from engine import check_engine
from policy_providers import fortigate, tufin, checkpoint

# import dominate
# from dominate.tags import *


# print(
#     check_engine.crossed_rules(
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


test = check_engine.crossed_rules(fortigate.create_df(
            rule_base_as_nested_dict=fortigate.rule_base_parsing(
                raw_dataframe=fortigate.files_reader(
                    path_to_files="C:\\Users\\andreyk\\PycharmProjects\\Tests",
                    file_extension="txt",
                    encoding_files="windows-1256"
                )
            )
        )
)

for row in test.itertuples():
    print(*row[0:])

    # print(
#     check_engine.crossed_rules(
#         dataframe=tufin.files_reader_and_parser(
#             path_to_files="C:\\Users\\andreyk\\PycharmProjects\\Tests\\tufin_reports\\test_csv_1",
#             # path_to_files="K:\\Skarim\\Harel\\Psagot\\FW",
#             file_extension="csv",
#             encoding_files="windows-1256"
#         )
#     )
# )

# print(
#     checkpoint.files_reader_and_parser(
#             path_to_files="K:\\Skarim\\Hapoalim\\PoalimSahar",
#             file_extension="csv",
#             encoding_files="windows-1256"
#         )
#     )

# def write_report(path: str, list_of_names: list, list_of_contexts: list):
#     with open(path, 'a') as htmlsky:
#         doc = dominate.document(title='Audit Report')
#         with doc.head:
#             meta(name="viewport", content="width=device-width, initial-scale=1")
#             style(
#                 """
#                 .accordion {
#                   background-color: #eee;
#                   color: #444;
#                   cursor: pointer;
#                   padding: 18px;
#                   width: 100%;
#                   border: none;
#                   text-align: left;
#                   outline: none;
#                   font-size: 15px;
#                   transition: 0.4s;
#                 }
#
#                 .active, .accordion:hover {
#                   background-color: #ccc;
#                 }
#
#                 .panel {
#                   padding: 0 18px;
#                   display: none;
#                   background-color: white;
#                   overflow: hidden;
#                 }
#                 """
#             )
#         with doc:
#             h2('Findings')
#             for n, c in zip(list_of_names, list_of_contexts):
#                 button(_class="accordion").add(n)
#                 div(_class="panel").add(p(c))
#             script(src='output/script.js')
#
#         htmlsky.write(str(doc))
#
#
# write_report(
#     path='AuditReport.html',
#     list_of_names=['row 1', 'row 2', 'row 3', 'row 4'],
#     list_of_contexts = ['context 1', 'context 2', 'context 3', 'context 4']
# )

