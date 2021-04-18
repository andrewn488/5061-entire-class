"""
TW 13
"""

import math, random, pylab, statistics


class Runner:
    """" Class to represent a runner with initial speed and stamina, as well as simulate them running a route.

        >>> joe = Runner(initial_speed=5.8, stamina=210)
        >>> joe
        Runner(5.8, 210)
        >>> sally = Runner(6.2, 240)
        >>> sally
        Runner(6.2, 240)
    """

    def __init__(self, initial_speed = 6.0, stamina = 200):
        self.number = random.randint(0, 100000000)
        self.elapsed_time = 0
        self.total_distance = 0
        self.initial_speed = initial_speed
        self.stamina = stamina


    def __repr__(self):
        """ Returns a string representation of the runner as:
            "Runner(self.initial_speed, self.stamina)"
        """
        return "Runner(%.1f, %d)" % (self.initial_speed, self.stamina)


    def speed(self, grade = 0.0):
        """ Returns the runner's current speed in minutes per mile using the following grade-adjusted exponential
            decay formula:

            s(t) = s_0 * e^(-t/m) + (5.4*g)

            Where:
            s_0 is initial speed in minutes/mile
            t is time in minutes
            m is stamina factor
            g is grade of route

            Additionally, speed is adjusted by normally distributed random factor with mean 1.0, stdev 10%.
        """
        current_speed = self.initial_speed * math.exp(-self.elapsed_time / self.stamina) + (5.4*grade)
        return random.gauss(1.0, 0.1) * current_speed

    def run(self, miles, grade = 0.0):
        """ Simulates the runner running for given miles @ the given grade and updates
            the elapsed time and total distance for this runner.
        """
        current_speed = self.speed(grade)
        time_elapsed_for_current_section = current_speed * miles # min/mi * mi = minutes
        self.total_distance = self.total_distance + miles
        self.elapsed_time = self.elapsed_time + time_elapsed_for_current_section

    def __str__(self):
        """ Returns a string representation of the runner as:
            "Runner(self.initial_speed, self.stamina)"
        """
        return "Runner(%.1f, %d)" % (self.initial_speed, self.stamina)


    def __eq__(self, other):
        """ Implementation of equality comparison for this class. If the other
            object being compared is a runner, will compare against the 3
            unchanging class variables:
                1. Unique Runner Number (generated at random upon initialization)
                2. Initial Speed
                3. Stamina

            Returns True if equal with other object, False otherwise.
        """
        if isinstance(other, Runner):
            return (
                    self.number == other.number and
                    self.initial_speed == other.initial_speed and
                    self.stamina == other.stamina
            )
        return False
    def __lt__(self, other):
        """ Compares runner to another runner based on elapsed time (less time elapsed means faster runner).

            Returns True if strictly faster, False otherwise.
        """
        if isinstance(other, Runner):
            return self.elapsed_time < other.elapsed_time
        return False

    def __le__(self, other):
        """ Compares runner to another runner based on elapsed time (less time elapsed means faster runner).

            Returns True if faster or equal, False otherwise.
        """
        if isinstance(other, Runner):
            return self.elapsed_time <= other.elapsed_time
        return False

    def __ge__(self, other):
        """ Compares runner to another runner based on elapsed time (less time elapsed means faster runner).

            Returns True if slower or equal, False otherwise.
        """
        if isinstance(other, Runner):
            return self.elapsed_time >= other.elapsed_time
        return False

    def __gt__(self, other):
        """ Compares runner to another runner based on elapsed time (less time elapsed means faster runner).

            Returns True if strictly slower, False otherwise.
        """
        if isinstance(other, Runner):
            return self.elapsed_time > other.elapsed_time
        return False

    def __ne__(self, other):
        """ Compares runner to another runner for inequality.

            Returns True if not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self):
        """ Hash implementation to provide the ability to use object as a key to dictionary for purposes
            of recording information in simulation function.
        """
        return hash(str(self) + str(self.number))


def simulate_races(course, num_races = 1000, num_racers = 100):
    """ Simulates the given course for the number of races (default 1000) with number of racers (default 100).

        After finishing simulation, displays a graph of mean finish times for each of the racers for all races.
    """
    # create 100 runners
    runners = []
    for i in range(num_racers):
        # mu 6.0 min/mi, stddev 1.2 min/mi
        initial_speed = random.gauss(6.0, 1.2) # get random initial speed with gaussian distribution parameters
        stamina = random.randint(100, 1000) # get random stamina factor [100,1000]
        runners.append(Runner(initial_speed, stamina)) # add runner to list

    race_finish_times_by_runner = {} # we want to store list of finish times for each race PER RUNNER

    # simulate 1000 races
    for i in range(num_races):
        # simulate race
        for route in course:
            # make each runner run the current route
            for runner in runners:
                runner.run(route[0], route[1])

        # get all finish times for this race
        for runner in runners:
            # if we need to init the list, init the list
            if runner not in race_finish_times_by_runner:
                race_finish_times_by_runner[runner] = []
            # otherwise append the racer's finish time to their list
            race_finish_times_by_runner[runner].append(runner.elapsed_time)

    # calculate mean finish times for each racer
    mean_race_finish_times = []
    for runner in runners:
        # get mean finish time
        mean_finish_time_for_racer = statistics.mean( race_finish_times_by_runner[runner] )
        # append it
        mean_race_finish_times.append(mean_finish_time_for_racer)

    # create plot
    pylab.figure(1)  # start a plot called Figure 1
    pylab.hist(mean_race_finish_times, bins=20)  # plot a histogram of the values using 20 columns
    pylab.show()
