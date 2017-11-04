%matplotlib inline
import scipy
import sympy
from modsim import *
import numpy as np

class EV():
	"""This class works out the number of EV on road by 2050."""
	def __init__(self, arg):
		super(EV, self).__init__()
		self.arg = arg

	@staticmethod
	def EV_cost():
		"""This function returns the final cost of EV for a consumer. It should decrease in the future as 
		the cost of manufacturing will decrease with accordance of economies of scale.."""
			pass	

	@staticmethod
	def Regulations():
		"""This function returns the final cost of CO2 and other regulations that will decrease the cost of 
		manufacturing and maintaining EVs. It works the way it should because regulations should decrease the cost of manufacturing
		 and running a EV."""
			pass

	@staticmethod
	def Subsidies_and_exemptions():
		"""This function returns the subsidies and exemptions that governments provide to cosumers for buying an EV."""
			pass

	@staticmethod
	def Resale_value():
		"""This function considers the impact of resale value on a consumer's choice to buy a EV."""
		pass


	@staticmethod
	def Total_EV_on_road():
		"""This function finally calculates the number of EVs on road by 2050."""
		pass




class Global_Oil_Demand():
	"""This class should work out the effect of Electric Vehicles on Global Oil Demand. I'll start working on this once we have 
	figured out Total_EV_on_road."""
	def __init__(self, arg):
		super(Global_Oil_Demand, self).__init__()
		self.arg = arg
		
	@staticmethod
	def Cost_of_oil():
		"""This function will calculate the cost of oil per barrel in the future."""
		pass