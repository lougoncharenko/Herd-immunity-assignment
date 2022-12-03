import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        """
        Attributes:
        self.logger: instance of Logger class
        virus: instance of Virus class
        pop_size: integer
        vacc_percentage: integer
        initial_infected: integer
        self.people: list
        self.newly_infected: list
        """
        self.logger = Logger('logger.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.people = self._create_population(self.virus)
        self.newly_infected = list()

    def _create_population(self, virus):
        """
        Method create a list of people (Person instances).
        Returns: The list of people
        """
        people = []
        for i in range(0, self.initial_infected):
            infected_people =Person(i, False, self.virus)
            people.append(infected_people)
        uninfected_population = self.pop_size - self.initial_infected
        for i in range(0, uninfected_population):
            uninfected_people = Person(i, False)
            people.append(uninfected_people)
        return people

    def _simulation_should_continue(self):
        """
        Method loops through people list to determine if everyone is dead or vaccinated
        Returns boolean to determine if the simulation should continue.
        """
        for person in self.people:
            survived = person.did_survive_infection()
            if survived == True:
                survived = did_survived = did_survived +1
            else:
                did_not_survive = did_not_survive +1
            if did_not_survive == self.pop_size or person.is_vaccinated == self.pop_size:
                return False
            else: 
                return True
   

    def run(self):
        """
        Method starts the simulation and tracks the number of steps the simulation has run.
        """
        time_step_counter = 0
        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate )
        while should_continue:
            time_step_counter += 1
            self.time_step()
            self.logger.log_time_step(time_step_counter)
            should_continue = self._simulation_should_continue()
        
    def time_step(self):
        """
        This method simulates interactions between people, calulate new infections,
        and determine vaccinations and fatalities from infections
        """
        alive_people = []
        random_people = []
        infected_people = []
        uninfected_people = []
        # SEPERATE ALIVE PEOPLE FROM DEAD PEOPLE, Creates infected and uninfected list
        for person in self.people:
            if person.is_alive == True:
                alive_people.append(person)
            if person.infection is None:
                uninfected_people.append(person)
            if person.infection is not None:
                infected_people.append(person)

        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        pass

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        # self.logger.log_interactions( )
        pass

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
