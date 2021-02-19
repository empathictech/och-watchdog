# OCH Watchdog

Python app that sends out notifications every time a new property is added to University of Maryland's Off Campus Housing (OCH) database that meets defined criteria.

This app was created, tested, and used in Spring of 2020. If/when OCH updates their website there is no gaurantee the app will continue to work.

## Getting started

The first step, as always, is to clone the repo to your machine. Run
```shell
git clone https://github.com/mwcodebase/och-watchdog.git
```

As mentioned, this app is built with Python, so make sure you have Python3 (any sub-version) installed on your machine: https://www.python.org/

### Dependencies/Prerequisites

This app has several Python dependencies. Run 
```shell
pip3 install -r requirements.txt
```
in the `/app` directory to install them all.

#### Selenium/geckodriver

This app uses Selenium, and is specifically built to use Firefox as its web browser. After installing the Selenium pip package (above) you will need to install geckodriver. Download the latest release here: https://github.com/mozilla/geckodriver/releases At the time of writing, geckodriver has versions for Linux, MacOS, and Windows. Linked below are docs for Selenium and geckodriver if you would like to learn more.

https://selenium-python.readthedocs.io/
https://github.com/mozilla/geckodriver

## Using the OCH Watchdog

If you want to use the default search criteria, you are good to go! Simply run
```shell
python3 app.py
```
if you are in the repo's `/app` directory, otherwise provide the full path to `app.py` from wherever you are.

If you would like to customize the search criteria, make your choices manually at https://ochdatabase.umd.edu/ and copy the URL that is generated to line 64 of `app.py`. Currently, the app only works with pre-generated URLs, it does not allow for customization from the command line (but feel free to add that functionality yourself and make PR for it!).

### Sending emails

The app's default functionality is to print results to stdout. If you would like to send emails you will need to create a `credentials.env` file in the `app` directory. `credentials.env` should contain this information, verbatim.

```text
recipient_email_address
sender_email_address
sender_email_password
```

The sender's email will need to allow less secure access to the account. An explanation on how to set this up can be found here: https://support.google.com/accounts/answer/6010255?hl=en

Notice, the .gitignore file contains `*.env`. While this is not the most elegant solution to avoiding plaintext password leaks, it suffices for a simple app such as this. That being said, in an abundance of caution, please do not use your main GMail account to send emails with this app. Using a seperate account is also receommended due to the requirement of less secure access to the account.

## FAQ

If you have any questions or issues, you might find a solution in the [FAQ](FAQ.md)

## Contributing

If you would like to contribute to {PROJECT_NAME}, please see how in [CONTRIBUTING](CONTRIBUTING.md)

## License

This project is licensed under the terms of the [MIT license](LICENSE.txt).
