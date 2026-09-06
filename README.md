# 🛰️ AI-Based Satellite Disaster Detection & Damage Assessment

An AI-powered system that analyzes satellite imagery to detect disasters, identify affected regions, estimate damage severity, and visualize disaster-affected areas using computer vision, deep learning, and GIS technologies.

---

## 📌 Overview

Natural disasters such as floods, cyclones, wildfires, and earthquakes can cause extensive damage to infrastructure and human settlements. Rapid assessment of affected regions is essential for effective rescue operations and resource allocation.

This project proposes an AI-based satellite image analysis system that automatically identifies disaster-affected areas by analyzing satellite imagery.

The system is designed to compare satellite images captured before and after a disaster, detect significant changes, identify affected regions, estimate the severity of damage, and display the results through an interactive dashboard.

The initial prototype focuses on **flood detection and affected-area analysis**, with the architecture designed to support additional disaster types in the future.

---

## 🎯 Objectives

- Detect disaster-affected regions from satellite imagery.
- Identify changes between pre-disaster and post-disaster images.
- Segment affected areas using deep learning.
- Estimate the percentage of affected area.
- Classify disaster severity.
- Visualize affected regions using GIS-based maps.
- Provide an interactive web-based disaster analysis dashboard.
- Create a scalable architecture that can support multiple disaster types.

---

## 🧠 System Architecture

```text
              Satellite Images
             Before + After
                    │
                    ▼
          Image Preprocessing
                    │
                    ▼
            AI / Deep Learning
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   Disaster Detection    Change Detection
          │                   │
          └─────────┬─────────┘
                    ▼
             Image Segmentation
                    │
                    ▼
            Damage Assessment
                    │
                    ▼
            Severity Estimation
                    │
                    ▼
             GIS Visualization
                    │
                    ▼
             Web Dashboard
