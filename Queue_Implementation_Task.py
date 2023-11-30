# Python 3.9.6 64-bit
# 2023-11-29

""" 
Task: Hospital Emergency Room Simulation

Background:
    Imagine you're building a simulation for a hospital's emergency room (ER). 
    The ER handles patients based on the severity of their condition and the order of arrival. 
    Patients with more severe conditions are treated before those with less severe conditions, 

Your Task:
1. Implement a Patient Queue System:
    Create a class Patient that includes attributes for name, condition_severity (an integer where a lower number indicates higher severity), and arrival_time.
    Implement a queue system that can add patients (add_patient) and process them (treat_patient).
    The queue should prioritize patients based on condition_severity and use arrival_time as a tiebreaker for patients with the same severity.

2. Simulate the ER Process:
    Write a function to simulate the arrival of patients. Randomly generate patient names, severity levels, and arrival times.
    Implement a loop to treat patients. Each iteration of the loop should treat one patient, simulating the process of an ER. Print the name of the patient being treated and their details.

3. Add a Feature to Handle Emergencies:
    Modify your queue system to handle such emergency cases.

4. Logging:
    Keep a log of patients as they are treated. After all patients have been treated, print out the log, showing the order in which patients were treated.

Learning Goals:
    Understand and implement a priority queue.
    Practice class design and object-oriented programming.
    Handle dynamic data management in a simulated real-world scenario.
    Learn to manage and prioritize data based on multiple criteria.
"""

from collections import deque 
import random as rd 

def random_patient_generator():
    # Simulate the arrival of patients. Randomly generate patient names, severity levels, and arrival times
    first_names = ['Eddy', 'Bob', 'Chris', 'Frank', 'Peter'] 
    last_names = ['Anderson', 'Willson', 'Jackson', 'Jones']

    patient_name = first_names[rd.randint(0, len(first_names)-1)] + " " + last_names[rd.randint(0, len(last_names)-1)]
    severity_level = rd.randint(1, 5) # Severity levels between 1-5
    arrival_time = f"{rd.randint(1, 24):02d}:{rd.randint(0, 59):02d}" # 24 Hours Based Time

    return [patient_name, severity_level, arrival_time]

class ProcessPatient():
    def __init__(self):
        self.er_queue = deque()
        self.patient = {} # Patient Name: Severity, Arrival
        self.log = [] # Patient Name: Treated Order

    def patient_log(self, name, order): #Save the order in which patients were treated
        self.log.append((order, name))

    def add_patient(self, name, severity_level, arrival_time): # Add Patient to the Emergency Room Queue
        # The queue should prioritize patients based on condition_severity and use arrival_time as a tiebreaker for patients with the same severity.
        if name not in self.patient.keys():
            self.er_queue.append((name, severity_level, arrival_time))
        else:
            return f"Patient: {name} already exists!"
        
    def simulation_process(self, current_patient, count):
        print(f"Currently Treating: {current_patient[0]} | Severity Level: {current_patient[1]} | Arrived At: {current_patient[2]}")
        process_patient_er.patient_log(current_patient[0], count)

    def process_patient(self):
        # Implement a loop to treat patients. Each iteration of the loop should treat one patient, simulating the process of an ER. Print the name of the patient being treated and their details.
        process_count = 0 

        # Bubble Sort Based on Severity Level and Arrival Time
        # I just learned about Queue and I didn't get to heapq yet, so I used bubble sort to complete the prioritization.
        for i in range(len(self.er_queue)-1):

            for j in range(i, len(self.er_queue)-1):

                if self.er_queue[i][1] < self.er_queue[j+1][1]: # Compare Severity Level
                    self.er_queue[i], self.er_queue[j+1] = self.er_queue[j+1], self.er_queue[i]
                
                elif self.er_queue[i][1] == self.er_queue[j+1][1]: # Equivalent
                    time_i = self.er_queue[i][2].replace(':', '')
                    time_j = self.er_queue[j+1][2].replace(':', '')

                    if int(time_j) < int(time_i): # Earlier
                        self.er_queue[i], self.er_queue[j+1] = self.er_queue[j+1], self.er_queue[i]

        while len(self.er_queue) > 0:
            current_patient = self.er_queue.popleft()
            print(process_count, current_patient)
            process_patient_er.simulation_process(current_patient, process_count)
            process_count += 1

process_patient_er = ProcessPatient()

for _ in range(20):
    name, severity_level, arrival_time = random_patient_generator()
    process_patient_er.add_patient(name, severity_level, arrival_time)
process_patient_er.process_patient()
