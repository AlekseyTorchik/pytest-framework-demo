pytest-framework-demo
===============
<img src="https://docs.pytest.org/en/stable/_static/pytest1.png" width="60">

Requirements
------------

For the installation you need:


- Win ![OS](https://icons.iconarchive.com/icons/kearone/comicons/16/windows-symbol-icon.png)
  / Mac ![OS](https://icons.iconarchive.com/icons/tatice/cristal-intense/16/Apple-multicolor-icon.png)
  / Linux ![OS](https://icons.iconarchive.com/icons/tatice/operating-systems/16/Linux-icon.png)
- Python 3.*![](https://icons.iconarchive.com/icons/cornmanthe3rd/plex/16/Other-python-icon.png)
- ChromeDriver - WebDriver for Chrome (latest stable release) ![](https://icons.iconarchive.com/icons/hopstarter/soft-scraps/16/Window-icon.png)
- Microsoft Edge Driver (correct WebDriver version for your build of Microsoft Edge) ![](https://icons.iconarchive.com/icons/hopstarter/sleek-xp-software/16/Command-Prompt-icon.png)
- Git ![](https://icons.iconarchive.com/icons/papirus-team/papirus-apps/16/git-icon.png)



Installation ![](https://icons.iconarchive.com/icons/hopstarter/soft-scraps/24/Button-Download-icon.png)
------------

* First of all make sure your virtual environment is activated. You aslo should install python 3.*, chromdriver, msedgedriver at you environments.

* Go to accessible folder where the project will be located.

* Run command line in that folder and type in the following command:
  
             git clone https://github.com/AlekseyTorchik/pytest-framework-demo.git

* This project uses some dependencies. Just run command line in project folder `pytest-framework-demo` 
  and type in the following command:
             
             pip install -r requirements.txt
            

Run tests ![](https://icons.iconarchive.com/icons/harwen/simple/32/RUN-icon.png)
------------

* Go to folder `pytest-framework-demo`.


* All test runs by command:

            pytest --env qa -s -v

  with report generation:

            pytest --env qa --html="results.html"

* Parallel running tests with parametr -n:
 
            pytest -m chemistry -n8

* Check environment tests for "qa":

            pytest -m envtest --env qa -v

* Check parametrization usage with fixture in case with tv brands:

            pytest -m tv -s

  with build-in mark:   

            pytest -m tvp -s

* Check cross-browser testing for Edge and Chrome: 

            pytest -m browsers

* Testing page navigation in Chrome:

            pytest -m ui

------------