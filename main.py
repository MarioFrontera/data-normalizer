from data_loader import load_data
from dataset import DataSet
from normalizer import normalize

values = load_data("data.txt")
normalized_values = normalize(values)
data = DataSet(normalized_values)

print("Normalized:", normalized_values)
print("Mean:", data.mean())
print("Minimum:", data.minimum())
print("Maximum:", data.maximum())
