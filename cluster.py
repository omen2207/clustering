import csv

def read_points_from_csv(csv_file):
    points = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            points.append([float(row[0]), float(row[1]), float(row[2])]) 
    return points

def compute_cluster_center(points):
    num_points = len(points)
    if num_points == 0:
        return (0, 0, 0)
    center_x = sum(point[0] for point in points) / num_points
    center_y = sum(point[1] for point in points) / num_points
    center_z = sum(point[2] for point in points) / num_points
    return (center_x, center_y, center_z)
def squared_euclidean_distance(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2
csv_file = r'C:\Users\bhilw\OneDrive\Documents\DM\cluster_data.csv' 
points = read_points_from_csv(csv_file)
cluster_center = compute_cluster_center(points)
print(f"Cluster Center: {cluster_center}")
distances = []
num_points = len(points)
for i in range(num_points):
    row = []
    for j in range(num_points):
        if j >= i: 
            distance = squared_euclidean_distance(points[i], points[j]) ** 0.5  
            row.append(distance)
        else:
            row.append(None) 
    distances.append(row)
print("\nUpper Triangular Distance Matrix:")
for i in range(num_points):
    for j in range(num_points):
        if j >= i:
            print(f"{distances[i][j]:6.2f}", end=" ")
        else:
            print("      ", end=" ")
    print()
