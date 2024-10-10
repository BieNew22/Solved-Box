import requests


class UserProfile:
    def __init__(self):
        self.tier = ""
        self.rank = ''
        self.need_rating = 0
        self.rating = 0
        self.solved = ''
        self.streak = ''
        self.classValue = ""
        self.arena = ""

    def print_self(self):
        print(f'Tier   : {self.tier}')
        print(f'Rank   : {self.rank}')
        print(f'Rating : {self.rating}')
        print(f'Need   : {self.need_rating}')
        print(f'Solved : {self.solved}')
        print(f'Streak : {self.streak}')
        print(f'Class  : {self.classValue}')
        print(f'Arena  : {self.arena}')


def get_user_data(id: str) -> UserProfile | None:
    """
    Get User data from solved.ac
    :param id: user id
    :return: UserProfile or None
    """
    # get user basic data from solved.ac
    url = f'https://solved.ac/api/v3/search/user?query={id}'
    res = requests.get(url)

    if res.status_code != 200:
        raise Exception('fail to connect solved.ac')

    DB = dict(res.json())

    if DB['count'] == 0:
        return None

    user_data = DB['items'][0]

    # get user streak information
    url = f'https://solved.ac/api/v3/user/grass?handle={id}&topic=default'
    res = requests.get(url)

    if res.status_code != 200:
        raise Exception('fail to connect solved.ac')

    nowStreak = res.json()

    # Extract essential data
    res = UserProfile()

    CLASS_ADD = {'none': '', 'sliver': '+', 'gold': '++'}

    res.streak = str(nowStreak['currentStreak']).strip()
    res.solved = str(user_data['solvedCount']).strip()
    res.rank = user_data['rank']
    res.tier = num_to_tier(user_data['tier']).strip()
    res.classValue = str(user_data['class']) + str(user_data['classDecoration'])
    res.arena = num_to_arena_tier(user_data['arenaTier'], user_data['arenaRating']).strip()

    res.rating = user_data['rating']
    res.need_rating = get_need_rating(user_data['tier'])

    return res


def num_to_tier(num):
    VALUE = {
        4: "I",
        3: "II",
        2: "III",
        1: "IV",
        0: "V"
    }

    TIER = {
        0: "🟫Bronze",
        1: "⬜Silver",
        2: "🟨Gold",
        3: "🟩Platinum",
        4: "🟦Diamond",
        5: "🟥Ruby",
    }

    if num == 0:
        return "⬛Unrated"
    elif num == 31:
        return "🟪Master"
    else:
        return TIER[(num - 1) // 5] + " " + VALUE[(num - 1) % 5]


def num_to_arena_tier(num, rating):
    DB = {
        0: "Unrated", 1: "C", 2: "C+", 3: "B", 4: "B+",
        5: "A", 6: "A+", 7: "S", 8: "S+", 9: "SS", 10: "SS+",
        11: "SSS", 12: "SSS+", 13: "X"
    }
    if num == 0:
        return DB[num]
    return f'{DB[num]} ({rating})'


def get_need_rating(tier):
    DB = [0, 30, 60, 90, 120, 150,
          200, 300, 400, 500, 650,
          800, 950, 1100, 1250, 1400, 1600, 1750,
          1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600,
          2700, 2800, 2850, 2900, 2950, 3000, 3000]

    return DB[tier + 1]
