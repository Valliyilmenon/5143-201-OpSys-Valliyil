# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 01:39:29 2017
@author: tinubu helix
"""

import threading
from processStarter import commandChecker


#The shell class

#constructor
class shell(object):
	def __init__(self):
		self.command = commandChecker()
	
      #Function to start the shell and prompt for user input.
	def run(self):
		while True:
			#get userinput
			self.userInput = input("% ")
			
			
			#check user input for termination callable
			if str.upper(self.userInput) == "EXIT" or str.upper(self.userInput) =="close":
				exit()
			
			#call the accept command method
			else:
				self.command.acceptCommand(self.userInput)
	
	#function to exit shell
	def exit():
		raise SystemExit
		
		
		
class mainThread(object):
	#constructor
	def __init__(self):
		self.shellCall = shell()
		self.thread_t = None
		
	def run(self):
		self.thread_t = threading.Thread(target=self.shellCall.run)
		self.thread_t.start()
		self.thread_t.join()

if __name__ == '__main__':
	start = mainThread()
start.run()
