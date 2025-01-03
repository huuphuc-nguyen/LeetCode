class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, char in enumerate(senate):
            if char == "R":
                radiant.append(i)
            else:  # char == "D"
                dire.append(i)

        n = len(senate)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)  # Radiant wins this round, goes to the back
            else:
                dire.append(d + n)  # Dire wins this round, goes to the back

        return "Radiant" if radiant else "Dire"

            