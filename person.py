import random
# random.seed(42)
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):
        """
        Instance properties:
        Id: Number
        is_vaccinated: Boolean
        infection: instance of virus
        """
        self._id = _id 
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        """
        This method only runs if person is infected by a virus
        If they are infected a random number between 0.0 and 1.0 is generated 
        and compared to the mortality rate of the virus, if it is less, they die.
        The method returns a Boolean showing if they survived.
        """
        if self.infection != None:
            random_number = random.randint(0.0, 1.0)
            if random_number < self.infection.mortality_rate:
                self.is_alive = False
            else:
                self.is_alive = True
                self.is_vaccinated = True
        return self.is_alive
       
if __name__ == "__main__":
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
 
    people = []
    virus = Virus("Dysentery", 0.7, 0.2)
    for i in range(0, 100):
          infected_person = Person(i, False, virus)
          people.append(infected_person)
    
    did_survived = 0
    did_not_survive = 0
    for person in people:
        survived = person.did_survive_infection()
        if survived == True:
            did_survived = did_survived +1
        else:
            did_not_survive = did_not_survive +1
    print(f'Number of people who did surive: {did_survived}')
    print(f"Number of people who didn't surive: {did_not_survive}")