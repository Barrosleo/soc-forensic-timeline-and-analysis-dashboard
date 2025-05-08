from log_generator import generate_logs
from log_parser import parse_logs
from correlation_engine import correlate_events
from timeline_dashboard import create_dashboard
from report_generator import generate_report
import os

def main():
    # ensure required directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    
    # generate synthetic logs and save to CSV
    logs_df = generate_logs(200)
    logs_df.to_csv("data/synthetic_logs.csv", index=False)
    print("Synthetic logs generated.")

    # parse logs from CSV
    logs = parse_logs("data/synthetic_logs.csv")
    print("Parsed logs:", len(logs), "records.")

    # correlate events to build a forensic timeline
    timeline = correlate_events(logs)
    print("Correlation complete. Event timeline has", len(timeline), "entries.")

    # generate and save an incident report
    report = generate_report(timeline)
    with open("docs/incident_report.json", "w") as f:
        f.write(report)
    print("Incident report generated at docs/incident_report.json")

    # launch the timeline dashboard for interactive visualization
    app = create_dashboard(timeline)
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
