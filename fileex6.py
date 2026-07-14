# program picking and unpicking
import pickle
l = [10, 20, 30, 40, 50, 60, 70]
with open("abc.pkl","wb+") as f:
    pickle.dump(l,f)
  