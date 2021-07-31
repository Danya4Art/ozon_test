import re


def get_value(key, string):
    pattern = rf'\[.*{key}:(?P<value>("[\-\w\s]*")|(\d*)).*\]'
    res = re.match(pattern, string).group('value')
    if '"' in res:
        res = res[1:len(res)-1]
    return res


f_in = open('input.txt', 'r')
stat = {
    "Validation error": {'count': 0, 'user_type': {}},
    "AntiFraud": {'count': 0, 'user_type': {}},
    "Unkown user": {'count': 0, 'user_type': {}}  # очепятка?)
}

data = {}

for string in f_in:
    if get_value('function', string) == 'MakePayment':
        message = get_value('message', string)
        if message not in stat.keys():
            continue
        stat[message]['count'] += 1
        user_type = get_value('user_type', string)
        if user_type in stat[message]['user_type'].keys():
            stat[message]['user_type'][user_type] += 1
        else:
            stat[message]['user_type'][user_type] = 1
        data[get_value('user_id', string)] = message

f_in.close()
f_out = open('output.txt', 'w')

for message in stat.keys():
    max_count_user_type = max(stat[message]['user_type'], key=stat[message]['user_type'].get)
    f_out.write(f'message "{message}", count {stat[message]["count"]}, most count user type {max_count_user_type}\n')

f_out.write('\n')

for id in data.keys():
    f_out.write(f'{id:10}\t"{data[id]}"\n')











