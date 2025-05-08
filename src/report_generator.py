import json
from datetime import datetime

def generate_report(timeline_df):
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_events": int(len(timeline_df)),
        "events": timeline_df.to_dict(orient="records")
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    import pandas as pd
    from log_parser import parse_logs
    from correlation_engine import correlate_events
    logs = parse_logs("data/synthetic_logs.csv")
    timeline = correlate_events(logs)
    report = generate_report(timeline)
    print(report)
