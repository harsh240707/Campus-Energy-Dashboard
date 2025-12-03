# data_processing.py
import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

def load_and_merge_data(data_dir="data"):
    data_path = Path(data_dir)
    all_files = list(data_path.glob("*.csv"))
    df_list = []

    if not all_files:
        logging.warning("No CSV files found in data directory!")

    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')
            # Add metadata if missing
            if 'building' not in df.columns:
                df['building'] = file.stem.split('_')[0]
            if 'month' not in df.columns:
                df['month'] = file.stem.split('_')[-1]
            df_list.append(df)
        except FileNotFoundError:
            logging.error(f"File not found: {file}")
        except Exception as e:
            logging.error(f"Error reading {file}: {e}")

    df_combined = pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()
    return df_combined

def calculate_daily_totals(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    daily = df.groupby(['building', pd.Grouper(key='timestamp', freq='D')])['kwh'].sum().reset_index()
    return daily

def calculate_weekly_aggregates(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    weekly = df.groupby(['building', pd.Grouper(key='timestamp', freq='W')])['kwh'].sum().reset_index()
    return weekly

def building_wise_summary(df):
    summary = df.groupby('building')['kwh'].agg(['sum','mean','min','max']).reset_index()
    summary.rename(columns={'sum':'total_kwh','mean':'avg_kwh','min':'min_kwh','max':'max_kwh'}, inplace=True)
    return summary
