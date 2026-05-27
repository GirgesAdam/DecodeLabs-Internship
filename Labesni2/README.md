# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# Install the required dependencies within the virtual environment
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

# Redirect Output and Error to a File (CMD)
```cmd
python model_least.py > output_and_logs_2.txt 2>&1
`
# Uninstall All Existing Packages

   You can use `pip freeze` to list all installed packages and then uninstall them. Here's a step-by-step approach:

   ```sh
   pip freeze > all_packages.txt
   ```

   This command saves the list of installed packages to a file named `all_packages.txt`.

   Next, uninstall all packages listed in `all_packages.txt`:

   ```sh
   pip uninstall -r all_packages.txt -y
   ```

   This will uninstall all packages listed in the file.

# open explorer in ubuntu
explorer.exe .

#open the working directory
cd /mnt/d/My\ Projects/Labbasni/ML_AI

# open docker of the tensorflow GPU with the working directory
docker run --gpus all -it -v "$(pwd | tr '[:upper:]' '[:lower:]'):/working" -w /working tensorflow/tensorflow:latest-gpu bash

# Install the required dependencies within the virtual environment
pip install -r requirements_gpu.txt

# Redirect Output and Error to a File (CMD)
```cmd

python model_gpu.py > output_and_logs_gpu.txt 2>&1
`
# install tensorflow in docker
https://www.tensorflow.org/install/docker