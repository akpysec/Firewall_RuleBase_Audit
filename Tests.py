import engine
from policy_providers import fortigate
# engine.check_engine.any_srce()

print(
    create_df(
        rule_base_as_nested_dict=rule_base_parsing(
            raw_dataframe=files_reader(
                path_to_files="C:\\Users\\andreyk\\PycharmProjects\\Tests",
                file_extension="txt",
                encoding_files="windows-1256")
        )
    )
)