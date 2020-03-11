'''
To solve this combinatorial optimization (NP hard) problem, the code uses nearest neighbors
which is a greedy algorithm to find the nearest path between a node and its neighbors using
the 3-opt local search. To optimize the path, the algorith performs a 2-opt swap. It then
randomly jumps to another node (perturbation) to avoid being stuck at the local optimum.
'''
import itertools, random #itertools used to go through combinations and count, random produces pseudorandom integers
import os, time #os finds the path of the file and time calculates the runtime of the algorithm
import numpy as np #numpy is used for defining efficient arrays that hold city coordinates
import matplotlib.pyplot as plt #used for plotting the graphs

class TSP(object): #Defining a class called 'TSP' which corresponds to the traveling salesman problem
    def __init__(self, input_file_path): #Initiating the initial variables to be used in the class
        self.input_file_path = input_file_path #file path of the city coordinates
        self.data = [] #array that holds city coordinates for dynamic use without updating file
        self.random_solution = [] #array for holding a candidate solution
        self.total_cost = 0 #cost integer of the total distance of a combination
        self.distance_mat = None #distance matrix

    def read_instance(self): #function which reads the coordinates file is defined. Takes no inputs
        input_file = open(self.input_file_path, 'r').read().splitlines() #reading the file line by line
        input_file.pop(0) #popping the first line which is just the number of cities
        cities = np.array([tuple(map(int, coord.split()[1:])) for coord in input_file]) #store coordinates in np array
        self.data = cities #copy the coordinate values stored in 'cities' to data

    def generate_nearest_neighbour_solution(self): #function that finds the nearest city from a node. Takes no inputs.
        cities = self.data.copy().tolist() #convert the coordinate values stored in data to list and store in cities
        random_selected_city = random.randint(0, len(cities) - 1) #generate a random number from 1 to the list length
        new_route = [cities[random_selected_city]] #pick the index of the city using the random number
        cities.pop(random_selected_city) #remove the coordinate of that specific city using pop(index)

        while len(cities) >= 1: #while there is a city left in the cities list
            last_city = np.array(new_route[-1]) #pick the last randomly generated number
            pending_cities = np.array(cities) #convert the cities list to an np array
            distances_arr = [self.euclidean_distance(last_city, c2) for c2 in pending_cities] #get the distance and store to array
            min_dist_idx = np.argmin(distances_arr) #get the minimum distance
            nearest_city = pending_cities[min_dist_idx].tolist() #the minimum distance is the nearest city
            new_route.append(nearest_city) #record the city as the nearest neighbor
            cities.remove(nearest_city) #remove that neighbor city from the cities array

        self.random_solution = new_route #store the latest new route to random solution after end of while loop
        self.total_cost = self.calc_tour_cost(new_route) #calculte the tour cost of visiting that new route

    def init_solution(self): #function that initializes a random solution as a starting point
        copied_data = self.data.copy() #copy data array to copied data
        data_len = copied_data.shape[0] # get the shape of the array
        for _ in range(data_len): #for all the elements in the shape of the array
            n1 = random.randint(0, data_len - 1) #generate a number from 1 to shape of list
            n2 = random.randint(0, data_len - 1) #generate a second number from 1 to shape of list

            copied_data[[n1,n2]] = copied_data[[n2,n1]] #invert the values at index n1 and n2 of copied data at random

        self.random_solution = copied_data.tolist() #store as a random solution approach
        self.total_cost = self.calc_tour_cost(copied_data) #get the cost of that tour

    def calc_tour_cost(self, cities): #function that calculates cost to tour city. Takes the coordinates of the cities as inputs
        cities_np_arr = np.array(cities) #convert cities list to a numpy array
        total_distance = 0.0 #Define the total population as 0
        for i in range(len(cities_np_arr)):#For the length of the coordinates array (used as an index)
            total_distance += self.euclidean_distance(cities_np_arr[i - 1], cities_np_arr[i]) #get the shortest distance between each point
        return total_distance #return the distance around the points in a straight line

    @staticmethod
    def euclidean_distance(c1, c2): #shortest distance calculation
        return np.linalg.norm(c2-c1) #get the shortest path between points c1 and c2

    def generate_combinations(self, cities, node1, node2, node3): 
        #Function that generates 8 possible combinations from 3 cities. Takes the 3 neighboring nodes as inputs.
        combo_1 = cities[:node1[0] + 1] + cities[node1[1]:node2[0] + 1] + cities[node2[1]: node3[0] + 1] + cities[node3[1]: ]
        combo_2 = cities[:node1[0] + 1] + cities[node1[1]:node2[0] + 1] + cities[node3[0]: node2[1] - 1: -1] + cities[node3[1]: ]
        combo_3 = cities[:node1[0] + 1] + cities[node2[0]:node1[1] - 1: -1] + cities[node2[1]: node3[0] + 1] + cities[node3[1]: ]
        combo_4 = cities[:node1[0] + 1] + cities[node2[0]:node1[1] - 1: -1] + cities[node3[0]: node2[1] - 1: -1] + cities[node3[1]: ]
        combo_5 = cities[:node1[0] + 1] + cities[node2[1]: node3[0] + 1] + cities[node1[1]:node2[0] + 1] + cities[node3[1]: ]
        combo_6 = cities[:node1[0] + 1] + cities[node2[1]: node3[0] + 1] + cities[node2[0]:node1[1] - 1: -1] + cities[node3[1]: ]
        combo_7 = cities[:node1[0] + 1] + cities[node3[0]: node2[1] - 1: -1] + cities[node1[1]:node2[0] + 1] + cities[node3[1]: ]
        combo_8 = cities[:node1[0] + 1] + cities[node3[0]: node2[1] - 1: -1] + cities[node2[0]:node1[1] - 1: -1] + cities[node3[1]: ]

        combinations_array = [combo_1, combo_2, combo_3, combo_4, combo_5, combo_6, combo_7, combo_8]
        distances_array = list(map(lambda x: self.calc_tour_cost(x), combinations_array))
        min_distance = int(np.argmin(distances_array))
        return combinations_array[min_distance], distances_array[min_distance]

    def opt_3_local_search(self, route):
        '''
        Generates all possible combinations of the 7 different city paths and chooses the one with the least cost
        Returns: updated coordinates and the least tour cost
        '''
        all_combinations = list(itertools.combinations(range(len(route)), 3))
        random_city = np.random.randint(low=0, high=len(route))
        all_combinations = list(filter(lambda x: random_city in x, all_combinations))

        for idx, item in enumerate(all_combinations):
            a1, c1, e1 = item
            b1, d1, f1 = a1+1, c1+1, e1+1

            route, distance = self.generate_combinations(route, [a1, b1], [c1, d1], [e1, f1])

        distance = self.calc_tour_cost(route)
        return route, distance

    def perform_2_opt_swap(self):
        '''
        Performs a 2-opt swap of the cities to change the ordering
        Return: the coordinates of the swapped citied
        '''
        cities = self.random_solution.copy()
        size_of_cities = len(cities)
        for i in range(5):
            c1, c2 = random.randrange(0, size_of_cities), random.randrange(0, size_of_cities)
            exclude = {c1}
            exclude.add(size_of_cities - 1) if c1 == 0 else exclude.add(size_of_cities - 1)
            exclude.add(0) if c1 == size_of_cities - 1 else exclude.add(c1 + 1)
            while c2 in exclude:
                c2 = random.randrange(0, size_of_cities)
            if c2 < c1:
                c1, c2 = c2, c1

            assert 0 <= c1 < (size_of_cities - 1)
            assert c1 < c2 < size_of_cities

            cities[c1:c2] = reversed(cities[c1:c2])
        return cities

    def acceptance_criterion(self, best_found):
        #Compares the existing best solution with the solution obtained from perturbation and local search.
        best_dist = self.calc_tour_cost(best_found)

        if random.random() < 0.05: #5% probabilistic chance
            self.random_solution = best_found
            self.total_cost = best_dist
        else:
            if best_dist < self.total_cost:
                self.random_solution = best_found
                self.total_cost = best_dist

    def main(self, initial_solution, file_name, iter_count): #takes a solution, the file and number of simulated events
        def plot_graph(cities, length_of_route, file_name): #function that plots the graph given the inputs
            cities_arr = np.array(cities)
            cities_arr = np.vstack([cities_arr, cities_arr[0]])
            plt.title("Length of the route is {}".format(length_of_route))
            plt.scatter(cities_arr[:, 0], cities_arr[:, 1])
            plt.plot(cities_arr[:, 0], cities_arr[:, 1])
            plt.show() #display the graph

        self.read_instance() #read the coordinates from the file
        if initial_solution == "nn":
            self.generate_nearest_neighbour_solution() #Get the nearest neighbours from it
        else:
            self.init_solution() #To prevent the program from crashing, I will randomly generate points
    
        #Plot initial graph with randomized solution
        plot_graph(self.random_solution, self.total_cost, 'final_graph_{}_{}_{}'.format(file_name, initial_solution, iter_count))

        # Start 3 OPT Local Search
        opt_3_local_search_start_time = time.time()
        route, distance = self.opt_3_local_search(self.random_solution)
        self.random_solution = route
        self.total_cost = distance #distance is the same as cost of the route
        seconds_to_run = 10 #the algorithm runs for 10 seconds
        counter = itertools.count()
        elapsed_time = time.time() #get the current time
        while time.time() - elapsed_time < seconds_to_run:
            cities = self.perform_2_opt_swap()
            if time.time() - elapsed_time < seconds_to_run:
                best_perturbed_solution, distance = self.opt_3_local_search(cities)
                self.acceptance_criterion(best_perturbed_solution)
                next(counter)
        #Plot final graph with solution
        plot_graph(self.random_solution, self.total_cost, 'final_graph_{}_{}_{}'.format(file_name, initial_solution, iter_count))

def run(iter_count, ip_file): #run the from the file
    tsp = TSP(ip_file) #calling the class
    tsp.main('random', 'test.tsp', iter_count) #running the main function where all the functions are called in

if __name__ == '__main__':
    file_name = 'test.tsp' #name of the coordinates file
    total_iteration_count = 0 #number of simulations: 0 is actually just the first simulation
    run(total_iteration_count, file_name) #calling the run function
    print("Done") #print done to signify completion