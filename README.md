#  Opensearch SIEM home lab | Cybersecurity portfolio project
![OpenSearch](https://img.shields.io/badge/OpenSearch-005EB8?style=for-the-badge&logo=opensearch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Filebeat](https://img.shields.io/badge/Filebeat-005571?style=for-the-badge)
![Logstash](https://img.shields.io/badge/Logstash-005571?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![osTicket](https://img.shields.io/badge/osTicket-FF8800?style=for-the-badge)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

#### Author: Patrick Sunden
#### Status: 🟧 In progress

# Overview
This project implements a fully functional monitoring and response lab environment that demonstates how a SOC environment detects and analyzes threats. This home lab combines log collection, centralized analysis and log aggregation, alerting, ticketing and eventually attack simulation. 

Logs from the Windows and Linux endpoints are shipped to Logstash using Winlogbeat and Filebeat, where they are parsed, enriched and sent to Opensearch, where they are stored and visualised. Detection rules in Opensearch identify suspicious activity from the logs, if suspicious activity is detected by an alert trigger, an alert is created in opensearch, user is alerted in slack (webhook from opensearch), and a ticket creation request is sent to osTicket by using a custom webhook and forwarder API.

The idea for this project is not only to present it, but also create easy to implement instructions for the environment when the project is finished.

# Architecture
![Architecture](img/Architecture.png "High level architecture of the SIEM home lab")



# Detailed workflow of the lab

A Beats agent (linux=filebeat, windows=winlogbeat) is installed on all hosts we want to monitor. These agents all send their data to Logstash, which is running on the monitoring host Ubuntu machine. This monitoring Ubuntu hosts Docker, with Opensearch, Logstash and osTicket as containers. Logstash then enriches and sorts the data, sending them to correct indexes in Opensearch-node1, these can then be visualized in opensearch-dashboards.
![Dashboards](img/dashboard.png "Opensearch Dashboard")

We can set up a monitor in opensearch to monitor the logs that are coming in to Opensearch. We can also specify triggers and actions for these monitors. A query looks for certain things in the logs, for example the example below looks for unsuccessful ssh login attempts from the last 5 minutes (full query not in image):
![Monitor Query](img/monitor_query.png "Opensearch Dashboard")
![Trigger and Action](img/trigger_and_action.png "Opensearch Dashboard")

The trigger then looks if there are more than 5 login attempts based on the results of the query. If this returns true, an alert is generated and the actions that have been specified will be fired. In this case the alert actions are sending an alert to Slack, and taking data from the query and sending a ticket creation request to osTicket via a custom API:
![Slack](img/slack_alert.png "Opensearch Dashboard")
![Forwarder](img/forwarder.png "Opensearch Dashboard")

This alert is then assigned automatically, and looks like this in osTicket:
![osTicket](img/osTicket.png "Opensearch Dashboard")

# Setting up the environment

# To-Do
* Add more hosts to monitor and add diversity to the monitored hosts
* Add more complicated detection rules and alerts
* Create more realistic attack simulations with Mythic C2
* Possibly replacing Opensearch with Splunk
* Integrate Wazuh

# Learning outcomes

* Security monitoring and log analysis using opensearch
* Detection engineering with monitors and Mustache templates
* Networking
* Designing the architecture of a SIEM environment
* Shell scripting
* Docker
