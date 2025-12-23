import unittest
from rk2 import DataManager

class TestComputerClassroomSystem(unittest.TestCase):
    
    def setUp(self):
        self.manager = DataManager()
    
    def test_task1_computers_starting_with_A(self):
        result = self.manager.task1_computers_starting_with_A()
        
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
        for model, ram, classroom_name in result:
            self.assertTrue(model.startswith('A'))
        
        expected_models = ['Acer Aspire', 'Acer Predator', 'Apple iMac', 'Asus ProArt']
        actual_models = [item[0] for item in result]
        
        for expected_model in expected_models:
            self.assertIn(expected_model, actual_models)
        
        sorted_models = sorted(actual_models)
        self.assertEqual(actual_models, sorted_models)
    
    def test_task2_classrooms_min_ram(self):
        result = self.manager.task2_classrooms_min_ram()
        
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
        for classroom_name, min_ram in result:
            self.assertIsInstance(classroom_name, str)
            self.assertIsInstance(min_ram, int)
            self.assertGreater(min_ram, 0)
        
        ram_values = [item[1] for item in result]
        sorted_ram_values = sorted(ram_values)
        self.assertEqual(ram_values, sorted_ram_values)
        
        expected_results = [
            ("Графическая лаборатория", 8),
            ("Программирование", 8),
            ("Основной компьютерный класс", 16),
            ("Мультимедийный центр", 32)
        ]
        
        for classroom_name, expected_min_ram in expected_results:
            found = False
            for actual_classroom, actual_min_ram in result:
                if actual_classroom == classroom_name:
                    self.assertEqual(actual_min_ram, expected_min_ram)
                    found = True
                    break
            self.assertTrue(found)
    
    def test_task3_all_relationships_sorted(self):
        result = self.manager.task3_all_relationships_sorted()
        
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        
        for model, ram, classroom_name in result:
            self.assertIsInstance(model, str)
            self.assertIsInstance(ram, int)
            self.assertIsInstance(classroom_name, str)
            self.assertGreater(ram, 0)
        
        models = [item[0] for item in result]
        sorted_models = sorted(models)
        self.assertEqual(models, sorted_models)
        
        expected_relationships = [
            ("Acer Aspire", 8, "Программирование"),
            ("Acer Predator", 16, "Графическая лаборатория"),
            ("Dell Optiplex", 16, "Основной компьютерный класс"),
        ]
        
        for expected_model, expected_ram, expected_classroom in expected_relationships:
            found = False
            for actual_model, actual_ram, actual_classroom in result:
                if (actual_model == expected_model and 
                    actual_ram == expected_ram and 
                    actual_classroom == expected_classroom):
                    found = True
                    break
            self.assertTrue(found)

if __name__ == '__main__':
    unittest.main(verbosity=2)