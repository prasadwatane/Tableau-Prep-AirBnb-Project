#!/usr/bin/env python
# coding: utf-8

# import libraries

import pandas as pd


# Function
def detect_outliers(df):
    return df[df['log_price'] > 10]