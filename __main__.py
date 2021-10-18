# Local Project Imports
from policy_providers import fortigate, tufin
from engine.check_engine import any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
from engine.cli_flags import args
from engine.bar_chart import stats_chart

# Packages Import
import colored
from colored import fg, attr, stylize
import dominate
from dominate.tags import *


BOLD_RED = colored.fg("red") + colored.attr("bold")
BOLD_GREEN = colored.fg("green") + colored.attr("bold")
BOLD_ORANGE = colored.fg("dark_orange_3a") + colored.attr("bold")

checks = [
    any_srv, any_dst, any_src, disabled, track_logs, worst_rules, crossed_rules
]


with open('Audit report.html', 'a') as htmlsky:
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
        for check in checks:
            findings = list() # Put here what found and then write to excel each
            if args.policy_provider == 'fortigate':
                forti = check(
                    dataframe=fortigate.create_df(
                        rule_base_as_nested_dict=fortigate.rule_base_parsing(
                            raw_dataframe=fortigate.files_reader(
                                path_to_files=args.path,
                                file_extension=args.file_extension,
                                encoding_files=args.encoding
                            )
                        )
                    )
                )
                if forti is not None:
                    """
                    for r in forti.index:
                        print(forti.iloc[r], forti.columns[0:])"""

                    button(_class="accordion").add(check.__name__.upper().replace('_', ' '))
                    div(_class="panel").add(p(forti))

                    print(stylize(f'{check.__name__.upper()} \tFINDING', BOLD_RED))
                elif forti is None:
                    print(stylize(f"{check.__name__.upper()} \tPASS", BOLD_GREEN))
                else:
                    print(stylize("Something else happened", BOLD_ORANGE))

            elif args.policy_provider == 'tufin':
                tufi = check(
                    dataframe=tufin.files_reader_and_parser(
                        path_to_files=args.path,
                        file_extension=args.file_extension,
                        encoding_files=args.encoding
                    )
                )
                if tufi is not None:
                    button(_class="accordion").add(check.__name__.upper().replace('_', ' '))
                    div(_class="panel").add(p(tufi.to_string()))

                    print(stylize(f'{check.__name__.upper()} \tFINDING', BOLD_RED))
                elif tufi is None:
                    print(stylize(f"{check.__name__.upper()} \tPASS", BOLD_GREEN))
                else:
                    print(stylize("Something else happened", BOLD_ORANGE))

        script("""
        var acc = document.getElementsByClassName("accordion");
        var i;
        
        for (i = 0; i < acc.length; i++) {
          acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
              panel.style.display = "none";
            } else {
              panel.style.display = "block";
            }
          });
        }
        """)
    doc = str(doc).replace('&quot;', '"').replace('&lt;', '<')
    htmlsky.write(doc)



# # For later
# if args.bar_chart:
#     stats_chart(finding_type="str", times_found=int)

