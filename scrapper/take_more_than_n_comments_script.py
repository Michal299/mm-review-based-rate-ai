import pandas as pd

n = 250

dataset = pd.read_csv('../dataset/extended_dataset.csv', sep='$', encoding='utf-8')

how_many_users_commented_films = dataset.groupby('title')['username'].apply(list).reset_index(name="users")

how_many_users_commented_films['count'] = how_many_users_commented_films['users'].apply(len)

below_n_comments = how_many_users_commented_films[how_many_users_commented_films['count'] < n]

print(below_n_comments)

print("Comments to remove: " + str(below_n_comments['count'].sum()))

print(dataset)

titles_to_remove = below_n_comments['title'].tolist()

dataset = dataset[~dataset['title'].isin(titles_to_remove)]

print(dataset)

dataset.to_csv('../dataset/dataset_with_more_than_n_comments.csv', sep='$', encoding='utf-8')

print("How many movies and tv series do we have? " + str(len(pd.unique(dataset['title']))))
only_movies = dataset[dataset['type'] == 'movie']
print("How many movies do we have? " + str(len(pd.unique(only_movies['title']))))
only_tv_series = dataset[dataset['type'] == 'tv_series']
print("How many tv_series do we have? " + str(len(pd.unique(only_tv_series['title']))))
