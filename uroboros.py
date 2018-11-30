from git import Repo


DATE = '01.12.2018'

with open(__file__, 'r') as f:
    i_am = f.read().split('\n')

with open('dates.txt') as f:
    i_am[3] = 'DATE = {}'.format(f.readline()[:-2])


repo = Repo('./')
print(repo.active_branch)
repo.git.fetch()
repo.index.add(['uroboros.py'])
repo.index.commit('wop')
origin = repo.remote(name='origin')
origin.push()

# repo.git
