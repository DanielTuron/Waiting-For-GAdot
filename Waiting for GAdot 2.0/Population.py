import numpy as np
import time
import pickle
from pynput import keyboard
from Organism import Organism
from skimage import color
import cv2

class Population:
    
    def __init__(self,realImageFile,mutationFunction, breedingFunction, selectionFunction,fitnessFunction,myFile,*,lims=None,startingGenes = 50, sizePop = 200):
        print("--------------creating population----------------")
        self.myFile = myFile
        self.realImage = color.rgb2lab(cv2.imread(realImageFile))
        self.mutate = mutationFunction
        self.breed = breedingFunction
        self.selection = selectionFunction
        pop = []
        for i in range(sizePop):
            organism = Organism(self.realImage,fitnessFunction,None,lims,startingGenes = startingGenes)
            pop.append(organism)
        self.population = pop
        self.optimalSolution = None
        self.optimalFitness = np.NINF
        self.generation = 0
        self.population.sort(key=lambda x: x.fitness, reverse = True)

    def continueInterface(self):
        global keepGoing
        keepGoing = True
        def on_press(key):
            global keepGoing
            try:
                k = key.char  # single-char keys
            except:
                k = key.name  # other keys
            if k in ['q','Q']:  # keys of interest
                # self.keys.append(k)  # store it in global-like variable
                print('q key pressed, finishing generation then stopping')
                keepGoing = False
                return False  # stop listener; remove this if want more keys
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread
        while(keepGoing):
            print("-----------gen",self.generation,"completed. Starting gen",self.generation+1,"...            Press q to stop----------------")
            start_time = time.time()
            self.nextGen()
            
            print("fitness: ",self.optimalFitness)
            print("--- %s seconds ---" % (time.time() - start_time))
            if(self.generation%10==0):
                self.savePop()
                print("-------------    saving...   ---------------------")

        self.savePop()
        print("Saved population to - ",self.myFile)
        inp = input("Enter p to plot optimal solution - Enter c to continue to next generation - Enter anything else to quit \n")
        if(inp == 'p'):
            self.optimalSolution.makeImage()
        if(inp == 'c'):
            self.continueInterface()

    def savePop(self):
        filehandler = open(self.myFile,'wb')
        pickle.dump(self, filehandler)

    def nextGen(self):
        self.selection(self)
        self.generation = self.generation + 1
        self.population.sort(key=lambda x: x.fitness, reverse = True)
        if self.population[0].fitness > self.optimalFitness:
            self.optimalSolution = self.population[0]
            self.optimalFitness = self.optimalSolution.fitness

    def orderedInsert(self,baby):
        babyF = baby.fitness
        beggining = 0
        end = len(self.population)
        while(end!=beggining):
            mid = (beggining + end)//2
            midF = self.population[mid].fitness
            if(midF==babyF):
                break
            elif(midF<babyF):
                beggining = mid + 1
            else:
                end = mid
        self.population.insert(mid,baby)
        

