"""import time: needed for time.ctime(), current time, and time.time(), computers internal clock
   import random: needed for random.seed() and random.random()
   import sys: needed for sys.exit()
   import csv: need for reading/writing a csv file whereas in this case we're just writing"""
		
import time	 
import random	
import sys	
import csv	


"Pump class"

class Pump:
	
	"""constructor function"""
	"""start is the initial amount of fuel in the tank in gallons, todaysPrice in $'s"""
	def __init__(self, start = 1000, todaysPrice = 3.099): 
		self.TankAmt = start
		self.todaysPrice = todaysPrice

	def values(self):
		print ('The gas tank has',self.TankAmt,'gallons of fuel')
		print ('The price per gallon of gas is:  $',self.todaysPrice,'\n\n\n')
		return

	def request(self, pumpAmt):
		if (self.TankAmt >= pumpAmt):
			pumped = pumpAmt
		else:
			if (self.TankAmt == 0):
				print('\nNo more fuel left...sorry!\n\n')
				sys.exit()
			else:
				pumped = self.TankAmt
		self.TankAmt -= pumped
		print (pumpAmt,'gallons were requested')
		print (round(pumped,2),'gallons were pumped')
		print (round(self.TankAmt,2),'gallons remain in the tank')
		print ('The total price is:  $',round(pumped*self.todaysPrice, 2),'\n\n')
		data = [time.ctime(), round(pumped, 2), round(self.TankAmt, 2), self.todaysPrice, round(pumped*self.todaysPrice, 2)] 
		return data		


"""Customer class"""

class Customer:

	"""constructor function"""
	"""random.seed() creates a random seed value needed so that random() does not create the same series of random numbers"""
	def __init__(self):       
		random.seed(time.time()) 
		"""seed value for random number generated based off of computer clock"""

	def arrive(self):
		return round(1 + round(100*random.random(),2) % 15, 2)  
		"""creates a random value between 1 and 15"""
	
	def gallons(self):
		return round(3 + round(100*random.random(),2) % 18, 2)
		"""creates a random value between 3 and 20"""


"""Function to write csv file"""

def writefile(dlist):

	"""thedata is basically a header for the csv file"""
	thedata = [['Date','Pumped Amount','Tank Amount',"Today's Price",'Purchase Amount']]

	"""This next step effectively merges lists thedata and dlist from main() creating a final list to write to csv"""
	thedata.extend(dlist)
	myFile = open('analysis.csv','w') 

	with myFile:	
		filewriter = csv.writer(myFile)
		filewriter.writerows(thedata)


"""main function"""

def main():
	
	SIMTIME = 5   
	"""Simulation time in hours"""
	MINUTES = 60
	totalTime = 0

	SimMinutes = SIMTIME * MINUTES
	print ('\n\n\n\nStarting a new simulation - simulation time is ',SimMinutes,' minutes \n')
	a = Pump()
	a.values()

	"""get the first arrival"""
	b = Customer()
	idleTime = b.arrive()
	totalTime += idleTime

	"""initializing dlist as an empty list to be appended below"""
	dlist = []
	
	while (totalTime <= SimMinutes):
	
		"""This adds the convenience of posting idle and/or simulation times in terms of appropiate units of measure""" 
		if idleTime >= MINUTES and totalTime >= MINUTES:
			print ('The idle time is',round(idleTime/MINUTES, 2),'hours and we are',round(totalTime/MINUTES, 2),'hours into the simulation')
		
		elif idleTime >= MINUTES and totalTime < MINUTES:
			print ('The idle time is',round(idleTime/MINUTES, 2),'hours and we are',round(totalTime, 2),'minutes into the simulation')
		
		elif idleTime < MINUTES and totalTime >= MINUTES:
			print ('The idle time is',idleTime,'minutes and we are',round(totalTime/MINUTES, 2),'hours into the simulation')
		else:
			print ('The idle time is',idleTime,'minutes and we are',round(totalTime, 2),'minutes into the simulation')
	
		"""Get the requested amount of fuel and store it in list dlist, which is part of a csv file""" 
		amtRequest = b.gallons()
		data = a.request(amtRequest)
		dlist.append(data)
					
		"""Get the next arrival"""
		idleTime = b.arrive()
		totalTime += idleTime

	writefile(dlist)

	"""Again an added convinience to posting of the idle time in terms of appropriate units"""
	if idleTime >= MINUTES:
		print ('The idle time is ',round(idleTime/MINUTES, 2),' hours.\nAs the total time now exceeds the simulation time, ')
	else:
		print ('The idle time is ',idleTime,' mintues.\nAs the total time now exceeds the simulation time, ')

	print ('this simulation is over.')
	return

"""Obligatory script to call the main() function to begin the program"""
if __name__=='__main__':
	main()	
