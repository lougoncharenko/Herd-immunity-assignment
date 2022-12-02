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
            f"\t Population Size: {pop_size}, \t Vaccination Percentage: {vacc_percentage}, \t Virus: name {virus_name}, \t mortality rate: {mortality_rate}, \t basic reproduction number: {basic_repro_num} /n"
        )
        filename.close()

        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        """
        This method logs the number of interactions, number of new infections and steps
        """
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        pass

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        """
        method that logs if the person survived, currrent population count and number of new fatalities
        """
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):
        """
        This method logs time step number
        """
        filename = open(self.file_name, "a")
        filename.write(f"Time Step Number: {time_step_number}")
        filename.close()       