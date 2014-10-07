#!/usr/bin/env python
import numpy as np
import pandas as pd

USERS_FILE = 'ml-1m/users.dat'
RATINGS_FILE = 'ml-1m/ratings.dat'
MOVIES_FILE = 'ml-1m/movies.dat'

SEP = '::'

def get_data():

    print 'loading users...'
    unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
    users = pd.read_table(USERS_FILE, sep=SEP, header=None,
        names=unames)

    print 'loading ratings...'
    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table(RATINGS_FILE, sep=SEP, header=None,
        names=rnames)

    print 'loading movies...'
    mnames = ['movie_id', 'title', 'genres']
    movies = pd.read_table(MOVIES_FILE, sep=SEP, header=None,
        names=mnames)

    print 'merging...'
    data = pd.merge(pd.merge(ratings, users), movies)

    # subsample (for quicker runtime)
    data = data.ix[np.random.choice(data.index, size=10000, replace=False)]

    # filter
    # user_ids_larger_1 = pd.value_counts(movielens.user_id, sort=False) > 1
    # movielens = movielens[user_ids_larger_1[movielens.user_id]]
    # print movielens.shape
    # np.all(movielens.user_id.value_counts() > 1)

    return data

def assign_to_set(df, test_pct=0.2):
    """Make train/test assignments."""

    sampled_ids = np.random.choice(
        df.index,
        size=np.int64(np.ceil(df.index.size * test_pct)),
        replace=False)

    df.ix[sampled_ids, 'for_testing'] = True
    return df

def compute_rmse(y_pred, y_true):
    """Compute Root Mean Squared Error."""
    return np.sqrt(np.mean(np.power(y_pred - y_true, 2)))

def evaluate(estimate_f):
    """RMSE-based predictive performance evaluation with pandas."""
    ids_to_estimate = zip(movielens_test.user_id, movielens_test.movie_id)
    estimated = np.array([estimate_f(u,i) for (u,i) in ids_to_estimate])
    real = movielens_test.rating.values
    return compute_rmse(estimated, real)

def estimate1(user_id, item_id):
    """Simple content-filtering based on mean ratings."""
    return movielens_train.ix[
        movielens_train.user_id == user_id, 'rating'].mean()

def estimate2(user_id, movie_id, default_rating=3.0):
    """Simple collaborative filter based on mean ratings."""
    ratings_by_others = movielens_train[movielens_train.movie_id == movie_id]

    if ratings_by_others.empty:
        return default_rating

    else:
        return ratings_by_others.rating.mean()

def main():

    movielens = get_data()

    # split grouped (by user_id) df into train/test sets
    movielens['for_testing'] = False
    grouped = movielens.groupby('user_id', group_keys=False).apply(assign_to_set)
    movielens_train = movielens[grouped.for_testing == False]
    movielens_test = movielens[grouped.for_testing == True]

    print 'train set size: {}'.format(movielens_train.shape)
    print 'test set size: {}'.format(movielens_test.shape)

    print 'RMSE for estimate1: %s' % evaluate(estimate1)
    print 'RMSE for estimate2: %s' % evaluate(estimate2)

if __name__ == '__main__':
    main()
