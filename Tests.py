import engine
from policy_providers import fortigate


print(
    fortigate.create_df(
        rule_base_as_nested_dict=fortigate.rule_base_parsing(
            raw_dataframe=fortigate.files_reader(
                path_to_files="C:\\Users\\andreyk\\PycharmProjects\\Tests",
                file_extension="txt",
                encoding_files="windows-1256")
        )
    )
)