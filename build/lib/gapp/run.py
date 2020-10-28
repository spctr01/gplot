import os 
import io

path = os.getcwd()

path = 'streamlit run'+' '+path+'/app.py'
os.system(path)