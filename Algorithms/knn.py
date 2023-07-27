import math
from collections import Counter

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def knn(training_data, test_instance, k):
    distances = []
    for i in range(len(training_data)):
        distance = euclidean_distance(training_data[i][:-1], test_instance)
        distances.append((distance, training_data[i][-1]))  # Appending distance and corresponding label
    distances.sort()  # Sorting distances in ascending order
    k_nearest_neighbors = distances[:k]  # Selecting k nearest neighbors
    labels = [neighbor[1] for neighbor in k_nearest_neighbors]  # Extracting labels
    # Counting the occurrence of each label in the k nearest neighbors
    label_counts = Counter(labels)
    # Returning the label with the highest occurrence
    return label_counts.most_common(1)[0][0]

# Example usage
training_data = [[1, 2, 'A'], [2, 3, 'A'], [4, 2, 'B'], [3, 5, 'B']]
test_instance = [2.5, 4]
k = 3

predicted_label = knn(training_data, test_instance, k)
print("Predicted label:", predicted_label)
