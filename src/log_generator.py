import pandas as pd
import random
import datetime

def generate_logs(num_records=100):
    sources = ['endpoint', 'network', 'cloud']
    events = ['login-failure', 'anomaly', 'alert', 'file-access', 'configuration-change']
    messages = [
        "user admin failed to login",
        "suspicious inbound traffic detected",
        "possible credential compromise",
        "unauthorized file access detected",
        "system configuration changed unexpectedly"
    ]
    logs = []
    for _ in range(num_records):
        log = {
            "timestamp": datetime.datetime.now().isoformat(),
            "source": random.choice(sources),
            "event": random.choice(events),
            "message": random.choice(messages)
        }
        logs.append(log)
    return pd.DataFrame(logs)

if __name__ == '__main__':
    df = generate_logs(50)
    print(df.head())
