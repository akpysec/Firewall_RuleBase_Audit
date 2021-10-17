import dominate
from dominate.tags import *
import os

def write_report(path: str, accordion_name: str, accordion_context: str):
    with open(path, 'a') as htmlsky:
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
            button(_class="accordion").add(accordion_name)
            div(_class="panel").add(p(accordion_context))
            script(src='script.js')
        doc = str(doc).replace('&quot', '"').replace('";', '"')
        # os.system(f'copy .\script.js {path.strip("fortigate-Audit-Report.html")} ') #fortigate-Audit-Report.html
        htmlsky.write(doc)
