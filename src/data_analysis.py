import json
import pandas as pd
import matplotlib.pyplot as plt

def load_raw_data(filepath="data/raw/sensor_data.json"):
    #Carrega os dados
    with open(filepath, 'r') as file:
        return json.load(file)

def analyze_data(data):
    df = pd.DataFrame(data)
    print("Estatísticas Descritivas:")
    print(df.describe())
    plt.figure(figsize=(10, 6))
    plt.plot(pd.to_datetime(df['timestamp']), df['temperature'], label='Temperature')
    plt.plot(pd.to_datetime(df['timestamp']), df['vibration'], label='Vibration')
    plt.plot(pd.to_datetime(df['timestamp']), df['speed'], label='Speed')
    plt.xlabel('Time')
    plt.ylabel('Sensor Readings')
    plt.title('Sensor Data Over Time')
    plt.legend()
    plt.show()
    return df
if __name__ == "__main__":
    data = load_raw_data()
    analyze_data(data)
