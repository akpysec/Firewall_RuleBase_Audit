""" For later """

import plotly
import plotly.graph_objects as go

colors = {'A':'steelblue',
          'B':'firebrick'}

fig = go.Figure(
    data=[
        go.Bar(
        y=[2, 1, 3],
        marker_color=colors
    )
    ],
    layout_title_text="Findings"
)
fig.show()
