
#!/usr/bin/env python3
# os_ticket_adapter.py

# This is used to get alerting data from opensearch and create a ticket on osticket via a POST request.

from flask import Flask, request, jsonify
import requests
import json
import os
import logging
from datetime import datetime


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


# turn these into environment variables or config file later
OSTICKET_URL = 'http://localhost:8081/api/tickets.json'
OSTICKET_API_KEY = 'ABF0E4E417C8D32BB445C66E835402D7'
DEFAULT_SUBMITTER_EMAIL = "alerts@opensearch.com"
DEFAULT_SUBMITTER_NAME = "Automated Alert System"
DEFAULT_TOPIC_ID = "1"
DEFAULT_PRIORITY = "2"  # Medium priority

def receive_data():
    data = request.get_json(force=True)
    logging.info(f"Received data: {data}")
    return data

@app.route('/osticket', methods=['POST'])
def create_ticket():
    payload = receive_data()
    print(payload)

    ticket = {
        "name": DEFAULT_SUBMITTER_NAME,
        "email": DEFAULT_SUBMITTER_EMAIL,
        "message": payload.get('message', 'No message provided'),
        "subject": payload.get('title', 'SOC alert'),
        "host": payload.get('host', 'unknown'),
        "timestamp": payload.get('timestamp', "date unkown"),
        "priority": payload.get("priority", DEFAULT_PRIORITY),
        "severity": payload.get("severity", "2"),
        "source_ip": payload.get("source_ip", "ip unknown"),
        "topic_id": DEFAULT_TOPIC_ID
    }

    headers = {
        'X-API-Key': OSTICKET_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.post(OSTICKET_URL, json=ticket, headers=headers)

    print("Response from osTicket:", response.status_code, response.text)

    logging.info("Received webhook: %s", payload.keys())
    return jsonify({"status": "ticket_sent", "osticket_status": response.status_code})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
