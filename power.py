"""
CIS-218 Final Lab
"""
# import unittest


class Power:
    """main class of Power"""

    def __init__(self, _name, _megawatts, _age):
        """Create variables"""
        self.name = _name
        self.age = _age
        self.megawatts = _megawatts
        self.lifespan = 60

    def capacity(self):
        """method that calculates the actual amount of electricity the power plant can produce based on age"""
        print(self.megawatts)
        print(self.lifespan)
        print(self.age)
        capacity = round(self.megawatts - (self.megawatts / self.lifespan * self.age))
        print(capacity)
        return capacity

    def available(self):
        """method which returns True if the capacity is greater than 0 or False if otherwise"""
        capacity = self.capacity()
        return bool(capacity > 0)

    def __str__(self):
        """method that returns the name of the power plant and its capacity"""
        return self.name + " (" + str(self.capacity()) + " MW)"

    def __repr__(self):
        """method that displays the representation of the Power class"""
        return f'Power(name="{self.name}",megawatts={self.megawatts},age={self.age},lifespan={self.lifespan})'


class Wind(Power):
    """Subclass of Power"""

    def __init__(self, name, megawatts, age):
        """Create variables"""
        super().__init__(name, megawatts, age)
        self.lifespan = 25


class Nuclear(Power):
    """Subclass of Power"""

    def __init__(self, name, megawatts, age, cooling_towers):
        """Create Variables"""
        super().__init__(name, megawatts, age)
        self.__cooling_towers = cooling_towers

    def available(self):
        """method which returns True if the capacity is greater than 0 or False if otherwise"""
        capacity = super().capacity()
        return bool(capacity >= self.__cooling_towers * 100)


class TestCases:
    """Description"""

    def test_wind_availability(self):
        """Description"""
        test1 = Wind("testWind1", 100, 10)
        assert test1.available() is True

    def test_wind_capacity(self):
        """Description"""
        test2 = Wind("testWind1", 100, 10)
        assert test2.capacity() == 60

    def test_nuclear_availability(self):
        """Description"""
        test3 = Nuclear("testNuclear1", 600, 10, 10)
        assert test3.available() is False

    def test_nuclear_capacity(self):
        """Description"""
        test4 = Nuclear("testNuclear1", 600, 10, 10)
        assert test4.capacity() == 500

    def tests_str(self):
        """Description"""
        test5 = Wind("Test Wind Plant", 100, 0)
        assert test5.__str__() == "Test Wind Plant (100 MW)"

    def tests_repr(self):
        """Description"""
        test6 = Power("Test Nuclear Plant", 100, 0)
        assert (
            test6.__repr__()
            == 'Power(name="Test Nuclear Plant",megawatts=100,age=0,lifespan=60)'
        )


if __name__ == "__main__":
    power_plants = [
        Wind(name="Alta Wind Energy", megawatts=1320, age=12),
        Wind(name="Roscoe Wind Farm", megawatts=781, age=10),
        Wind(name="Shepherds Flat Wind Farm", megawatts=845, age=13),
        Nuclear(name="Palo Verde", megawatts=3942, age=36, cooling_towers=3),
        Nuclear(name="Browns Ferry", megawatts=3300, age=48, cooling_towers=6),
        Nuclear(name="South Texas", megawatts=2560, age=34, cooling_towers=0),
    ]
    available = [_ for _ in power_plants if _.available()]
    order = sorted(available, reverse=True, key=lambda plant: plant.capacity())
    named_list = [str(_) for _ in order]
    print(named_list)
