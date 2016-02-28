import math
import egg_skeleton


class EggDrop(egg_skeleton.EggDropSkeleton):
    """
    Egg drop.
    Suppose that you have an N-story building and plenty of eggs.
    An egg breaks if it is dropped from floor T or higher and does not break otherwise.
    Your goal is to devise a strategy to determine the value of T given the following
    limitations on the number of eggs and tosses:
        Version 0: 1 egg, <= T tosses.
        Version 1: logN eggs and logN tosses. [ROUND UP]
        Version 2: logT eggs and 2logT tosses. [ROUND UP]
        (Advanced)Version 3: 2 eggs and 2*N^(1/2) tosses.
        (Advanced)Version 4: 2 eggs and <= c*T^(1/2) tosses for some fixed constant c.
    """

    def version0(self):
        floor = 0
        egg_broken = False
        while not egg_broken:
            floor += 1
            egg_broken = self.toss(floor)
        return floor

    def version1(self):
        upper = self.N
        lower = 1
        found = False
        floor = -1
        while not found:
            if upper - lower == 0:
                found = True
                floor = lower
                break
            t = (upper + lower) / 2
            egg_broken = self.toss(t)
            if egg_broken:
                upper = t
            else:
                lower = t + 1
        return floor

    def version2(self): # This one is in corner cases!
        upper = self.N
        lower = 1
        story = 1
        while story <= self.N:
            if not self.toss(story):
                lower = story
                story *= 2
            else:
                upper = story
                break
        lower += 1

        found = False
        floor = -1
        while not found:
            if upper - lower <= 0:
                found = True
                floor = upper
                break
            t = (upper + lower) / 2
            egg_broken = self.toss(t)
            if egg_broken:
                upper = t
            else:
                lower = t + 1
        return floor

    def version3(self):
        S = int(math.sqrt(self.N)) + 1
        floor = 1 - S
        while floor + S <= self.N:
            if self.toss(floor + S):
                if floor + S == 1: return 1
                break
            floor += S

        for i in range(floor + 1, min(floor + S, self.N)):
            if self.toss(i):
                return i
        return min(floor + S, self.N)

    def version4(self):
        egg_broken = False
        i = 1
        while i * i <= self.N:
            if self.toss(i * i): # if an egg breaks
                break
            i += 1

        for i in range((i - 1) * (i - 1) +1, min(self.N, i * i)):
            if self.toss(i):
                return i
        return min(self.N, math.pow(i, 2))