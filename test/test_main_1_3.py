import pytest

from main_1_3 import vote

citizens_votes = [
    [3, 2, 3, 2, 1, 1, 1, 3, 1, 1],
    [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 2, 1, 2, 1, 1],
    [1, 2, 2, 3, 2, 1, 1, 3, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 1],
    [2, 2, 1, 3, 3, 2, 3, 1, 1, 2, 1, 2, 2, 2, 3],
    [3, 3, 2, 2, 1, 3, 1, 2, 3, 1, 2, 2, 1, 3, 3],
]
params = ((citizens_votes[0],1),
          (citizens_votes[1],1),
          (citizens_votes[2],"Нужен второй тур выборов"),
          (citizens_votes[3],2),
          (citizens_votes[4],3))
@pytest.mark.parametrize('votes,expected',params)

def test_vote(votes,expected):
    assert vote(votes) == expected

