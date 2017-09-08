from collections import defaultdict
def group_anagrams(words):
    '''Given an array of strings, group anagrams together.'''
    groups = defaultdict(list)
    for w in words:
        groups[''.join(sorted(w)).replace(' ', '')].append(w)

    return list(groups.values())

if __name__ == '__main__':
    words = ["eat", "tea", "tan","国家","ate", "nat", "bat", "家国", "william shakespeare", "i am a weakish speller"]
    groups = group_anagrams(words)
    print(groups)
    # [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate'], ['国家', '家国'], ['william shakespeare', 'i am a weakish speller']]

