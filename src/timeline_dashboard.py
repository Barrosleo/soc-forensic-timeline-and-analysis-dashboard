import dash
from dash import dcc, html
import dash_table
import plotly.express as px

def create_dashboard(timeline_df):
    app = dash.Dash(__name__)
    
    # Create a simple line chart of events over time
    fig = px.line(timeline_df, x="timestamp", y="source", markers=True,
                  title="Incident Timeline")
    
    app.layout = html.Div(children=[
        html.H1("SOC Forensic Timeline Dashboard"),
        html.Div("Timeline of correlated security events:"),
        dash_table.DataTable(
            id='timeline-table',
            columns=[{"name": i, "id": i} for i in timeline_df.columns],
            data=timeline_df.to_dict('records'),
            page_size=10,
        ),
        dcc.Graph(figure=fig)
    ])
    
    return app

if __name__ == '__main__':
    from log_parser import parse_logs
    from correlation_engine import correlate_events
    logs = parse_logs("data/synthetic_logs.csv")
    timeline = correlate_events(logs)
    app = create_dashboard(timeline)
    app.run_server(debug=True)
