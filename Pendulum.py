import pendulum 
from icecream import ic

# https://pendulum.eustace.io/docs/

#dt_toronto = pendulum.datetime(2024, 1, 1 , tz= 'America/Toronto')

#dt_vancouver = pendulum.datetime(2024, 1, 1, tz='America/Vancouver')

#ic(dt_toronto.diff(dt_vancouver).in_hours())

dt = pendulum.datetime(2024, 2, 22)

ic(dt.format('ddd DD MMM YYYY',) )



