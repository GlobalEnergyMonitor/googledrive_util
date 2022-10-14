# googledrive_util
<!---[![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm)--->
<!---[![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm)--->
<!---[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)--->
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)  
This repository documents a process for accessing and writing docs on the GEM Drive using gspread and googleapiclient.
The module implements interfaces with Google Sheets but the procedures documented here should generalize to other docs. 

GEM contributors: Please add an instruction using pygsheets if you have a working example.  

GEM users with feedback and requests: Please submit your requests through [issues](https://github.com/GlobalEnergyMonitor/googledrive_util/issues).

Last Updated: October 14th 2022

## Getting started
### Client Secret File
See [here](https://developers.google.com/sheets/api/quickstart/python) for setting up Google Developer account and create an OAuth credential.
Following through the "Set up your environment" step should yield you a JSON file on your computer. Step-by-step instruction is given below. 

Step-by-step:
* [Create a developer account](https://developers.google.com/).
* [Create, shut down, and restore projects](https://support.google.com/googleapi/answer/6251787?hl=en#zippy=%2Ccreate-a-project).
* Go to [the API Console Dashboard](https://console.developers.google.com/).
* Select the project you just created: find the pull down menu right of the "Google Cloud" at the top left of the page.
* Go to the three horizontal bars in the top left corner, select APIs & Services > Enable Apis & Services.
* Click on "+ Enable Apis and Services."
* In the APL Library find and enable:
  * Google Sheets API
  * Google Drive API
* Go back to APIs & Services (make sure you aren't under the Drive or Sheet API). You can do this from the three horizontal bars icon.
* Go to Credentials.
  * Create an [OAuth Credentials](https://developers.google.com/workspace/guides/configure-oauth-consent).
    * Click on + CREATE CREDENTIALS > OAuth client ID.
    * Go to OAuth consent screen.
    * Choose Internal for User Type.
    * Then only fill out the app name (same as the project name) and the emails.
    * You can specify th app domain as the GEM domain.
    * No need to add anything to Scopes.
    * Back to Dashboard.
  * If you want to make a Service Account, then [this](https://www.youtube.com/watch?v=4ssigWmExak) is a straightfoward resource.
* Go to Credentials.
  * Click on + CREATE CREDENTIALS > OAuth Client ID.
  * Choose "Desktop App" in the Application Type and give the name.
  * Download the JSON file to your local and move the file to where you store credentials.
  * Make sure you take a note on the local path.
* Additional [third party resource](https://levelup.gitconnected.com/python-pandas-google-spreadsheet-476bd6a77f2b).

### Install Libraries and Packages
Make sure you have the following installed on your environment (conda, colab, jupyter, any IDE such as Pycharm, etc...).    
- [Google Client Library](https://developers.google.com/sheets/api/quickstart/python#install_the_google_client_library). If you use mac and are having trouble installing pip [this](https://gist.github.com/haircut/14705555d58432a5f01f9188006a04ed) maybe helpful.
- [gspread](https://docs.gspread.org/en/latest/)  
- [pandas](https://pandas.pydata.org/)

### Set up a Sample Google Sheets and Find the Sheet ID
- Go to [this](https://drive.google.com/drive/folders/1DaMi_yPWxCERsTxBJB1-tqEX49Zkv_5D) folder on the GEM Drive.
- Open sample_1 and find the sheet ID:
  - look at the url which looks like: https://docs.google.com/spreadsheets/d/14lX1K71k1NZ3KDDt07p0nH95u5SOpLz5gypCkFYVZz4/edit#gid=0
  - the sheet ID is: 14lX1K71k1NZ3KDDt07p0nH95u5SOpLz5gypCkFYVZz4
- If you want to set up your own sample, simply create a spreadsheet on the GEM Drive and find the sheet ID.

### Run google_drive_util module for a use case example
- Open google_drive_util.py in googledrive_util folder.
- Navigate to "TODO for a new user" and fill out client_secret_path, sample_sheet_ID, and sample_sheet_tab info.
- Run google_drive_util.py. This will executes the main function which calls the read_usecase function. 
- If this is your first time running this script, you will be prompted to approve access to the spreadsheet by google (on your web browser and also on your phone).
- Once you approve access, then you should see the contents of the sample_1 file printed on your console.

### Read the documentation on google_drive_util.py
Please read through the docstrings and comments in this file to understand the general use cases of the Google Client Library and Gspread.

# TODO
- Instruction for coda environment and the yml file.
- Read and write use case.
