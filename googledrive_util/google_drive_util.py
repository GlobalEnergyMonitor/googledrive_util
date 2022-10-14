# -*- coding: utf-8 -*-

"""
Implements interfaces with GEM drive.

Functions:
    main(): A use case example.

    read_usecase(): A use case example for reading a Google Sheets into pandas DataFrame.

    credentials(json_token, scopes_, client_secret_path_): Returns credentials.

    credential_readonly(): Returns read-only credential.

    get_gspread_readonly_oauth_credentials(): Returns read-only gspread credentials.

    get_gspread_rw_oauth_credentials(): Returns read-write gspread credentials.

    credentials_gspread_oauth(scopes_, client_secret_path_, json_token_name): Returns the output of gspread.oauth which is a .client.Client class.

    read_googlesheets_from_drive(sheet_id, data_range): Returns google sheets data as pandas DataFrame.

    read_googleseets_from_drive_gspread(sheet_id, tab_name, gspread_creds): Returns google sheets data as pandas DataFrame. This function accomplishes the same thing as read_googlesheets_from_drive function.

    write_dataframe_to_gsheets_gspread(sheet_id, tab_name, data2write, gspread_creds): Writes to google sheets.
"""

# === Packages ===
from __future__ import print_function

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path
import gspread
import pandas as pd

# === SCOPES ===
# A list of scopes are found at: https://developers.google.com/identity/protocols/oauth2/scopes

# Scopes for read-only tasks.
readonly_scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Scopes for read-write tasks.
readwrite_scopes = ['https://www.googleapis.com/auth/spreadsheets']

# === Secrets and Tokens ===
# The files below, readonly_token.json and readwrite_token.json, store the
# user's access and refresh tokens, are created automatically when the
# authorization flow completes for the first time. In other words, you do not
# have to have these tokens before you use any of the functions beforehand. Note
# that one token per 'scopes' you define above will be generated. So if changing
# the 'scopes' delete the existing token for a given scope or create another
# token name for that new 'scopes'.
readonly_json_token = 'readonly_token.json'  # You can change the name to whatever is suitable.
readwrite_json_token = 'readwrite_token.json'  # You can change the name to whatever is suitable.

# TODO for a new user: Change this path to where you have your client secret.
client_secret_path = '/your/local/path/to/client_secret.json'  # TODO: Put your path.
sample_sheet_ID = 'Sheet ID'  # TODO: Put the address to your sseet ID.
sample_sheet_tab = 'Tab name'  # TODO: Enter the correct tab name.


def main():

    read_usecase()


def read_usecase():
    """A use case example for reading a Google Sheets into pandas DataFrame."""
    # Establish read-only credentials.
    # Note that read-write credentials alone would be sufficient, but using
    # read-only credential puts extra protection for data being read (e.g.,
    # tracker data).
    readonly_cred_result, readonly_gc = credentials_gspread_oauth(scopes_=readonly_scopes,
                                                                  client_secret_path_=client_secret_path,
                                                                  json_token_name=readonly_json_token
                                                                  )
    if readonly_cred_result:
        # Open the Google Sheets at data2write_sheet_id and tab_name as a DataFrame.
        read_result, sample_data = read_googleseets_from_drive_gspread(sheet_id=sample_sheet_ID,
                                                                       tab_name=sample_sheet_tab,
                                                                       gspread_creds=readonly_gc
                                                                       )
        if read_result:
            print('Sample data loaded to DataFame!')
            print(sample_data.head())

        else:
            print('Loading sample data failed!!')
            print(sample_data)

    else:
        print('Read credential not established!')
        print(readonly_gc)


def write_dataframe_to_gsheets_gspread(sheet_id, tab_name, data2write, gspread_creds):
    """
    Writes to google sheets.

    Code below is adapted and modified from:

    Args:
        sheet_id (str): Google Sheet ID.
        tab_name (str): A desired tab name of Google Sheets at sheet_id.
        data2write (pandas.DataFrame): Data to be written at sheet_id.
        gspread_creds:

    Returns:
        Boolean, value:
            True, 'success'
            False, error
    """

    try:
        # Open the Google Sheets to write to.
        gsheets = gspread_creds.open_by_key(key=sheet_id)
        spreadsheet = gsheets.worksheet(title=tab_name)  # Access a specific sheet (tab).

        # Write to the spreadsheet.
        write_result = spreadsheet.update([data2write.columns.values.tolist()] + data2write.values.tolist())

        return True, write_result

    except Exception as err:
        return False, err


