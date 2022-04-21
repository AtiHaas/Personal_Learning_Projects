#UROP Interview 
#____________________________________________________________________________________

#0) Importing libraries
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as pl
from scipy import stats

#____________________________________________________________________________________


#1) Defining a function that will turn the data from the .mat file to a numpy array

def matToNumpy(path):
    
    data = loadmat(path)
    Dx_T_dV = data['Dx_T_dV']
    
    return Dx_T_dV #Returning the .mat file as a numpy array


#____________________________________________________________________________________
    

#2) Importing the measured data
    
    #a) Defining the finder paths to the data 
path_17N  = r"/Users/atihaas/Library/CloudStorage/OneDrive-Personal/CV és mottivational letter/Ongoing/UROP/UROP Interview prep/Experimental hysteresis loops/14mum_100Hz_17N.mat" #Defining the path for the information
path_100N = r"/Users/atihaas/Library/CloudStorage/OneDrive-Personal/CV és mottivational letter/Ongoing/UROP/UROP Interview prep/Experimental hysteresis loops/14mum_100Hz_100N.mat" #Defining the path for the information
path_150N = r"/Users/atihaas/Library/CloudStorage/OneDrive-Personal/CV és mottivational letter/Ongoing/UROP/UROP Interview prep/Experimental hysteresis loops/14mum_100Hz_150N.mat" #Defining the path for the information

    #b) Turning these files into numpy arrays
Dx_T_dV_17N  = matToNumpy(path_17N)
Dx_T_dV_100N = matToNumpy(path_100N)
Dx_T_dV_150N = matToNumpy(path_150N)


#____________________________________________________________________________________


#3) Plotting the loops:

    #a) plotting the Friction force against the tangential relative displacement

#17N case:
for i in range(np.shape(Dx_T_dV_17N)[2]):
    pl.plot(Dx_T_dV_17N[:,0,i]*1000, Dx_T_dV_17N[:,1,i])
    pl.title("100 Hz, 17N loading case")
    pl.xlabel("Tangential relative displacement [\mum]")
    pl.ylabel("Friction force [N]")

pl.show()

#100N case:
for i in range(np.shape(Dx_T_dV_100N)[2]):
    pl.plot(Dx_T_dV_100N[:,0,i]*1000, Dx_T_dV_100N[:,1,i])
    pl.title("100 Hz, 100N loading case")
    pl.xlabel("Tangential relative displacement [\mum]")
    pl.ylabel("Friction force [N]")

pl.show()

#150N case:
for i in range(np.shape(Dx_T_dV_150N)[2]):
    pl.plot(Dx_T_dV_150N[:,0,i]*1000, Dx_T_dV_150N[:,1,i])
    pl.title("100 Hz, 150N loading case")
    pl.xlabel("Tangential relative displacement [\mum]")
    pl.ylabel("Friction force [N]")

pl.show()

    #b) plotting the friction force against the tangential relative velocity

#17N case:
for i in range(np.shape(Dx_T_dV_17N)[2]):
    pl.plot(Dx_T_dV_17N[:,2,i], Dx_T_dV_17N[:,1,i])
    pl.title("100 Hz, 17N loading case")
    pl.xlabel("Tangential relative velocity [mm/s]")
    pl.ylabel("Friction force [N]")

pl.show()
    
#100N case:
for i in range(np.shape(Dx_T_dV_100N)[2]):
    pl.plot(Dx_T_dV_100N[:,2,i], Dx_T_dV_100N[:,1,i])
    pl.title("100 Hz, 100N loading case")
    pl.xlabel("Tangential relative velocity [mm/s]")
    pl.ylabel("Friction force [N]")
    
pl.show()
    
#150N case:
for i in range(np.shape(Dx_T_dV_150N)[2]):
    pl.plot(Dx_T_dV_150N[:,2,i], Dx_T_dV_150N[:,1,i])
    pl.title("100 Hz, 150N loading case")
    pl.xlabel("Tangential relative velocity [mm/s]")
    pl.ylabel("Friction force [N]")
    
pl.show()
    
#____________________________________________________________________________________

    
#4) Finding the energy dissapated in a loop:

    #a) Defining the function that will preform the numerical integration
def trapeziumRuleGeneral(x,y):
    
    #Finding the number of nodes (n) and the subinrerval (h) between each neighbouring nodes (Here the nodes might not be equidistant!!)
    n = len(x)
    h = []
    for i in range(n-1):
        h.append(x[i+1] - x[i]) 
        
    integral = 0
    
    for i in range(n-1):
        
        integral += ((y[i+1]+y[i]) * h[i]) / 2
        
    return integral

    #b) Defining a function that will integrate a loop by splitting the loop into two sides to preform the integration:

def energyDissapated(Dx_T_dV):
    
    #Defining the arrays that will hold the dissapated energies
    energy = []
    
    
    #Iterating over each loop:
    for i in range(np.shape(Dx_T_dV)[2]):
        
        #Defining the arrays that will hold the upper and lower parts of the curves
        x_upper = []
        y_upper = []
        x_lower = []
        y_lower = []
        
        #Populating these:
        for j in range(np.shape(Dx_T_dV)[0]):
               if (Dx_T_dV[j,1,i]>0):
                   x_upper.append(Dx_T_dV[j,0,i])
                   y_upper.append(Dx_T_dV[j,1,i])
               else:
                   x_lower.append(Dx_T_dV[j,0,i])
                   y_lower.append(Dx_T_dV[j,1,i])
        
        #Computing the integrals:
        energy_upper = trapeziumRuleGeneral(x_upper, y_upper)
        energy_lower = trapeziumRuleGeneral(x_lower, y_lower) 
      
     
        
        #Adding the energy of the loop to the energies
        energy.append(energy_upper + energy_lower)
    
    return energy

