from src.iot_simulation import simulate_sensors, save_raw_data
from src.data_analysis import load_raw_data, analyze_data
from src.optimization_algorithm import optimize_production

def main():
    data = simulate_sensors()
    save_raw_data(data)
    raw_data = load_raw_data()
    processed_data = analyze_data(raw_data)
    optimize_production(processed_data)

if __name__ == "__main__":
    main()
