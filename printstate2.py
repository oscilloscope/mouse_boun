
import numpy as np
def printstatement3():
    print("This is the third print statement")

### Apply PCA to these data that has x, y and timestamp columns and return the first 2 components
def generate_features(mouse_raw):
    
    import numpy as np
    x = mouse_raw['x'].copy()
    y = mouse_raw['y'].copy()
    horiz_spd = mouse_raw['x'].diff()/mouse_raw['timestamp'].diff()
    vert_spd = mouse_raw['y'].diff()/mouse_raw['timestamp'].diff()
    tang_spd = np.sqrt((horiz_spd**2)+(vert_spd**2))

    horiz_acc = horiz_spd.diff()/mouse_raw['timestamp'].diff()
    vert_acc = vert_spd.diff()/mouse_raw['timestamp'].diff()
    tang_acc = np.sqrt((horiz_acc**2)+(vert_acc**2))
    
    # Calculate the speed and acceleration of the mouse movement
    dx = np.diff(x)
    dy = np.diff(y)
    speed = np.sqrt(dx ** 2 + dy ** 2)
    acceleration = np.diff(speed)
    #acceleration = np.nan_to_num(acceleration)
    # Calculate the jerk of the mouse movement
    jerk = np.diff(acceleration)
    #jerk = np.mean(jerk)
    

    return { 'horiz_spd': horiz_spd, 'vert_spd': vert_spd, 'tang_spd':tang_spd, 
            'horiz_acc': horiz_acc, 'vert_acc': vert_acc,  
            'tang_acc': tang_acc, 'mouse_rawx_diff': mouse_raw['x'].diff(), 'mouse_rawx_timestamp': mouse_raw['timestamp'].diff(),
           'jerk': jerk }

def ranges(x):
    #print(x.max() - x.min())
    return x.max() - x.min()
def rmssd(x):
    
    return np.sqrt(np.mean(np.diff(x) ** 2))
def sdsd(x):
    return st.stdev(np.diff(x))
def nni_50(x):
    return  sum(np.abs(np.diff(x)) > 50)

def pnni_50(x):
    return 100 * nni_50(x) / len(x)

def nni_20(x):
    return sum(np.abs(np.diff(x)) > 20)

def pnni_20(x):
    return  100 * nni_20(x) / len(x)

def nni_5(x):
    return sum(np.abs(np.diff(x)) > 5)

def avg_hr(x):
    return  st.mean(100/x)

def avg_hr(x):
    return  st.mean(60000/x)
def std_hr(x):
    return  st.stdev(60000/x)
def min_hr(x):
    return  min(60000/x)
def max_hr(x):
    return  max(60000/x)

def energy(x):
    return sum(np.square(x))
def abs_sum_diff(x):
    
    return sum(np.abs(np.diff(x)))


def printstatement2():
    print("This is the second print statementxxx22x3321111q")
    print("asdasdasdasd")
    print("This is the second print statementxxx22x3321111qq")