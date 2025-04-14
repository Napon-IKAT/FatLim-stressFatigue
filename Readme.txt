Napon Opasanon, Leon Josef Stahr, Lukas Suchy and Alexander Hasse.
Professorship of Machine Elements and Product Development, Technische Universität Chemnitz, Germany.


The augmented dataset was created based on the Fatlim dataset (Papuga et al., 2022).
The original dataset is available at the following link: https://www.pragtic.com/fatlim.php
The corresponding publication can be found here: https://doi.org/10.3390/met12020289




Before running the program, ensure you have the following:

Python installed, reccommend Python 3.10.x.
PyTorch and NumPy libraries installed. You can install them using the following commands in terminal or command prompt.
"pip install torch numpy"

A pre-trained model exp_model.pth (this file should be located in the same directory as the Python script).

Running the Program

Download the Python script (cpu_model_1.py) and ensure the pre-trained model file (exp_model.pth) is in the same directory as the script.
Run the Python Script:

Open a terminal or command prompt and navigate to the directory where the files are stored.
Run the script by typing:

"python cpu_model_1.py"


Input Features:
Depending on your choice, you will be prompted to enter a set of material properties. For example:
Choice 1: You will need to enter all features (e.g. stress tensor, Rm, Re) and the experimental data (e.g. f0, t-1, t0).
Choice 2: You will need to enter only the base features (e.g. stress tensor, Rm, Re). The program will estimate f0, t-1, and t0. 
