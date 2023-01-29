import pandas as pd
import subprocess
import os
from datetime import date, timedelta
import config

def runcmd(cmd, verbose = False, *args, **kwargs):

        process = subprocess.Popen(
            cmd,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True,
            shell = True
        )
        std_out, std_err = process.communicate()
        if verbose:
            print(std_out.strip(), std_err)
        pass

def get_data():
    # Change cwd
    current_path = os.chdir('personal_fitness_tracker/health_data/')
    # Get date of data
    today = date.today() - timedelta(days=1)

    # Ingest data
    for i in config.sheet_links.keys():
        # Download data
        runcmd(f'wget "https://docs.google.com/spreadsheets/d/{config.sheet_links[i]}/export?format=csv" -O "{i}.csv"')
        
        # Format downloaded data
        df = pd.read_csv(f'{i}.csv',header = None)
        df.rename(columns = {0:'timestamp',1:i},inplace = True)
        df.timestamp = pd.to_datetime(df.timestamp)
        df.to_csv(f'{i}.csv',header = False, index = None)
        
    os.chdir('../')