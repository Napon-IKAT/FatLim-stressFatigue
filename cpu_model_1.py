# %%
import torch
import torch.nn as nn
import numpy as np
import os
import time

# %%
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(NeuralNetwork, self).__init__()

        self.normalization = nn.BatchNorm1d(input_size)

        self.fc_layers = nn.Sequential(

            nn.Linear(input_size, 200),
            nn.ReLU(),

            nn.Linear(200, 200),
            nn.ReLU(),

            nn.Linear(200, 200),
            nn.ReLU(),

            nn.Linear(200, 200),
            nn.ReLU(),

            nn.Linear(200, 200),
            nn.ReLU(),

            nn.Linear(200, output_size)
        )
    
    def forward(self, x):

        out = self.normalization(x)
        out = self.fc_layers(out)

        return out

# %%
model = torch.load("exp_model.pth", weights_only=False, map_location=torch.device('cpu')) 
os.system('cls')

# %%
def get_valid_choice():
    while True:
        print("\nChoose input mode:")
        print("     1. With Experimental Data (f0, t-1, t0)")
        print("     2. Without Experimental Data (The accuracy may be diminished!)")
        print("     3. Exit ")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in ('1', '2', '3'):
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))  # Convert input to float
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# %%
base_features = ['s11a', 's22a', 's33a', 't12a', 't13a', 't23a', 
                 's11m', 's22m', 's33m', 't12m', 't13m', 't23m', 
                 'fi11', 'fi22', 'fi33', 'fi12', 'fi13', 'fi23', 'Rm', 'Re',]

material_properties = [ 'f0', 't-1', 't0']
print(
'''
       AI for Multiaxial Stress Fatigue Prediction
--------------------------------------------------------      
 Professorship Machine Elements and Product Development 
        Chemnitz University of Technology, Germany
''')
print("\nLoading... Please wait.")
time.sleep(3)

while True:

    choice = get_valid_choice()


    if choice == '3':
        print("Deactivate model. Goodbye!")
        break

    if choice == '1':
        input_names = base_features + material_properties
        input_values = [get_valid_float(f"{name}: ") for name in input_names]  

    if choice == '2':  
        input_names = base_features
        input_values = [get_valid_float(f"{name}: ") for name in input_names]
        f_1 = 0.45 * input_values[18]
        f0 = (f_1)/(1-(0.00035*input_values[18])-0.1)
        t_1 = float((f_1)*(1/np.sqrt(3)))
        t0 = float((2*t_1)/((f_1/f0)+0.5))
        #input_values.append(f_1)
        input_values.append(f0)
        input_values.append(t_1)
        input_values.append(t0)

    input_tensor = torch.tensor([input_values], dtype=torch.float32)

    for name, value in zip(input_names, input_values):
        print(f"{name}={value},", end=" ")
    
    model.eval()
    with torch.no_grad():
        exp_outputs = model(input_tensor)
        exp_outputs = exp_outputs.to('cpu') 

    exp_pred = float(exp_outputs.detach().numpy().item())
    print('')
    print( "Predicted equivalent stress: ", round(exp_pred,2), "MPa")
        
        


