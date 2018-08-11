def rules(rules_filename):
    with open(rules_filename, encoding='UTF-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename="plural4-rules.txt"):
    for matches_rule, apply_rule in rules(filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError("No matching rule")
