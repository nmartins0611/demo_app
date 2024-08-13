from flask import Flask, render_template
import random

app = Flask(__name__)

# Dummy data generator for latency
def get_latency_data():
    # Hostnames for Texas Data Center
    texas_hosts = [f"fin{str(i).zfill(2)}.gf.core.com" for i in range(1, 6)]
    # Hostnames for Illinois Data Center
    illinois_hosts = [f"fin{str(i).zfill(2)}.gf.core.com" for i in range(6, 11)]

    texas_data = [
        {"hostname": hostname, "latency": random.randint(20, 100)}
        for hostname in texas_hosts
    ]

    illinois_data = [
        {"hostname": hostname, "latency": random.randint(20, 100)}
        for hostname in illinois_hosts
    ]

    return texas_data, illinois_data

@app.route('/')
def index():
    texas_data, illinois_data = get_latency_data()
    return render_template('index.html', texas_data=texas_data, illinois_data=illinois_data)

if __name__ == '__main__':
    app.run(debug=True)
