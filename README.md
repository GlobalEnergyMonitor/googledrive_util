# googledrive_util
<!---[![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm)--->
<!---[![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm)--->
<!---[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)--->
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)  
This repository documents a process for accessing and writing docs on the GEM Drive using gspread and googleapiclient.
The module implements interfaces with Google Sheets but the general procedure should generalize to other docs. 

To GEM contributors: Please add an instruction using pygsheets if you have a working example.  

Last Updated: October 13th 2022

## Getting started
### Client Secret File
See [here](https://developers.google.com/sheets/api/quickstart/python) for setting up Google Developer account and create an OAuth credential.
Following through the "Set up your environment" step should yield you a JSON file on your computer.  
TODO: Add step-by-step

### Install Google Client Library and gspread package
Make sure you have the following installed on your environment (conda, any IDE such as Pycharm, jupyter, etc...).    
- [Google Client Library](https://developers.google.com/sheets/api/quickstart/python#install_the_google_client_library). If you use mac and are having trouble installing pip [this](https://gist.github.com/haircut/14705555d58432a5f01f9188006a04ed) maybe helpful.
- [gspread](https://docs.gspread.org/en/latest/)   

### Set up a Sample Google Sheets and Find the Sheet ID

### Run test()

## Tests
TODO: Make a sample. 
<!---
Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Give an example
```
--->