def read_googleseets_from_drive_gspread(sheet_id, tab_name, gspread_creds):
    """Returns google sheets data as pandas DataFrame.

    Output of this function is the same as that of read_googlesheets_from_drive
    function.

    Args:
        sheet_id (str): Google Sheet ID.
        tab_name (str): A tab bane of the sheet at sheet_id.
        gspread_creds : Output of the credentials_gspread_oauth function.

    Returns:
        Bool, value:
            True, DataFrame containing the data at tab_name of the sheet at sheet_id.
            False, error message.
    """

    try:
        # Open a Google Sheets.
        gsheets = gspread_creds.open_by_key(key=sheet_id)
        spreadsheet = gsheets.worksheet(title=tab_name)  # Access a specific tab.
        data_frame = pd.DataFrame(spreadsheet.get_all_records(expected_headers=[]))  # expected_header option provided following: https://github.com/burnash/gspread/issues/1007

        return True, data_frame

    except Exception as err:
        return False, err


def read_googlesheets_from_drive(sheet_id, data_range, credential_):
    """
    Returns google sheets data as pandas DataFrame.

    Output of this function is the same as that of
    read_googleseets_from_drive_gspread function.

    Code below is adapted from:
    https://developers.google.com/sheets/api/quickstart/python and
    https://levelup.gitconnected.com/python-pandas-google-spreadsheet-476bd6a77f2b.

    Args:
        sheet_id (str): Google Sheet ID.
        data_range (str): Data range to read from the sheet.
        credential_ : Output of the credentials function.

    Returns:
        Bool, value:
            True, DataFrame
            False, error
    """

    # Read from Google Drive.
    try:
        service = build('sheets', 'v4', credentials=credential_)

        # Call the Sheets API.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=data_range).execute()
        values = result.get('values', [])

        if not values:
            message = f'No data found at: {sheet_id}, data range: {data_range}.'
            return False, message

        else:
            data_frame = pd.DataFrame(values)
            data_frame.columns = data_frame.iloc[0]
            data_frame.drop(data_frame.index[0], inplace=True)
            data_frame.dropna(how='all')  # If all values are NA, drop that row or column.
            if data_frame.empty:
                message = f'Empty data at: {sheet_id}, {data_range}'
                return False, message
            else:
                return True, data_frame

    except HttpError as err:
        message = f'HttpError occurred! Check sheet_id and data_range.\n' \
                  f'sheet_id: {sheet_id} \n' \
                  f'data_range: {data_range} \n' \
                  f'{err}'
        return False, message
    except Exception as err:  # Intentionally catch all other errors.
        message = f'An unknown error occurred! \n' \
                  f'{err}'
        return False, message


def get_gspread_readonly_oauth_credentials():
    """Returns read-only gspread credentials."""
    return credentials_gspread_oauth(scopes_=readonly_scopes, client_secret_path_=client_secret_path, json_token_name=readonly_json_token)


def get_gspread_rw_oauth_credentials():
    """Returns read-write gspread credentials."""
    return credentials_gspread_oauth(scopes_=readwrite_scopes, client_secret_path_=client_secret_path, json_token_name=readwrite_json_token)


def credentials_gspread_oauth(scopes_, client_secret_path_, json_token_name):
    """Returns the output of gspread.oauth which is a .client.Client class.

    Args:
        scopes_ (list): A list containing a scope. A list of scopes can be found at: https://developers.google.com/identity/protocols/oauth2/scopes
        client_secret_path_ (str): Absolute path to your client secret (.json).
        json_token_name (str): The name of the json token (*.json, e.g., token.json).

    Returns:
        Bool, value:
            True, .client.Client class.
            False, error message
    """
    try:
        # Authenticate credentials.
        gc = gspread.oauth(scopes=scopes_,
                           credentials_filename=client_secret_path_,
                           authorized_user_filename=json_token_name
                           )
        return True, gc

    except Exception as err:
        return False, err


def credential_readonly():
    """Returns read-only credential."""
    return credentials(json_token=readonly_json_token, scopes_=readonly_scopes, client_secret_path_=client_secret_path)


def credentials(json_token, scopes_, client_secret_path_):
    """
    Returns credentials.

    Code below is adapted from:
    https://developers.google.com/sheets/api/quickstart/python

    Args:
        json_token (str): The name of the json token (*.json, e.g., token.json).
        scopes_ (list): A list containing a scope. A list of scopes can be found at: https://developers.google.com/identity/protocols/oauth2/scopes
        client_secret_path_ (str): Absolute path to your client secret (.json).

    Returns:
        Bool, value:
            True, credentials
            False, error
    """

    creds = None
    try:
        if os.path.exists(json_token):
            creds = Credentials.from_authorized_user_file(json_token, scopes_)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret_path_, scopes_)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run.
            with open(json_token, 'w') as token:
                token.write(creds.to_json())

        return True, creds

    # Catch any errors. This is on purpose.
    except Exception as error:
        message = f'An error occurred during authentication for readonly drive access. \n' \
                  f'Check your client secret and the path and see the error below: \n' \
                  f'{error}'
        return False, message


if __name__ == '__main__':
    main()
