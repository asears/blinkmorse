# blinkmorse

Face and eye detection with OpenCV and Python

Thanks to [Brandon Jackson](https://github.com/brandonjackson/nap-alert) for xml definitions 

# Resources for Blink Detection

[Blinking Matters](https://www.blinkingmatters.com/features)  
[Andre Venancio](http://andrevenancio.com/eye-blink-detection/)  
[ClmTracker](https://github.com/auduno/clmtrackr)  

# Python Libraries

[Pygaze](https://www.pygaze.org/installation/)
[PsychoPy](https://github.com/lupyanlab/lab-computer/wiki/Install-psychopy-on-Anaconda-python)
[Pyo](http://ajaxsoundstudio.com/software/pyo/)

## Extending the solution

http://compromise.cool/  

## Pygaze with Anaconda Python
### Setup Hints for Windows

#### New Environment - Anaconda 3.5
```
conda create -n shooting python=3.5
activate shooting
```
Rename environment
conda create --name blinkmorse --cloneshooting
conda remove --name shooting --all # or its alias: `conda env remove --name old_name`

```
conda install python=3.5
conda install -c menpo opencv3
REM Numpy will be downgraded in Anaconda
conda install numpy scipy matplotlib pandas pyopengl 
REM Phoenix Version for Python 3.5
pip install wxpython 
conda install lxml openpyxl xlrd configobj pyyaml gevent pillow 
conda install greenlet msgpack-python psutil pytables requests seaborn future
conda install --channel conda-forge pyglet
pip install moviepy pyosf python-bidi psychopy_ext psychopy json_tricks
conda install --channel cogsci pygame
```

## Installing Pyo
*32-bit only, Does not work on 64-bit, requires compilation* 
```
conda config –add channels https://conda.binstar.org/erik
```
Install to ProgramData\Anaconda3 folder.

## Visual Studio Code Debugging

1. Select Anaconda Interpreter
2. To use a Python interpreter that's installed in a virtual environment:
Edit the python.pythonPath setting to point to the virtual environment. For example:

Windows:
```
{
    "python.pythonPath": "c:/dev/ala/venv/Scripts/python.exe"
}
```

## Visual Studio Code Unit Tests

[Configuring Tests](https://code.visualstudio.com/docs/python/unit-testing)

Enable one of these
```
  "python.unitTest.unittestEnabled": false,
    "python.unitTest.pyTestEnabled": true,
    "python.unitTest.nosetestsEnabled": false,
```

# Distributing a Package

[Python Lessons Learned. Read This Before You Start Building a Distributable Python Package](https://blog.jongallant.com/2018/01/python-lessons-learned/)
