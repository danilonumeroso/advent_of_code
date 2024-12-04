import math
from collections import deque

LOW = 0
HIGH = 1

def parse_devices(lines):
    devices = {}
    for line in lines:
        name, value = line.split('->')
        name = name.strip()
        value = value.strip()
        devices[name[1:] if not name.startswith('b') else name] = {
            'type': name[0],
            'dest': [v.strip() for v in value.split(',')],
        }

    for key in devices:
        if devices[key]['type'] == '%':
            devices[key]['state'] = LOW

        for dst in devices[key]['dest']:
            if dst in devices and devices[dst]['type'] == '&':
                if 'src' not in devices[dst]:
                    devices[dst]['src'] = {}
                devices[dst]['src'][key] = LOW
    return devices

def reset_devices(devices):
    for key in devices:
        if devices[key]['type'] == '%':
            devices[key]['state'] = LOW
        elif devices[key]['type'] == '&':
            for src in devices[key]['src']:
                devices[key]['src'][src] = LOW

    

def is_flip_flop(node):
    return node['type'] == '%'

def is_conjunction(node):
    return node['type'] == '&'

def handle_flip_flop(node):
    node['state'] = 1 - node['state']
    return node['state']

def handle_conjunction(node, sender, signal):
    node['src'][sender] = signal

    if all(node['src'].values()):
        return LOW
    
    return HIGH

def compute_interval(devices, gate):
    # Instatiate a FIFO queue
    queue = deque()
    queue.append(('button', 'broadcaster', LOW))
    
    while queue:
        sender, receiver, signal = queue.popleft()

        if receiver == gate and signal == LOW:
            return True

        if receiver not in devices:
            continue        

        if is_flip_flop(devices[receiver]) and signal == HIGH:
            continue

        if is_flip_flop(devices[receiver]) and signal == LOW:
            signal = handle_flip_flop(devices[receiver])
        elif is_conjunction(devices[receiver]):
            signal = handle_conjunction(devices[receiver], sender, signal)
            
        for dst in devices[receiver]['dest']:
            queue.append((receiver, dst, signal))

    return False

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    devices = parse_devices(lines)

    gates = [key for key in devices if 'mf' in devices[key]['dest']]
    intervals = []

    for gate in gates:
        it = 1
        while not compute_interval(devices,gate):
            it += 1
        reset_devices(devices)
        intervals.append(it)

    print(math.lcm(*intervals))
