import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = " textSummarizer"

list_of_files = [
  ".github/workflow/.gitkeep",
  f"src/{project_name}/_init_.py",
  f"src/{project_name}/component/_init_.py",
  f"src/{project_name}/utils/_init_.py",
  f"src/{project_name}/utils/common.py",
  f"src/{project_name}/logging/_init_.py",
  f"src/{project_name}/config/_init_.py",
  f"src/{project_name}/config/configuration/_init_.py",
  f"src/{project_name}/pipeline/_init_.py",
  f"src/{project_name}/entity/_init_.py",
  f"src/{project_name}/constant/_init_.py",
  "config/config.yaml",
  "params.yaml",
  "app.py",
  "main.py",
  "DockerFile",
  "requirements.txt",
  "setup.py",
  "research/trials.ipynb",




]
for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)

  if filedir != "":
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Creating directory: {filedir} for the file {filename}")


  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) :
    
    with open(filepath, 'w') as f:
      pass
      logging.info(f"Created empty file: {filepath}")



  else:
    logging.info(f"File {filepath} already exists.")