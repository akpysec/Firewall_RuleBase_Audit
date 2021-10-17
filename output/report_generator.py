def write_report(path: str, list_of_names: list, list_of_contexts: list):
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
            for n, c in zip(list_of_names, list_of_contexts):
                button(_class="accordion").add(n)
                div(_class="panel").add(p(c))
            script(src='script.js')

        htmlsky.write(str(doc))
