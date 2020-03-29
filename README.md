# och-watchdog
Python app that sends out notifications every time a new property is added to University of Maryland's Off Campus Housing (OCH) database that meets defined criteria.

This app was created, tested, and used in Spring of 2020. If/when OCH updates their website there is no gaurantee the app will continue to work.

## Installation/setup

Step 1, as always, is to clone the repo to your machine.

run
```shell
git clone https://github.com/mwcodebase/och-watchdog.git
```
wherever you would like to store the repo.

The main requirement for running this app is to have selenium setup. If you do not already have selenium setup for Python, the documentation can be found here: https://selenium-python.readthedocs.io/

This app's selenium setup utilizes Mozilla Firefox. 

Beyond selenium, this app requires several pip packages. To install them, simply run
```shell
pip3 install -r app/requirement.txt
```
from the repo's base directory.

Now that all the requirements have been seutp, if you want this app to send emails, follow the directions in the next section. If you only wish to print results to stdout, there is nothing left to do.

run
```shell
python3 app/app.py --test
```
from the repo's base directory.

## Sending emails

To send emails you will need to create a `credentials.env` file in the `/app/env_files/` directory. The app is expecting `credentials.env` to contain this information, verbatim.

```text
recipient's email address
sender's email address
sender's emai password
```

Notice, the .gitignore file contains one line: `*.env`. While this is not the most elegant solution to avoiding plaintext password leaks, it suffices for a simple app such as this. That being said, in an abundance of caution, please do not use your main GMail account to send emails with this app.

The app is ready to go, run
```shell
python3 app/app.py
```
from the repo's base directory.
