import os
import random
import json
from datetime import datetime, timedelta

def simulate_sensors(duration_minutes=10, interval_seconds=5):
    # Simula sensores IoT coletando dados em uma linha de produção.
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    current_time = start_time
    data = []
    while current_time < end_time:
        sensor_readings = {
            "timestamp": current_time.isoformat(),
            "temperature": round(random.uniform(20.0, 80.0), 2),
            "vibration": round(random.uniform(0.0, 10.0), 2),
            "speed": round(random.uniform(50.0, 200.0), 2)
        }
        data.append(sensor_readings)
        current_time += timedelta(seconds=interval_seconds)
    return data

def save_raw_data(data, filepath="data/raw/sensor_data.json"):
    # Cria o diretório, se necessário
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Salva os dados em um arquivo JSON
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    data = simulate_sensors()
    save_raw_data(data)
    print("Dados simulados salvos em 'data/raw/sensor_data.json'")
