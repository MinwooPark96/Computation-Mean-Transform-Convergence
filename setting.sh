ENV_NAME=meantransform

conda create -n ${ENV_NAME} python=3.8
conda activate ${ENV_NAME}

pip install -r requirements.txt
