'''
FQ20 - OMSBA 5061 - Week 10
​
TW14: World Series
​
Maroon Team: Chequala Fuller, Tamalyn Tamura, Andrew Nalundasan
​
Description: Write the WorldSeries class that models a baseball
world series. Make a stab at the simulation, too, if you have time.
'''
​
import random
​
​
class WorldSeries(object):
    """simulate the World Series of US baseball. The first team to
    win 4 games wins the series. Randomly pick the winner for each
    game using the given probability.
    
    >>> ws = WorldSeries('Boston Red Sox', 'New York Yankees', p=.73)
    >>> # story=True says print out results of each game and the series winner
    >>> bostonWins = ws.simulate(story=True)  
    Game 1: Boston Red Sox win (Boston 1 games: New York 0 games)
    Game 2: Boston Red Sox win (Boston 2 games: New York 0 games)
    Game 3: New York Yankees win (Boston 2 games: New York 1 games)
    Game 4: Boston Red Sox win (Boston 3 games: New York 1 games)
    Game 5: Boston Red Sox win (Boston 4 games: New York 1 games)
    Boston Red Sox win the series!
    >>> bostonWins
    True
    >>> # without story (using the default of story=False, it just returns if team1 won
    >>> ws.simulate() 
    True
    >>> if ws.simulate():
        print(ws.team1, "won!")
        else:
        print(ws.team2), "won!")
​
    New York Yankees won!
    """
    
    def __init__(self, team1, team2, p):
​
        self.team1 = team1
        self.team2 = team2
        self.p = p
        self.loc1 = 'Boston'
        self.loc2 = 'New York'
        #win = random.random() < p
​
    #def __str__(self, 
    
​
    #def random_win(self):
​
        #win = random.random() < p
        
        
                   
    def simulate(self, story = False):
        """returns the results of each game and the series winner, if story = True"""
​
        counter1 = 0
        counter2 = 0
        
        for n in range(1, 6):
            win = random.random()
            #print(win)
            #print(n)
            if win < self.p:
                counter2 += 1
            else:
                counter1 += 1
            print('Game %d: %s win (%s %d games: %s %d games)' % (n, self.team1, self.loc1,
                                                                 counter1, self.loc2, counter2))
        if counter1 > counter2:
            print('%s win the series!' % self.team1)
        else:
            print('%s win the series!' % self.team2)
