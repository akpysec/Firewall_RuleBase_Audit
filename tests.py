from engine import check_engine
from policy_providers import fortigate, tufin, checkpoint

import dominate
from dominate.tags import *


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

def write_report():
    with open('AuditReport.html', 'w') as htmlsky:
        doc = dominate.document(title='Audit Report')

        with doc.head:
            meta(name="viewport", content="width=device-width, initial-scale=1")
            style(
                """
                .accordion {
                  background-color: #eee;
                  color: #444;
                  cursor: pointer;
                  padding: 18px;
                  width: 100%;
                  border: none;
                  text-align: left;
                  outline: none;
                  font-size: 15px;
                  transition: 0.4s;
                }
                
                .active, .accordion:hover {
                  background-color: #ccc;
                }
                
                .panel {
                  padding: 0 18px;
                  display: none;
                  background-color: white;
                  overflow: hidden;
                }
                """
            )
        with doc:
            h2('Findings')
            button(_class="accordion").add("First")
            div(_class="panel").add(p("Some text"))
            script(src='script.js')

        htmlsky.write(str(doc))
