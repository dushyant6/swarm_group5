import matplotlib.pyplot as plt
import numpy

def isfloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def load_data():
	file4 = open(r'neighbors.csv','r')
	#file4 = open(r'Sheet1.csv','r')
	#file4 = open(r'HW9.csv','r')
	file_lines = []

	list_of_lists = []

	#number of robots
	n  = 30


	for m in range(n):
		robot_number = m
		globals()["robot_"+str(robot_number)]= []
		globals()["robot_"+str(robot_number) +"dist"]= []
		list_of_lists.append(globals()["robot_"+str(robot_number)])
		
	for count, line in enumerate(file4):
		x = line.strip().split(',')
		robot_number = x[0]
		if len(x)%2 == 0:
			#this is a valid row
			pass
		else:
			x = x[:-1]
		if(len(x) != 0):
			if(x[0].isnumeric()):
				if(len(x) > 2 and (str(x[0]) + " sees neighbors: ") == x[1]):
					neigh_list = []
					dist_list = []
					for i in range(len(x)-1):
						if (isfloat(x[i]) and isfloat(x[i+1])): 					
							if (i%2 == 0 and i > 1):
								neigh_list.append(float(x[i]))
								dist_list.append(float(x[i+1]))
					globals()["robot_"+str(robot_number)].append(neigh_list)
					globals()["robot_"+str(robot_number)+"dist"].append(dist_list)

	robot_neigh_list = []
	robot_neigh_dist_list = []


	for m in range(n):
		robot_number = m
		robot_neigh_list.append(globals()["robot_"+str(robot_number)])
		robot_neigh_dist_list.append(globals()["robot_"+str(robot_number) +"dist"])
	
	return robot_neigh_list, robot_neigh_dist_list	

def sanity_check(robot_neigh_list, robot_neigh_dist_list):
	for i in range(len(robot_neigh_list)):
		for j in range(len(robot_neigh_list[i])):
			if len(robot_neigh_list[i][j]) != len(robot_neigh_dist_list[i][j]):
				print(f'Fault in data importing')
	print('done data importing')
	return
	
def main():
	robot_neigh_list, robot_neigh_dist_list = load_data()
	sanity_check(robot_neigh_list, robot_neigh_dist_list)
	print(f'length of robot_neigh_list = {len(robot_neigh_list)}')
	print(f'length of robot_neigh_dist_list = {len(robot_neigh_dist_list[0])}')



if __name__ == "__main__":
	main()
