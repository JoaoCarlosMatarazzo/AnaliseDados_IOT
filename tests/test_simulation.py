import unittest
from src.iot_simulation import simulate_sensors

class TestSimulation(unittest.TestCase):
    def test_simulated_data_length(self):
        # Gera dados para 1 minuto com intervalo de 10 segundos
        data = simulate_sensors(duration_minutes=1, interval_seconds=10)
        # Verifica se o número de entradas está correto (1 minuto / 10 segundos = 6)
        self.assertEqual(len(data), 6)

    def test_simulated_data_format(self):
        # Gera dados para teste
        data = simulate_sensors(duration_minutes=1, interval_seconds=10)
        # Verifica se cada entrada possui as chaves esperadas
        for entry in data:
            self.assertIn("timestamp", entry)
            self.assertIn("temperature", entry)
            self.assertIn("vibration", entry)
            self.assertIn("speed", entry)

    def test_value_ranges(self):
        # Gera dados para teste
        data = simulate_sensors(duration_minutes=1, interval_seconds=10)
        # Verifica se os valores estão nos intervalos esperados
        for entry in data:
            self.assertTrue(20.0 <= entry["temperature"] <= 80.0)
            self.assertTrue(0.0 <= entry["vibration"] <= 10.0)
            self.assertTrue(50.0 <= entry["speed"] <= 200.0)

if __name__ == "__main__":
    unittest.main()
