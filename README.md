# Multi-Sensor Dashboard — ROS 2

A ROS 2 project demonstrating custom messages, multiple publisher nodes, ROS 2 topics, and a multi-sensor aggregator.

This project was built as **Week 3 — Project 1** of my ROS 2 learning roadmap.

---

## 📌 Project Overview

The project simulates three independent robot sensors:

- 📏 Ultrasonic distance sensor
- 🧭 IMU orientation sensor
- 🔋 Battery level sensor

Each sensor runs as a **separate ROS 2 publisher node** and publishes data using a custom ROS 2 message type.

A central **dashboard aggregator node** subscribes to all three sensor topics and combines their latest values into a single dashboard output.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │ Ultrasonic Publisher │
                    └──────────┬───────────┘
                               │
                               ▼
                         /ultrasonic
                               │
                               │
                               ▼
                        ┌───────────────────┐
                        │                   │
                        │ Dashboard         │
                        │ Aggregator        │
                        │                   │
                        └───────────────────┘
                               ▲
                               │
                            /imu
                               │
                    ┌──────────┴───────────┐
                    │                      │
              IMU Publisher          Battery Publisher
                    │                      │
                    └─────── /battery ────┘                                       │
