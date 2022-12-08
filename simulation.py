import random, sys
from person import Person
from logger import Logger
from virus import Virus
import argparse

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
        self.people = self._create_population()
        self.newly_infected = []
        self.vaccinated_population = []
        self.fatalities = []
        self.time_step_number = 0

    def _create_population(self):
        """
        Method create a list of people (Person instances).
        Returns: The list of people
        """
        people = []
        infected_people = []
        uninfected_people = []

        for i in range (0, self.initial_infected):
            infected_person = Person (i, False, self.virus)
            infected_people.append(infected_person)

        uninfected_population = self.pop_size - self.initial_infected
        for i in range(0, uninfected_population):
            uninfected_person = Person(i, False)
            uninfected_people.append(uninfected_person)
        people = uninfected_people + infected_people

        for person in people:
            if person.is_vaccinated:
                self.vaccinated_population(person)

        print(len(people))
        self.people = people
        return self.people

    def _simulation_should_continue(self):
        """
        Method loops through people list to determine if everyone is dead or vaccinated
        Returns boolean to determine if the simulation should continue.
        """
        infected_population = 0
        vaccinated_population = 0
        for person in self.people:
            if person.is_alive and person.infection is not None:
                infected_population += 1
            if person.is_alive and person.is_vaccinated == True:
                vaccinated_population +=0

        if infected_population > 0 and vaccinated_population > 0:
            return True
        else:
            return False
   

    def run(self):
        """
        Method starts the simulation and tracks the number of steps the simulation has run.
        """
        should_continue = True

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate )
        
        #simulation loop
        while should_continue:
            self.time_step_number += 1
            self.time_step()
            should_continue = self._simulation_should_continue()
        
    def time_step(self):
        """
        This method simulates interactions between people, calulate new infections,
        and determine vaccinations and fatalities from infections
        """
        if len(self.people) < 100:
            random_people = random.choices(self.people, k=len(alive_people))   
        else:
            random_people = random.choices(self.people, k=100)

        for person in self.people:
           if person.infection:
                for random_person in random_people:
                    self.interaction(person, random_person)

        self._infect_newly_infected() 
        

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
        number_of_new_fatalities = 0

        for person in self.newly_infected:
            if person.is_alive == True:
                person.infection = self.virus
                survived = person.did_survive_infection()
            if survived:
                self.vaccinated_population.append(person)
            else: 
                number_of_new_fatalities += 1
                self.pop_size -= 1
                self.fatalities.append(person)
    
        alive_population = []
        for person in self.people:
             if person not in self.fatalities:
                alive_population.append(person)
        self.people = alive_population
        self.logger.log_infection_survival(self.time_step_number, self.pop_size, number_of_new_fatalities )
        self.newly_infected = []

if __name__ == "__main__":
    #parse CLI arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('pop_size', metavar='population size', type=int, help='Enter a number for the population size: ')
    parser.add_argument('vacc_percentage', metavar='vacc_percentage', type=float, help='Enter a decimal number without the percent sign for the the vaccination percentage: ')
    parser.add_argument('virus_name', metavar='virus', type=str, help='Enter a name for the virus: ')
    parser.add_argument('virus_repro', metavar='virus_repro', type=float, help='Enter a decimal number for the virus reproduction rate: ')
    parser.add_argument('virus_mortality', metavar='virus_mortality', type=float, help='Enter a decimal number for the virus mortality rate: ')
    parser.add_argument('initial_infected', metavar='initial_infected', type=int, help='Enter a number for initially infected')

    args = parser.parse_args()
    cli_virus_name = args.virus_name
    cli_virus_repro = args.virus_repro
    cli_virus_mortality = args.virus_mortality
    cli_pop_size = args.pop_size
    cli_vacc_percentage = args.vacc_percentage
    cli_initial_infected = args.initial_infected

    cli_virus = Virus(cli_virus_name, cli_virus_mortality, cli_virus_repro)
    cli_simulation = Simulation(cli_virus, cli_pop_size, cli_vacc_percentage, cli_initial_infected)
    cli_simulation.run()
