class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = False
        second = False
        third = False

        for triplet in triplets:
            if (triplet[0] == target[0]
                    and triplet[1] <= target[1]
                    and triplet[2] <= target[2]):
                first = True
            if (triplet[1] == target[1]
                    and triplet[0] <= target[0]
                    and triplet[2] <= target[2]):
                second = True
            if (triplet[2] == target[2]
                    and triplet[1] <= target[1]
                    and triplet[0] <= target[0]):
                third = True
        
        return first and second and third