#____________________________________________________________________________________

#5) Finding the friction coefficient:


    #a) Calculating the friction coefficient for each loop:
def frictionCoefficient(Dx_T_dV, N): #N is the normal force
    
    #Finding the energy dissapated in each loop
    energy = energyDissapated(Dx_T_dV)
    
    #Defining the array that will hold the amplitudes:
    DeltaX = []
    #Defining the array that will hold the friction coefficients:
    nu = []
                              
    #Iterating over each loop to find the amplitudes:
    for i in range(np.shape(Dx_T_dV)[2]):
        
        #Finding the amplitudes
        DeltaX.append( max(Dx_T_dV[:,0,i]) - min(Dx_T_dV[:,0,i]))
    
    
    #Calculatinf the friction coefficient
    for i in range(np.shape(Dx_T_dV)[2]):
        nu_ = energy[i] / (2 * N * DeltaX[i])
        nu.append(nu_)
    
    return nu

    #b) Finding the friction coefficient for each loop

nu_17N = frictionCoefficient(Dx_T_dV_17N, 17)
nu_100N = frictionCoefficient(Dx_T_dV_17N, 100)
nu_150N = frictionCoefficient(Dx_T_dV_17N, 150)


#____________________________________________________________________________________


#6) Finding the tangential contact stiffness

def tangentialContactStiffness(Dx_T_dV):
    
    #Defining the array that will hold the k_t-s:
    kt = []
    
    
    #Iterating over each loop to find the amplitudes:
    for i in range(np.shape(Dx_T_dV)[2]):
        
        
        #Finding the lower left corner (indicies)
        index_lowerleft = list(Dx_T_dV[:,0,i]).index(min(Dx_T_dV[:,0,i]))
    
        
        #Finding the subset of the loop that we are interested in:
        x_kt = []
        y_kt = []
        
        while (Dx_T_dV[index_lowerleft,1,i] < 0):
           
           x_kt.append(Dx_T_dV[index_lowerleft,0,i]*1000)
           y_kt.append(Dx_T_dV[index_lowerleft,1,i])
           
           index_lowerleft += 1
           
       
        slope, intercept, r, p, std_err = stats.linregress(x_kt, y_kt)
        
        kt.append(slope)

    return kt

        #b) Finding the tangential contact stiffness for each loop

kt_17N  = tangentialContactStiffness(Dx_T_dV_17N)
kt_100N = tangentialContactStiffness(Dx_T_dV_100N)
kt_150N = tangentialContactStiffness(Dx_T_dV_150N)


#____________________________________________________________________________________

#7) Finding the cumulative energy disspaited:

    #a) Defining the cummulative energy dissapation for the loops
    
def cummulativeEnergy(Dx_T_dV):
    
    #Finding the energies for each loop:
    energy = energyDissapated(Dx_T_dV)
    
    #Defining the list that will hold the result and an extra help variable
    summaEnergy  = []
    summaEnergy_ = 0

    #Iterating over each loop to find the amplitudes:
    for i in range(np.shape(Dx_T_dV)[2]):
        summaEnergy.append(summaEnergy_)
        summaEnergy_ += energy[i]
        
    return summaEnergy

    #b) Finding the Cummulative Energy for each loop

cummalativeEnergy_17N  = cummulativeEnergy(Dx_T_dV_17N)
cummalativeEnergy_100N = cummulativeEnergy(Dx_T_dV_100N)                            
cummalativeEnergy_150N = cummulativeEnergy(Dx_T_dV_150N)

#____________________________________________________________________________________

#8) Plotting the results:

    #a) 17N case:

#The friction coefficient
pl.scatter(cummalativeEnergy_17N, nu_17N)
pl.title("100 Hz, 17N loading case")
pl.xlabel("Cummulative Energy dissapation [J]")
pl.ylabel("Friction Coefficient [ ]")

pl.show()

#The ftangential contact stiffness
pl.scatter(cummalativeEnergy_17N, kt_17N)
pl.title("100 Hz, 17N loading case")
pl.xlabel("Cummulative Energy dissapation [J]")
pl.ylabel("Tengential friction coefficient [N/\mum ]")

pl.show()

    #b) 100N case:

#The friction coefficient
pl.scatter(cummalativeEnergy_100N, nu_100N)
pl.title("100 Hz, 100N loading case")
pl.xlabel("Cummulative Energy dissapation [J]")
pl.ylabel("Friction Coefficient [ ]")

pl.show()

#The ftangential contact stiffness
pl.scatter(cummalativeEnergy_100N, kt_100N)
pl.title("100 Hz, 100N loading case")
pl.xlabel("Cummulative Energy dissapation [J]")
pl.ylabel("Tengential friction coefficient [N/\mum ]")

pl.show()

    #c) 150N case:

#The friction coefficient
pl.scatter(cummalativeEnergy_100N, nu_100N)
pl.title("100 Hz, 150N loading case")
pl.xlabel("Cummulative Energy dissapation [J]")
pl.ylabel("Friction Coefficient [ ]")

pl.show()

#The ftangential contact stiffness
pl.scatter(cummalativeEnergy_100N, kt_100N)
pl.title("100 Hz, 150N loading case")
pl.xlabel("Cummulative Energy dissapation [J]")
pl.ylabel("Tengential friction coefficient [N/\mum ]")


#____________________________________________________________________________________

#END
