
"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    counts = dict()
    words = s.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    import operator
    sorted_words = sorted(sorted(counts.items()), key=operator.itemgetter(1), reverse = True)
    # print sorted_words
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    i = 0
    top_n = list()
    while i < n:
        top_n.append(tuple(sorted_words[i]))
        i += 1
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()