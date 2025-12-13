import sys
from collections import deque


def main():
    data = open(sys.argv[1]).read().splitlines()
    modules = {}
    broadcast_targets = []

    for line in data:
        left, right = line.split(' -> ')
        destinations = right.split(', ')

        if left == 'broadcaster':
            broadcast_targets = destinations
            modules['broadcaster'] = {
                'type': 'broadcaster',
                'dests': destinations,
                'memory': {},
                'state': False
            }
        else:
            module_type, module_name = left[0], left[1:]
            modules[module_name] = {
                'type': module_type,
                'dests': destinations,
                'memory': {},
                'state': False
            }

    for name, module in modules.items():
        for dest in module['dests']:
            if dest in modules and modules[dest]['type'] == '&':
                modules[dest]['memory'][name] = 'low'

    low_pulses, high_pulses = 0, 0
    q = deque()

    for _ in range(1000):
        low_pulses += 1

        for dest in broadcast_targets:
            q.append(('broadcaster', dest, 'low'))

        while q:
            source, target, pulse = q.popleft()

            if pulse == 'low':
                low_pulses += 1
            else:
                high_pulses += 1

            if target not in modules:
                continue

            module = modules[target]

            if module['type'] == '%':
                if pulse == 'low':
                    module['state'] = not module['state']
                    outgoing = 'high' if module['state'] else 'low'
                    for next_dest in module['dests']:
                        q.append((target, next_dest, outgoing))

            elif module['type'] == '&':
                module['memory'][source] = pulse
                all_high = all(x == 'high' for x in module['memory'].values())
                outgoing = 'low' if all_high else 'high'
                for next_dest in module['dests']:
                    q.append((target, next_dest, outgoing))

    print(low_pulses * high_pulses)


if __name__ == "__main__":
    main()
