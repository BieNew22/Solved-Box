import os
from utils import add_space, update_gist, make_graph
from profile import get_user_data

user_name = os.environ.get('USER_NAME')
github_token = os.environ.get('GH_TOKEN')
gist_id = os.environ.get('GIST_ID')

if __name__ == "__main__":
    # check environment
    if not user_name or not github_token or not gist_id:
        print("Please set the environment")
        exit(1)

    # get user data
    user_data = get_user_data(user_name)
    if not user_data:
        print("Please check your user name")
        exit(1)

    # make content
    halfGistWidth = 23
    betweenTxt = " " * 3

    rankAndName = f'#{f'{user_data.rank:,}'} @{user_name}'
    percent = user_data.rating / user_data.need_rating * 100
    display_percent = f'{round(percent, 1)}% ({user_data.rating:,})'
    graph = make_graph(percent, 15)

    special_space = "ㅤ"
    print(len(display_percent))
    print(len(graph))
    content = [add_space(user_data.tier, halfGistWidth, special_space), betweenTxt,
               add_space(special_space, halfGistWidth, rankAndName), "\n",
               add_space(graph, halfGistWidth + halfGistWidth // 2 - 4, display_percent), "\n",
               add_space("✅ Solved :", halfGistWidth, user_data.solved), betweenTxt,
               add_space("🔥 Streak : ", halfGistWidth, user_data.streak), "\n",
               add_space("💠 Class  :", halfGistWidth, user_data.classValue), betweenTxt,
               add_space("🧭 Arena  :", halfGistWidth, user_data.arena), "\n"]

    """ 내용 구상안
    file name : newbie22's solved.ac profile
    1. tear                     #rank
    2. rating (그래프 형식) %출력
    3. ✅ Solved:           321     🔥 Streak:           23
    4. 💠 Class:              4     🧭 Arena:             0      
    """
    print(''.join(content))
    update_gist(gist_id, github_token, ''.join(content), user_name)