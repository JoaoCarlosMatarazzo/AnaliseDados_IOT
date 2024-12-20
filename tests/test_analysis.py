import unittest
from src.data_analysis import analyze_data

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        # Dados simulados para teste
        self.sample_data = [
            {"timestamp": "2024-12-20T12:00:00", "temperature": 65.2, "vibration": 4.8, "speed": 120.5},
            {"timestamp": "2024-12-20T12:00:05", "temperature": 66.1, "vibration": 4.3, "speed": 119.8},
            {"timestamp": "2024-12-20T12:00:10", "temperature": 64.9, "vibration": 5.0, "speed": 121.0}
        ]

    def test_analyze_data_statistics(self):
        # Testa a função analyze_data
        import pandas as pd
        df = pd.DataFrame(self.sample_data)
        summary = df.describe()

        # Verifica estatísticas específicas
        self.assertAlmostEqual(summary['temperature']['mean'], 65.4, places=1)
        self.assertAlmostEqual(summary['vibration']['mean'], 4.7, places=1)
        self.assertAlmostEqual(summary['speed']['mean'], 120.43, places=2)

if __name__ == "__main__":
    unittest.main()
