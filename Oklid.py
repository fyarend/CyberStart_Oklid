
import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (2, 1)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Her nokta için en yakın noktayı bulan fonksiyon
def closestPoints(points):
    closest_points_list = []
    for idx1, point1 in enumerate(points):
        min_distance = float('inf')
        closest_point = None
        for idx2, point2 in enumerate(points):
            if idx1 != idx2:
                distance = euclideanDistance(point1, point2)
                if distance < min_distance:
                    min_distance = distance
                    closest_point = point2
        closest_points_list.append((point1, closest_point))
    return closest_points_list

# closestPoints fonksiyonunu çağırarak sonuçları yazdırma
closest_point_results = closestPoints(points)
for result in closest_point_results:
    print(f"Point {result[0]} is closest to {result[1]} with a distance of {euclideanDistance(result[0], result[1])}.")

