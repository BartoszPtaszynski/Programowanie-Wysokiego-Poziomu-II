from typing import List

def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

print(average([1.5, 2.5, 3.5]))  