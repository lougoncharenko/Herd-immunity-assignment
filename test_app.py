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
