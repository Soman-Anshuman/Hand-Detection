# import mediapipe
# import sys

# print(mediapipe.__version__)

# if sys.prefix != sys.base_prefix:

#     print("You are currently running inside a virtual environment") 

# else:

#     print("You are not in a virtual environment")

import sys

def get_venv_name():
    venv_path = getattr(sys, 'real_prefix', getattr(sys, 'base_prefix', sys.prefix))
    if venv_path != sys.prefix:
        return venv_path.split('/')[-1]  # Extract the last part of the path
    return None

venv_name = get_venv_name()
if venv_name:
    print("Virtual environment name:", venv_name)
else:
    print("Not in a virtual environment")