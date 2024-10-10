import requests


def update_gist(gist_id: str, github_token: str, content: str, user_name: str) -> None:
    url = f'https://api.github.com/gists/{gist_id}'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {github_token}',
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f'Failed to get gist: {resp.status_code} {resp.text}')
    gist = resp.json()
    file_name = list(gist['files'].keys())[0]
    data = {
        'files': {
            file_name: {
                'filename': f'{user_name}\'s solved.ac profile',
                'content': content
            }
        }
    }
    resp = requests.patch(url, headers=headers, json=data)
    if resp.status_code != 200:
        raise Exception('Failed to update gist')


def add_space(pre, length, suf):
    lenA, lenB = len(pre), len(str(suf))
    return str(pre) + ' ' * (length - lenA - lenB) + str(suf)


def make_graph(percent, size):
    data = ['⬜', '⬛']

    full = int(size * (percent / 100))
    return data[1] * full + data[0] * (size - full)
