'''
Created on 2022/07/07

@author: mori
'''
import numpy as np

class Individual:
    def __init__(self,size=10):
        self._size=size
        self._chromosome = np.array(np.random.randint(0,2,size))     
       
    def getSize(self):
        return self._size
    def getChromosome(self):
        return self._chromosome
    def getGene(self,i):
        return self._chromosome[i]
    def setGene(self,i,value):
        self._chromosome[i]=value
    def __str__(self):
        return str(self._chromosome)
    def __len__(self): #same as self.getSize()
        return self._chromosome.size
    def fitness(self):
        return sum(self._chromosome) #OneMax problem

        
def mutation(pop):
    mutation_rate=1/len(pop[0]) #common setting
    for indiv in pop:
        for i in range(len(indiv)):
            rnd=np.random.rand()
            if(rnd<mutation_rate):
                if(indiv.getGene(i)==1):
                    indiv.setGene(i,0)
                else:
                    indiv.setGene(i,1)

def crossover(pop):
    print("crossover") 
    
def selection(pop):
    print("selection")

def getElite(pop):
    elite=pop[0]
    bestFitness=pop[0].fitness()
    for indiv in pop[1:]:
        if(indiv.fitness()>bestFitness):
            elite=indiv
            bestFitness=indiv.fitness()
    return elite
    
def printPop(pop):
    for indiv in pop:
        print(indiv,indiv.fitness())
         
#main
if __name__=="__main__":
    pop_size=10
    generation_size=100
    pop=[Individual(20) for i in range(pop_size)]
    
    for t in range(generation_size):
        mutation(pop)
        crossover(pop)
        selection(pop)
    elite = getElite(pop)
    print(elite,elite.fitness())


