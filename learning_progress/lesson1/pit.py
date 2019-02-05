import matplotlib.pyplot as pit
import numpy as np


# pit.plot([1,3,5],[4,8,10])
# pit.show()

pit.figure(1,dpi=50)
data = [1,1,1,2,2,2,3,3]
pit.hist(data)
pit.show()