# Network Anomaly Detection
This project involves a Python script for detecting network anomalies based on packet sizes. The script simulates network traffic data, processes it, and identifies anomalies using statistical methods. It also visualizes the results with a histogram.

## Features
- Simulates Packet Data: Generates random packet sizes and introduces anomalies.
Preprocesses Data: Processes the collected packet data.
- Detects Anomalies: Identifies anomalies based on a threshold calculated using mean and standard deviation.
- Visualizes Results: Displays a histogram of packet sizes and highlights anomalies.
## Prerequisites
Ensure you have Python installed along with the following libraries:
- numpy
- pandas
- scikit-learn
- matplotlip
- scapy
`pip install numpy pandas scikit-learn matplotlib scapy`

## Script Details
network_anomaly_detector.py
1. `collect_packet_data()`: Simulates packet size data including anomalies.
2. `preprocess_packets()`: Processes the packet data (currently just converts it to a NumPy array).
3. `detect_anomalies()`: Calculates the anomaly threshold and detects anomalies based on packet sizes.
4. `plot_anomalies()`: Visualizes packet size distribution and detects anomalies.
5. `monitor_network_traffic()`: Continuously collects data, detects anomalies, and plots results.

## Usage
To run the script, execute the following command in your terminal:
`python network_anomaly_detector.py`
The script will continuously monitor the simulated network traffic, detect anomalies, and plot the results.

## Notes
- The script uses simulated data. Replace the collect_packet_data() function with actual network traffic data collection logic for real-world usage.
- Adjust the time.sleep() duration in the monitor_network_traffic() function to control how frequently the script checks for anomalies.
## Contributing:
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.
