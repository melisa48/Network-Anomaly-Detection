import numpy as np
import matplotlib.pyplot as plt

# Function to simulate packet data collection
def collect_packet_data():
    # Simulate packet sizes (this would be replaced with actual data collection logic)
    np.random.seed(0)
    packet_sizes = np.random.normal(loc=500, scale=150, size=1000)
    # Introduce some anomalies
    anomalies = np.random.normal(loc=1500, scale=100, size=10)
    packet_sizes = np.concatenate([packet_sizes, anomalies])
    return packet_sizes

# Function to preprocess packet data
def preprocess_packets(packet_data):
    # For this example, we are using packet sizes directly
    return np.array(packet_data)

# Function to detect anomalies
def detect_anomalies(packet_sizes):
    mean = np.mean(packet_sizes)
    std_dev = np.std(packet_sizes)
    threshold = mean + 3 * std_dev
    anomalies = packet_sizes[packet_sizes > threshold]
    return threshold, anomalies

# Function to visualize anomalies
def plot_anomalies(packet_sizes, anomalies, threshold):
    plt.figure(figsize=(10, 6))
    plt.hist(packet_sizes, bins=50, alpha=0.7, label='Packet Sizes')
    plt.axvline(x=threshold, color='r', linestyle='--', label='Anomaly Threshold')
    plt.scatter(anomalies, [0]*len(anomalies), color='r', label='Anomalies')
    plt.xlabel('Packet Size')
    plt.ylabel('Frequency')
    plt.title('Packet Size Distribution with Anomalies')
    plt.legend()
    plt.show()

# Main function to monitor network traffic and detect anomalies
def monitor_network_traffic():
    # Collect and preprocess packet data
    packet_data = collect_packet_data()
    packet_sizes = preprocess_packets(packet_data)
    
    # Perform anomaly detection
    threshold, anomalies = detect_anomalies(packet_sizes)
    
    if len(anomalies) > 0:
        print("Anomalies detected!")
        print("Anomaly Threshold:", threshold)
        print("Detected Anomalies:", anomalies)
        
        # Visualize anomalies
        plot_anomalies(packet_sizes, anomalies, threshold)

# Start monitoring once
monitor_network_traffic()
