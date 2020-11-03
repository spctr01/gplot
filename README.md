 <h1 align="center">Gplot </h1>
<h5 align="center">Python library with graphical interface to plot intractive chart from the google sheet</h5>

 
 ![alt text](https://github.com/spctr01/gploter/blob/main/demo.gif)
 
 -----
 ## Installation   (Tested on Linux)
  Downlaod gploter by pip:
  ```
  pip install gplot
  ```
 ## Usage
 Run the comamnd in terminal:
 ```
 gplot
 ```
 It opens  a frontend in browser automatically if doesnt open automatically type in browser `http://localhost:8501`

 #### Make the google sheet public
  
 - paste the google sheet id and sheet name respectively. (by default both are filled for demo)
 - Press column button. It automatically fetchs columns names from sheet to choose x and y axis
 - Choose  the axis and press plot button
 
 ##### to save ploted chart as image click the camera icon on right top of the chart
 
 ------
 ## Directory structure
 ```
  
|-gapp
|    |
|    |--app.py  :  fronend for the library gets user input & plot chart
|    |
|    |--plot.py  : fetches sheet column and return chart
|    |
|    |location.py  : returns the location of file app.py
|    |
|    |--sessionState.py : handles the session state of streamlt 
|    |
|    |--__init__.py :  __init__ file
|
| 
|-gplot   :  executable file to run the library 
|
|-setup.py  :  package metadata information  (used for pip)
|
|-build     :   build package information   (used for pip)
|
|-dist      :   contains .whl file          (use for pip)
|
|-gplot.egg-info :   compliled bite code   (used for pip)
 ```
 
 
