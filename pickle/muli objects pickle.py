import pickle
with open('model_due.pickle', 'wb') as handle:
    pickle.dump([classifier,vectorizer], handle, protocol=pickle.HIGHEST_PROTOCOL)

