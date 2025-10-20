import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # storing probabilities of each page
    transition = {}

    # number of pages or sites
    number_of_pages = len(corpus.keys())

    # initial probability for all pages
    for link in corpus.keys():
        transition[link] = (1 - damping_factor) / number_of_pages
    
    # number of links inside page
    length = len(corpus[page])

    # if length is empty it transtion needs to add damping_factor / number_of_pages, because if 
    if not length:
        for link in corpus.keys():
            transition[link] += damping_factor / number_of_pages
    # else if will add simple probability for every count of that page
    else:
        for link in corpus[page]:
            transition[link] += damping_factor / length

    return transition


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # first page is choosen randomly
    cur_page = random.choice(list(corpus.keys()))
    
    # for storing ranking of pages
    ranking = {}

    for i in range(n):
        
        # making sure that we have cur_page in ranking
        ranking[cur_page] = ranking.get(cur_page, 0) + 1

        # it will return probability of choosing next pages
        transition = transition_model(corpus, cur_page, damping_factor)

        # using random module we will choose one of the choices based on probability
        cur_page = random.choices(
            population=list(transition.keys()), 
            weights=list(transition.values()), 
            k=1
        )[0]

    # making all sum up to 1
    for link in ranking:
        ranking[link] /= n

    return ranking


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """ 
    
    n = len(corpus)
    PageRank = {page: 1 / n for page in corpus.keys()}

    # for changing containing of empty pages
    fixed_corpus = {}
    for page, links in corpus.items():
        if links:
            fixed_corpus[page] = links
        else:
            fixed_corpus[page] = set(corpus.keys())
    
    changed = True
    while changed:
        new_rank = {}
        changed = False
        
        for page in corpus:

            # initial rank is (1 - damping_f) / n for every page
            rank = (1 - damping_factor) / n

            for possible_page in corpus:
                if page in fixed_corpus[possible_page]:

                    # formula for finding pagerank with current pagerank
                    rank += (
                        damping_factor * 
                        (PageRank[possible_page]) / len(fixed_corpus[possible_page])
                    )
            # assigning new ranking of page
            new_rank[page] = rank

            if abs(new_rank[page] - PageRank[page]) > 0.001:
                changed = True
        # every iteration ranking will be changed 
        PageRank = new_rank
    
    return PageRank


if __name__ == "__main__":
    main()
