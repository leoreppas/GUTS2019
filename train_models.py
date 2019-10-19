from lda_analysis import lda_thresh as lda
import numpy as np
import pickle

# Dataset locations for each category
exes_filename = 'lda_analysis/dataset_exes.csv'
friends_filename = 'lda_analysis/dataset_friends.csv'
parents_filename = 'lda_analysis/dataset_parents.csv'
colleague_filename = 'lda_analysis/dataset_colleague.csv'

# Training models
exes = lda.LDAThresh(exes_filename)
exes_model = exes.threshold_model()

friends = lda.LDAThresh(friends_filename)
friends_model = friends.threshold_model()

parents = lda.LDAThresh(parents_filename)
parents_model = parents.threshold_model()

colleague = lda.LDAThresh(colleague_filename)
colleague_model = colleague.threshold_model()

# Save the models to disk
exes_file = 'exes_model.sav'
friends_file = 'friends_model.sav'
parents_file = 'parents_model.sav'
colleague_file = 'colleague_model.sav'

pickle.dump(exes_model, open(exes_file,'wb'))
pickle.dump(friends_model, open(friends_file,'wb'))
pickle.dump(parents_model, open(parents_file,'wb'))
pickle.dump(colleague_model, open(colleague_file,'wb'))

# Code to load models
#loaded_model = pickle.load(open(filename,'rb'))
#result = 