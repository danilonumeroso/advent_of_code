import re

def parse_rating(rating):
    """
        Parse rating from input file.
        Returns a dict of the form:
        {
            'a': 3,
            'b': 4,
            'c': 5
        }
    """
    expr = re.findall(r'[a-z]=\d+', rating)
    return {
        e.split('=')[0]: int(e.split('=')[1])
        for e in expr
    }

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

def cond_fn(rating, cond):
    """Evaluates the condition given a rating."""
    if cond == '':
        return True
    
    var_name = cond[0]
    return rating[var_name] > int(cond[2:]) if '>' in cond else rating[var_name] < int(cond[2:])

def apply_rules(workflows, name, rating):
    for rule in workflows[name]:
        cond, action = rule['cond'], rule['action']

        if cond_fn(rating, cond):
            return action
        
    raise "No rules apply"

def is_accepted(workflows, name, rating):
    """
        Main function: returns True if the rating is accepted, False otherwise.
    """
    action = apply_rules(workflows, name, rating)
    if action in ['A','R']:
        return action == 'A'
    return is_accepted(workflows, action, rating)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        workflows, ratings = f.read().split('\n\n')
    workflows = workflows.split('\n')
    ratings = ratings.split('\n')

    ratings = [parse_rating(r) for r in ratings]
    workflows = parse_workflows(workflows)
    
    accepted_ratings = list(filter(lambda r: is_accepted(workflows, 'in', r), ratings))
    print(sum([sum(a.values()) for a in accepted_ratings]))

