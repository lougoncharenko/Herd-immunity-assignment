################################################################################
## To run the tests, first make sure you have pytest installed:
##
## $ pip3 install pytest
##
## Then, open up a terminal to the homework folder and run the following:
##
## $ pytest
##
################################################################################

import pytest
import io
import sys
from virus import Virus
from simulation import Simulation

#test Virus class
def test_virus_instance():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus

def test_virus_name():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"

def test_virus_repro_rate():
     virus = Virus("HIV", 0.8, 0.3)
     assert virus.repro_rate == 0.8

def test_virus_mortality_rate():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.mortality_rate == 0.3

# test person class

# test simulation class
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # # Make a new instance of the imulation
    virus = Virus(pop_size, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()

