# soc forensic timeline and analysis dashboard

this project simulates a soc incident investigation by aggregating synthetic log data from multiple sources, correlating events into a forensic timeline, visualizing the incident's progression through an interactive dashboard, and generating detailed incident reports that outline the investigation and remediation actions.

## key features
- data aggregation & normalization from synthetic logs
- event correlation to reconstruct incident timelines
- interactive dashboard for timeline visualization
- automated incident reporting

## usage
1. use github codespaces or the online web editor to modify the project.
2. install dependencies from `requirements.txt`.
3. run the project with:
python src/main.py

## repository structure
soc-forensic-timeline-and-analysis-dashboard/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_report.json
├── data/
│   └── synthetic_logs.csv
└── src/
    ├── main.py
    ├── log_generator.py
    ├── log_parser.py
    ├── correlation_engine.py
    ├── timeline_dashboard.py
    └── report_generator.py

