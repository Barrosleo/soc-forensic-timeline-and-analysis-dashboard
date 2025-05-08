def correlate_events(logs_df):
    # sort logs by timestamp to simulate timeline correlation
    timeline = logs_df.sort_values(by="timestamp").reset_index(drop=True)
    return timeline

if __name__ == '__main__':
    import pandas as pd
    from log_parser import parse_logs
    logs = parse_logs("data/synthetic_logs.csv")
    timeline = correlate_events(logs)
    print(timeline)
