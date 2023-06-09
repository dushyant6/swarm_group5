#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:50:37 2023

@author: dushyant
"""
from csv_data_reader import *

class Swarm:
        def __init__(self, class_int, class_num, num_robots):
                #class int determines which class the robot belongs to, e.g. 1, 2, 3
                self.class_int = class_int
                self.class_num = class_num
                self.num_robots = num_robots
                #define list of robots with the id belonging to the class int
                self.robot_id_list = []
                for i in range(num_robots):
                        if i%class_num == class_int:
                                self.robot_id_list.append(i)
                self.class_size = len(self.robot_id_list)
                self.neigh_dict = {}
                for id in self.robot_id_list:
                        robot = Robot(id)
                        self.neigh_dict[id] = robot.clustered_neighbors
                self.cluster_size_list = self.cluster_size()

                        
        def cluster_size(self):
                #find minimum size of neighbor list among all robots (should be somewhat close and not cause too much loss of data)
                min_size = 0
                len_list = []
                for id in self.robot_id_list:
                        #print('id =', id)
                        robot = Robot(id)
                        len_list.append(len(robot.seen_distances))
                min_size = min(len_list)
                #print('min size/ time in seconds for experiment = ', min_size, 's')                        
                cluster_size_list = []
                keys = list(self.neigh_dict.keys())
                #print('keys = ', keys)
                
                for m in range(min_size):
                        max_cluster_size = 1
                        for point in keys:
                                cluster = []
                                for i in self.neigh_dict[point][m]:
                                        cluster.append(i)
                                        #print('point =', point, ', m =',m,', i =',i)
                                '''
                                for node in self.neigh_dict[point][m]:
                                        if(len(self.neigh_dict[node][m]) >0):
                                                for pt in self.neigh_dict[node][m]:
                                                        #print(pt, end = ",")
                                                        cluster.append(pt)
                                        #print("\n")
                                        '''
                                cluster = list(set(cluster))
                                cluster_size = len(cluster)
                                if cluster_size > max_cluster_size:
                                        max_cluster_size = cluster_size + 1 
                        cluster_size_list.append(max_cluster_size)
                return cluster_size_list

        def find_total_cost(self):
                #Find total cost at all instances for a swarm using cluster sizes. Need to correct cluster size logic as it is giving wrong answer currently
                return


class Robot:
        def __init__(self, id):
                self.id = id
                self.total_cost = 0
                self.instance_cost = 0
                self.seen_neighbors = []
                self.seen_distances = []
                self.seen_neighbors = self.get_neighbors()
                self.seen_distances = self.get_distances()
                self.clustered_neighbors = []
                self.clustered_neighbors = self.get_clustered_neighbors()
                self.time = []
                
        def get_neighbors(self):
                robot_neigh_list, _ = load_data()
                return robot_neigh_list[self.id]

        def get_distances(self):
                _, robot_neigh_dist_list = load_data()
                return robot_neigh_dist_list[self.id]

        def get_clustered_neighbors(self):
                clustered_neighbors = []
                for i in range(len(self.seen_distances)):
                        cluster = []
                        for j in range(len(self.seen_distances[i])):
                                if self.seen_distances[i][j] < 25:
                                        cluster.append(self.seen_neighbors[i][j])
                        clustered_neighbors.append(cluster)
                return clustered_neighbors
                
                
class test:
        def __init__(self):
                self.robot = Robot(4)


def cluster_size(neigh_dict):
        keys = list(neigh_dict.keys())
        max_cluster_size = 0
        for point in keys:
                cluster = []
                for i in neigh_dict[point]:
                        cluster.append(i)
                
                for node in neigh_dict[point]:
                        if(len(neigh_dict[node]) >0):
                                for pt in neigh_dict[node]:
                                        #print(pt, end = ",")
                                        cluster.append(pt)
                        #print("\n")
                cluster = list(set(cluster))
                cluster_size = len(cluster)
                if cluster_size > max_cluster_size:
                        max_cluster_size = cluster_size
        return max_cluster_size

def find_cost(num_classes, class_size, cluster_size):
        #gamma ration in Mitrano's paper
        gamma = -cluster_size/class_size
        return

keys = []
neigh_dict = dict()
for i in range(1,15):
        keys.append(i)
        neigh_dict[i] = []

neigh_dict[1] = [2,3,4,5,6, 7]
neigh_dict[5] = [1,4,6,12,13,14,11]
neigh_dict[4] = [2,3,10,11,12,5,6,1]
neigh_dict[3] = [1,2,4, 8, 9,10, 11]

cl_size = cluster_size(neigh_dict)
print('cluster_size =', cl_size)


a = test()
#print(len(a.robot.seen_distances))
#print(len(a.robot.seen_neighbors[40]))
#print('robot id =',a.robot.id)
y = a.robot.clustered_neighbors

test_swarm = Swarm(1, 3, 30)
z = test_swarm.cluster_size_list
#print(test_swarm.robot_id_list)
#print(test_swarm.cluster_size_list)