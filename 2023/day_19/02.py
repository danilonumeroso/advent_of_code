import re

MIN_NUMBER = 1
MAX_NUMBER = 4000

def invert_cond(cond):
    if cond == '':
        return ''
    
    if '>' in cond:
        return cond.replace('>', '<')

    return cond.replace('<', '>')

def parse_workflows(workflows):
    """
        Parse workflows from input file.
        Returns a dict of the form:
        {
            'workflow_name': [
                {
                    'cond': 'a>3',
                    'action': 'B'
                },
                {
                    'cond': '',
                    'action': 'A'
                }
            ]
        }
    """
    res = {}
    for w in workflows:
        # Get workflow name
        name = re.findall(r'[a-z]+{', w)[0][:-1]
        res[name] = {}

        # Get workflow rules
        rules = re.findall(r'{.+}', w)[0][1:-1].split(',')
        res[name] = []

        for rule in rules:
            if ":" not in rule:
                res[name].append({
                    'cond': '',
                    'action': rule
                })
                continue

            cond, action = rule.split(':')
            res[name].append({
                'cond': cond,
                'action': action
            })
    
    return res

def compute_global_conditions(workflows): 
    from collections import deque


    queue = deque([('in', '')])
    conditions = []

    while queue:
        action, global_cond = queue.popleft()

        if action == 'R':
            continue

        if action == 'A':
            conditions.append(global_cond[1:])
            continue

        for rule in workflows[action]:
            cond, action = rule['cond'], rule['action']

            if '>' in cond:
                cond = cond[:2] + str(int(cond[2:]) + MIN_NUMBER)

            new_cond = global_cond + (',' + cond if cond != '' else '')
            global_cond = global_cond + (',' + invert_cond(cond) if cond != '' else '')
            queue.append((action, new_cond))

    return conditions

def reduce_cond(conditions):
    """
        Given a list of conditions, returns a tuple (greater_than, less_than) where:
            - less_than is the maximum number that is less than all the numbers in the conditions
            - greater_than is the minimum number that is greater than all the numbers in the conditions
        Example:
            ['x<8', 'x>3','x>5'] -> [5, 8]
    """
    less_than, greater_than = MAX_NUMBER+1, MIN_NUMBER
    for cond in conditions:
        if '<' in cond:
            less_than = min(less_than, int(cond.split('<')[1]))
        elif '>' in cond:
            greater_than = max(greater_than, int(cond.split('>')[1]))
    return (greater_than, less_than)

def compute_number_of_combinations(conditions):

    res = 0

    for cond in conditions:
        x_cond = [c for c in cond.split(',') if c.startswith('x')]
        m_cond = [c for c in cond.split(',') if c.startswith('m')]
        a_cond = [c for c in cond.split(',') if c.startswith('a')]
        s_cond = [c for c in cond.split(',') if c.startswith('s')]

        x = reduce_cond(x_cond)
        m = reduce_cond(m_cond)
        a = reduce_cond(a_cond)
        s = reduce_cond(s_cond)

        combinations = 1
        for interval in [x, m, a, s]:
            combinations *= interval[1] - interval[0]

        res += combinations

    return res

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        workflows, ratings = f.read().split('\n\n')

    workflows = workflows.split('\n')
    workflows = parse_workflows(workflows)
    
    print(compute_number_of_combinations((compute_global_conditions(workflows))))

