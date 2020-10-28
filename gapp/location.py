import os 
import io

path = os.path.realpath(__file__)

path = path[:-11]
path = 'streamlit run'+' '+path+'app.py'
os.system(path) 