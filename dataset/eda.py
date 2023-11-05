import string

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from collections import Counter


def plot_bars(data, column):
    column_distribution = pd.DataFrame(data[column].value_counts()).reset_index()

    plt.figure(figsize=(10, 5))
    bars = plt.bar(column_distribution['index'], column_distribution[column])

    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), bar.get_height(), va='bottom', ha='center')

    plt.xticks(column_distribution['index'])
    plt.xlabel(column)
    plt.ylabel("frequency")
    plt.title("Distribution of " + column)

    plt.show()


def plot_hist(data, column):
    fig, ax = plt.subplots(figsize=(10, 5))
    n, bins, patches = ax.hist(data[column], rwidth=0.95)
    bins_as_ints = [int(round(x)) for x in bins]
    ax.set_xticks(bins_as_ints)
    plt.xlabel(column)
    plt.ylabel("frequency")
    plt.title("Distribution of " + column)

    plt.show()


def findMostFrequentWords(comments, k):
    text = comments.str.cat(sep=' ')
    text = text.translate(str.maketrans('', '', string.punctuation))
    listOfWords = text.split()
    listOfWordsWithoutConjunctions = [w.lower() for w in listOfWords if len(w) > 5]
    counter = Counter(listOfWordsWithoutConjunctions)
    return counter.most_common(k)


def to_len(comment):
    if type(comment) == str:
        return len(comment)
    return comment


if __name__ == "__main__":
    films = pd.read_csv('dataset.csv', sep='$')
    tv_series = pd.read_csv('dataset_tv_series.csv', sep='$')

    plot_bars(films, 'user_rate')
    plot_bars(tv_series, 'user_rate')

    films['user_comment_length'] = films['user_comment'].map(to_len)
    tv_series['user_comment_length'] = tv_series['user_comment'].map(to_len)

    plot_hist(films, 'user_comment_length')
    plot_hist(tv_series, 'user_comment_length')

    print(findMostFrequentWords(films['user_comment'], 25))
    print(findMostFrequentWords(tv_series['user_comment'], 25))

    numerical_attributes = ['user_rate', 'movie_rating', 'movie_rating_count']
    pd.plotting.scatter_matrix(films[numerical_attributes], figsize=(16, 8))
    plt.show()

    f, ax = plt.subplots(figsize=(16, 8))
    sns.heatmap(films.corr(), annot=True, linewidths=.1, fmt='.2f', ax=ax)
    plt.title('correlation matrix', fontweight="bold")
    plt.show()
