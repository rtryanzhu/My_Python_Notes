# Reorder the dataframe columns with column numbers.
order = [32] + list(range(0,32))
data = trial[trial.columns[order]]

##############################

# Execute a function in APPLY method
"""
    The apply method operates on each row of a dataframe object, therefore when executing a function through apply method, there can be a parameter indicating the row if you don't want to operate on each element by citing a function like np.sqrt. One may just name it as row. If there are other parameter in this function such as the name of specific columns, then it can be delcared when defining the function and the arguments can be passed through args in the apply method.
"""
# When direclty operating on each element.
data = {'A':[1,2,3,4],
        'B':[5,6,7,8]
        }
df = pd.DataFrame(data)
df.apply(np.sqrt)

# When passing arguments to function in apply method.
def get_interval_days(row, start, end):   # the parameter can be named as anything you want
    start_date = dt.datetime.strptime(row[start], '%Y-%m-%d')
    end_date = dt.datetime.strptime(row[end], '%Y-%m-%d') 

    return (end_date - start_date).days
    
wbs = {
    "wbs": ["job1", "job2", "job3", "job4"],
    "date_from": ["2019-04-01", "2019-04-07", "2019-05-16","2019-05-20"],
    "date_to": ["2019-05-01", "2019-05-17", "2019-05-31", "2019-06-11"]
}

df = pd.DataFrame(wbs)
df['elapsed'] = df.apply(
    get_interval_days, axis=1, args=('date_from', 'date_to')) 
    # argument 'date_from' corresponds to parameter start
