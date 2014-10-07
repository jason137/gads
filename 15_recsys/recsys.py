#!/usr/bin/env python
import numpy as np
import pandas as pd

# USER_DATA = 'ml-1m/users.dat'
MOVIE_DATA = 'ml-1m/movies.dat'
RATINGS_DATA = 'ml-1m/ratings.dat'

def assign_to_set(df):
    sampled_ids = np.random.choice(df.index,
        size=np.int64(np.ceil(df.index.size * 0.2)),
        replace=False)

    df.ix[sampled_ids, 'for_testing'] = True
    return df

def compute_rmse(y_pred, y_true):
    """ Compute Root Mean Squared Error. """
    return np.sqrt(np.mean(np.power(y_pred - y_true, 2)))

def evaluate(estimate_f):
    """ RMSE-based predictive performance evaluation with pandas. """
    ids_to_estimate = zip(movielens_test.user_id, movielens_test.movie_id)
    estimated = np.array([estimate_f(u,i) for (u,i) in ids_to_estimate])
    real = movielens_test.rating.values
    return compute_rmse(estimated, real)

def estimate1(user_id, item_id):
    """ Simple content-filtering based on mean ratings. """
    return movielens_train.ix[
        movielens_train.user_id == user_id, 'rating'].mean()

def estimate2(user_id, movie_id):
    """ Simple collaborative filter based on mean ratings. """
    ratings_by_others = movielens_train[
        movielens_train.movie_id == movie_id]

    if ratings_by_others.empty: 
        return 3.0

    else:
        return ratings_by_others.rating.mean()

# def main():

# user_cols =dd ['user_id', 'gender', 'age', 'occ', 'zip']
movie_cols = ['movie_id', 'title', 'genres']
user_ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']

# print 'loading users...'
# users = pd.read_csv(USER_DATA, header=None, sep='::', names=user_cols)

print 'loading movies...'
movies = pd.read_csv(MOVIE_DATA, header=None, sep='::', names=movie_cols)

print 'loading users/ratings...'
user_ratings = pd.read_csv(RATINGS_DATA, header=None, sep='::',
    names=user_ratings_cols).drop(['timestamp'], axis=1)

print 'merging data...'
k = pd.merge(user_ratings, movies)

# subsample
N = 10000
k = k.ix[np.random.choice(k.index, size=N, replace=False)]

print 'subsampled dataset: {} users, {} movies'.format(
    k.user_id.nunique(),
    k.movie_id.nunique())


print 'RMSE for estimate1: %s' % evaluate(estimate1)
print 'RMSE for estimate2: %s' % evaluate(estimate2)

movielens['for_testing'] = False
grouped = movielens.groupby('user_id', group_keys=False).apply(assign_to_set)
movielens_train = movielens[grouped.for_testing == False]
movielens_test = movielens[grouped.for_testing == True]
print movielens_train.shape
print movielens_test.shape
print movielens_train.index & movielens_test.index
# if __name__ == '__main__':
#     main()

# example adapted from:
# https://github.com/UnataInc/pycon2013/
