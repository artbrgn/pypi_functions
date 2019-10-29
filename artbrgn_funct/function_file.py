def wrangle(X):
    """Wrangle train, validate, and test sets in the same way"""
        
    # Convert Inspection Date to datetime
    X['date_recorded'] = pd.to_datetime(X['Inspection Date'], infer_datetime_format=True)
    
    # Extract components from date_recorded, then drop the original column
    X['year_recorded'] = X['date_recorded'].dt.year
    X['month_recorded'] = X['date_recorded'].dt.month
    X['day_recorded'] = X['date_recorded'].dt.day
    X = X.drop(columns='Inspection Date')
    X = X.drop(columns='date_recorded')
    
    # return the wrangled dataframe
    return X
