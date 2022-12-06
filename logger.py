class Logger(object):
    """
    A helper class for logging all events that happen in the simulation.
    """
    def __init__(self, file_name):
        """
        Instance properties:
        File_name: string (full file name where logs will be written to)
        """
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        """
        This shows the starting data including:
        population, initial infected, the virus, and the initial vaccinated.
        """
        filename = open(self.file_name, "w")
        filename.write(
            f"\t Population Size: {pop_size} \t Vaccination Percentage: {vacc_percentage} \t Virus: name {virus_name} \t mortality rate: {mortality_rate} \t basic reproduction number: {basic_repro_num} \n"
        )
        filename.close()

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        """
        This method logs the number of interactions, number of new infections and steps
        """
        filename = open(self.file_name, 'a')
        filename.write(f" \t Step number: {step_number} \t Interactions: {number_of_interactions} \t New Infections: {number_of_new_infections} \n")
        filename.close()

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        """
        method that logs if the person survived, currrent population count and number of new fatalities
        """
        filename = open(self.file_name, "a")
        death_total = 0
        for person in number_of_new_fatalities:
             if not person.is_alive:
                 death_total += 1
        file_name.write(f"  \t Step Number: {step_number}  \t Population count: {population_count}  \t  Death Total: {death_total} \n")
        filename.close()

    def log_time_step(self, time_step_number):
        """
        This method logs time step number
        """
        filename = open(self.file_name, "a")
        filename.write(f" \t Time Step Number: {time_step_number} \n")
        filename.close()       