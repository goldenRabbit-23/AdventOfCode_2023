import sys


def main():
    workflow_block, parts_block = open(sys.argv[1]).read().split("\n\n")

    workflows = {}
    for line in workflow_block.splitlines():
        name, rules_str = line[:-1].split('{')
        rules = rules_str.split(',')
        parsed_rules = []

        for rule in rules:
            if ':' in rule:
                condition, dest = rule.split(':')
                var, operator = condition[0], condition[1]
                value = int(condition[2:])
                parsed_rules.append((var, operator, value, dest))
            else:
                parsed_rules.append((None, None, None, rule))

        workflows[name] = parsed_rules

    parts = []
    for line in parts_block.splitlines():
        attrs = line[1:-1].split(',')
        part_dict = {}
        for attr in attrs:
            key, value = attr.split('=')
            part_dict[key] = int(value)
        parts.append(part_dict)

    answer = 0

    for part in parts:
        current_workflow = 'in'

        while current_workflow not in ('A', 'R'):
            rules = workflows[current_workflow]

            for var, operator, value, dest in rules:
                if var is None:
                    current_workflow = dest
                    break

                part_value = part[var]
                if operator == '>' and part_value > value:
                    current_workflow = dest
                    break
                elif operator == '<' and part_value < value:
                    current_workflow = dest
                    break

        if current_workflow == 'A':
            answer += sum(part.values())

    print(answer)


if __name__ == "__main__":
    main()
