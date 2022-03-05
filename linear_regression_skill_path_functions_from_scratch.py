
def euclidean_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += (pt1[i] - pt2[i]) ** 2
  return distance ** 0.5

def manhattan_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

def hamming_distance(pt1, pt2):
  distance = 0
  for num in range(len(pt1)):
    distance += 1 if pt1[num] != pt2[num] else 0
  return distance

print (hamming_distance([1,2],[1,100]), hamming_distance.__name__)
print (hamming_distance([5,4,9],[1,7,9]),)
print(euclidean_distance([1, 2], [4, 0]))
print(manhattan_distance([1, 2], [4, 0]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))
print(hamming_distance([1,2], [4,0]))

from scipy.spatial import distance

print(distance.euclidean([1,2],[4,0]))
print(distance.cityblock([1,2],[4,0]))
print(distance.hamming([5, 4, 9], [1, 7, 9]),hamming_distance([5, 4, 9], [1, 7, 9]))
print(distance.hamming([1,2],[4,0]),hamming_distance([1,2], [4,0]))

