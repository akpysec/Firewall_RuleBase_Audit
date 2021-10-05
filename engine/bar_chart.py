""" For later """

import plotly
import plotly.graph_objects as go

def stats_chart(finding_type: str, times_found: int):
    colors = {'A':'steelblue',
              'B':'firebrick'}

    fig = go.Figure(
        data=[
            go.Bar(
            y=[2, 1, 3])
        ],
        layout_title_text="Findings"
    )
    return fig.show()
