import sys
from math import prod


def main():
    workflow_block, _ = open(sys.argv[1]).read().split("\n\n")

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

    def dfs(current_workflow, ranges) -> int:
        # Base case
        if current_workflow == 'R':
            return 0
        if current_workflow == 'A':
            return prod(hi - lo + 1 for lo, hi in ranges.values())

        rules = workflows[current_workflow]
        total = 0

        # Recursive case
        current_ranges = ranges.copy()

        for var, operator, value, dest in rules:
            if var is None:
                total += dfs(dest, current_ranges)
            else:
                lo, hi = current_ranges[var]

                if operator == '<':
                    pass_lo, pass_hi = lo, min(hi, value - 1)
                    fail_lo, fail_hi = max(lo, value), hi
                elif operator == '>':
                    pass_lo, pass_hi = max(lo, value + 1), hi
                    fail_lo, fail_hi = lo, min(hi, value)

                if pass_lo <= pass_hi:
                    next_ranges = current_ranges.copy()
                    next_ranges[var] = (pass_lo, pass_hi)
                    total += dfs(dest, next_ranges)

                if fail_lo <= fail_hi:
                    current_ranges[var] = (fail_lo, fail_hi)

        return total

    print(dfs('in', {key: (1, 4000) for key in "xmas"}))


if __name__ == "__main__":
    main()
