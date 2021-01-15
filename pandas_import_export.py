import pandas
import numpy as np

# Import data
data = pandas.read_csv(r'D:\file_path\file.csv')
data.head()

# Separate columns into column vectors
Iout = data['Iout (mA)'].values
Vout = data['Vout (V)'].values
Pout = data['Pout (mW)'].values

# View shape and first few values of data vectors
print('Iout:', Iout.shape)
print(Iout[0:3])
print('Vout:', Vout.shape)
print(Vout[0:3])
print('Pout:', Pout.shape)
print(Pout[0:3])

# Combine data into one matrix for export
m = len(Iout)
X = np.block([Iout.reshape(m, 1), Vout.reshape(m, 1), Pout.reshape(m, 1)])

# Verify X is correct
print('X shape:', X.shape)
print(X[0, :])

# Export data
datax = pandas.DataFrame(X, columns=['Iout (mA)', 'Vout (V)', 'Pout (mW)'])
datax.to_csv(r'D:\file_path\filex.csv', index = False)
