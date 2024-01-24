class Solution(object):
    def largestAltitude(self,gain):
        max_altitude = 0
        current_altitude = 0

        for gain_value in gain:
            current_altitude += gain_value
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude


