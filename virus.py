class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        """
        Instance properties:
        Name: string
        Repro_rate: number
        mortality_rate: number
        Attributes used in Simulation.
        """
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        
# Test this class
if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
