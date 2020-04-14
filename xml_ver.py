

def word_counter(word_list):
    words_list = {}
    word_sorting = []
    for line in word_list:
        words = line.split(' ')
        for word in words:
            word_sorting.append(word)
    for sorted_word in sorted(word_sorting):
        if len(sorted_word) > 6:
            word_amount = int(words_list.get(sorted_word.lower(), 0)) + 1
            words_list[sorted_word.lower()] = word_amount
    return words_list


def xml_version():
    phrases = []
    import xml.etree.ElementTree as Et
    parser = Et.XMLParser(encoding='utf-8')
    tree = Et.parse(f'newsafr.xml', parser)
    root = tree.getroot()
    channel = root.find('channel')
    items = channel.findall('item')
    for item in items:
        phrases.append(item.find('description').text)
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

diction = sort_and_output(word_counter(xml_version()))




