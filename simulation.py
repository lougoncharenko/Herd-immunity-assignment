import random, sys
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
        self.time_step_number: integer
        """
        self.logger = Logger('logger.txt')
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.people = self._create_population(self.virus)
        self.newly_infected = list()
        self.vaccinated = []
        self.time_step_number = 0

    def _create_population(self, virus):
        """
        Method create a list of people (Person instances).
        Returns: The list of people
        """
        people = []
        infected_people = []
        uninfected_people = []
        for i in range(0, self.initial_infected):
            infected_person =Person(i, False, self.virus)
            infected_people.append(infected_person)

        uninfected_population = self.pop_size - self.initial_infected
        for i in range(0, uninfected_population):
            uninfected_person = Person(i, False)
            uninfected_people.append(uninfected_person)
        return people

    def _simulation_should_continue(self):
        """
        Method loops through people list to determine if everyone is dead or vaccinated
        Returns boolean to determine if the simulation should continue.
        """
        vaccinated_person = len(self.people.is_vaccinated)
        alive_population = self.pop_size
        while unvaccinated_population > 0 and alive_population > 0:
            return True
        return False
   

    def run(self):
        """
        Method starts the simulation and tracks the number of steps the simulation has run.
        """
        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate )
        while should_continue:
            self.time_step_number += 1
            self.time_step()
            self.logger.log_time_step(self.time_step_number)
            should_continue = self._simulation_should_continue()
        
    def time_step(self):
        """
        This method simulates interactions between people, calulate new infections,
        and determine vaccinations and fatalities from infections
        """
        # TODO: Call self._infect_newly_infected(self)  at the end of every time step and infect each Person.
        alive_people = []
        infected_people = []
        uninfected_people = []
        random_people = []
        # SEPERATE ALIVE PEOPLE FROM DEAD PEOPLE, Creates infected and uninfected list
        for person in self.people:
            if person.is_alive == True:
                alive_people.append(person)
            if person.infection is None:
                uninfected_people.append(person)
            if person.infection is not None:
                infected_people.append(person)
        print(f"Alive people: {alive_people}, infected people: {infected_people}, uninfected people: {uninfected_people}")
        
        if len(alive_people) < 100:
            random_people = random.choices(alive_people, k=len(alive_people))   
        else:
            random_people = random.choices(alive_people, k=100)

        for infected_person in infected_people:
            for random_person in random_people:
                self.interaction(infected_person, random_person)

        
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
        number_of_interactions = 0
        if random_person.is_vaccinated == False:
            if random_person.infection is None:
                random_number = random.randint(0.0, 1.0)
                if random_number > self.virus.repro_rate:
                    number_of_interactions += 1
                    self.newly_infected.append(random_person)
                    number_of_new_infections = len(self.newly_infected)
                    self.logger.log_interactions(self.time_step_number, number_of_interactions, number_of_new_infections)

    def _infect_newly_infected(self):
        """
        Method loops through self.newly_infected to infect each person with the virus and resets 
        self.newly_infected back to an empty list
        """
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.infected_people:
            if person.is_alive == True:
                person.infection = self.virus
                person.did_survive_infection()

        self.newly_infected = []

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
    virus = Virus(pop_size, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
