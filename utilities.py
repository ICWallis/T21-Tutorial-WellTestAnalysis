#
# Functions for T21 tutoral
# mostly specific methods made simplify the notebooks
#

import pandas as pd
from datetime import datetime
from dateutil import tz
import openpyxl
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

#
# Datetime tools
# 

def to_nztime(t):
    '''
    Convert datetime from UTC to NZ time zone +13 hrs
    
    Method from D.Dempsey
    https://github.com/ddempsey/whakaari

    args: ISO formatted datetime in UTC time

    returns: ISO formatted datetime in NZ time
    '''
    utctz = tz.gettz('UTC')
    nztz = tz.gettz('Pacific/Auckland')
    return [ti.replace(tzinfo=utctz).astimezone(nztz) for ti in pd.to_datetime(t)]

# https://docs.python.org/3/library/datetime.html?highlight=re#datetime.datetime.timestamp

def datetime_to_timestamp(dataframe_col):
    '''
    Make POSIX timestamp from Python datetime object

    args: dataframe column containing datetime objects

    returns: list of POSIX timestamp floats 
    '''
    list = []
    for date in dataframe_col:
        timestamp = datetime.timestamp(date)
        list.append(timestamp)
    return list


def timestamp_to_datetime(dataframe_col):
    '''
    Make Python datetime object from POSIX timestamp

    args: dataframe column containing POSIX timestamps

    returns: list of datetime objects 
    '''
    list = []
    for date in dataframe_col:
        newdate = datetime.fromtimestamp(date)
        list.append(newdate)
    return list

#
# Bespoke functions designed to import and mudge sample data
#

def read_flowrate(filename):
    ''' 
    Read PTS-2-injection-rate.xlsx in as a pandas dataframe and munge for analysis

    args: filename is r'PTS-2-injection-rate.xlsx'

    returns: pandas dataframe with local NZ datetime and flowrate in t/hr
    '''
    df = pd.read_excel(filename, header=1) 
    df.columns = ['raw_datetime','flow_Lpm']

    list = []
    for date in df['raw_datetime']:
        newdate = datetime.fromisoformat(date)
        list.append(newdate)
    df['ISO_datetime'] = list 

    list = []
    for date in df.ISO_datetime:
        newdate = pd.to_datetime(datetime.strftime(date,'%Y-%m-%d %H:%M:%S'))
        list.append(newdate)
    df['datetime'] = list

    df['flow_tph'] = df.flow_Lpm * 0.060

    df['timestamp'] = datetime_to_timestamp(df.datetime)

    df.drop(columns = ['raw_datetime', 'flow_Lpm', 'ISO_datetime'], inplace = True)

    return df

def read_pts(filename):
    '''
    Read PTS-2.xlsx in as a Pandas dataframe and munge for analysis

    args: filename is r'PTS-2.xlsx'

    returns: Pandas dataframe with datetime (local) and key coloumns of PTS data with the correct dtype
    '''
    df = pd.read_excel(filename)

    dict = {
        'DEPTH':'depth_m',
        'SPEED': 'speed_mps',
        'Cable Weight': 'cweight_kg',
        'WHP': 'whp_barg',
        'Temperature': 'temp_degC',
        'Pressure': 'pressure_bara',
        'Frequency': 'frequency_hz'
    }
    df.rename(columns=dict, inplace=True)

    df.drop(0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    list = []
    for date in df.Timestamp:
        newdate = openpyxl.utils.datetime.from_excel(date)
        list.append(newdate)
    df['datetime'] = list

    df.drop(columns = ['Date', 'Time', 'Timestamp','Reed 0',
       'Reed 1', 'Reed 2', 'Reed 3', 'Battery Voltage', 
       'PRT Ref Voltage','SGS Voltage', 'Internal Temp 1', 
       'Internal Temp 2', 'Internal Temp 3','Cal Temp', 
       'Error Code 1', 'Error Code 2', 'Error Code 3',
       'Records Saved', 'Bad Pages',], inplace = True)
    
    df[
        ['depth_m', 'speed_mps','cweight_kg','whp_barg','temp_degC','pressure_bara','frequency_hz']
    ] = df[
        ['depth_m','speed_mps','cweight_kg','whp_barg','temp_degC','pressure_bara','frequency_hz']
        ].apply(pd.to_numeric)
    
    df['timestamp'] = datetime_to_timestamp(df.datetime)

    return df

#
# Generate standard overview plot
#

def overview_fig(pts_df,flowrate_df,title=''):
    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1,figsize=(10,15),sharex=True)
    ax1.set_title(title,y=1.1,fontsize=15)

    ax1.plot(flowrate_df.datetime, flowrate_df.flow_tph, label='Surface pump flowrate', 
        c='k', linewidth=0.8, marker='.')
    ax1.set_ylabel('Surface flowrate [t/hr]')
    ax1.set_ylim(0,150)
    
    ax2.plot(pts_df.datetime, pts_df.depth_m, label='PTS tool depth', 
        c='k', linewidth=0.8)
    ax2.set_ylabel('PTS tool depth [m]')
    ax2.set_ylim(1000,0)
    
    ax3.plot(pts_df.datetime, pts_df.pressure_bara, label='PTS pressure', 
        c='tab:blue', linewidth=0.8)
    ax3.set_ylabel('PTS pressure [bara]')
    
    ax4.plot(pts_df.datetime, pts_df.temp_degC, label='PTS temperature', 
        c='tab:red', linewidth=0.8)
    ax4.set_ylabel('PTS temperature')
    
    ax5.plot(pts_df.datetime, pts_df.frequency_hz, label='PTS impeller frequency', 
        c='tab:green', linewidth=0.8)
    ax5.set_ylim(-30,30)
    ax5.set_ylabel('PTS impeller frequency [hz]')
    # 1 hz = 60 rpm

    ax6.plot(pts_df.datetime, pts_df.speed_mps, label='PTS tool speed', 
        c='tab:orange', linewidth=0.8)
    ax6.set_ylim(-2,2)
    ax6.set_ylabel('PTS tool speed [mps]')
    
    ax6.set_xlabel('Time [hh:mm]')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    
    for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
        ax.grid()
    
    return plt

    
