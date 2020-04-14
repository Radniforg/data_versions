

def word_counter(word_list):
    words_list = {}
    for line in word_list:
        words = line.split(' ')
        for word in words:
            if len(word) > 6:
                word_amount = int(words_list.get(word.lower(), 0)) + 1
                words_list[word.lower()] = word_amount
    return words_list


def json_version():
    import json
    with open('newsafr.json', encoding='utf-8') as json_data:
        phrases = []
        json_content = json.load(json_data)
        for news in json_content['rss']['channel']['items']:
            phrases.append(news['description'])
    return phrases


def sort_and_output(dictionary):
    top_ten = 1
    runner_up = 0
    while top_ten < 10:
        for key, value in dictionary.items():
            if int(value) == max(dictionary.values()) - runner_up:
                print(f'На {top_ten} месте: {key} - {value}')
                top_ten += 1
                if top_ten > 10:
                    break
        runner_up += 1


diction = sort_and_output(word_counter(json_version()))





