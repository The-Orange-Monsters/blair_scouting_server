import dataconstants
# from getdata import percent


# Helper function to convert floats to percents and round
def percent(n):
    return str(int(n * 100))


# Calculates data we want for teams on the other alliance
class OtherAlliance:
    total, lowh, lowc, highc, highh = [0] * 5
    habsuccess = [0, 0, 0, 0]

    def __init__(self, team):
        self.team = team

    def add_line(self, line):
        self.total += 1

        self.lowc += int(line[dataconstants.CSC]) + int(line[dataconstants.L1RC])
        self.lowh += int(line[dataconstants.CSH]) + int(line[dataconstants.L1RH])
        self.highc += int(line[dataconstants.L2RC]) + int(line[dataconstants.L3RC])
        self.highh += int(line[dataconstants.L2RH]) + int(line[dataconstants.L3RH])

        self.habsuccess[int(line[dataconstants.HAB_ATTEMPT])] += line[dataconstants.HAB_SUCCESS] == '3'

    def tostring(self):
        if self.total:
            lowc = str(self.lowc / self.total)
            lowh = str(self.lowh / self.total)
            highc = str(self.highc / self.total)
            highh = str(self.highh / self.total)

            success = percent(self.habsuccess[2] / self.total) + ':' + \
                      percent(self.habsuccess[3] / self.total)

            order = [self.team, '', lowh, lowc, highc, highh, dataconstants.PLACE_HOLDER, success,
                     dataconstants.PLACE_HOLDER]
            return dataconstants.SEP.join(order)
        return self.team + ': ' + dataconstants.NO_DATA
