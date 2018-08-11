import re


def match_sxz(noun):
    return re.search('[szx]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return '{}s'.format(noun)


rules = (
            (match_sxz, apply_sxz),
            (match_h, apply_h),
            (match_y, apply_y),
            (match_default, apply_default)
        )


def plural(noun):

    '''
        return (apply_rule(noun) for matches_rule, apply_rule in
        rules if matches_rule(noun))
    '''
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


noun = input("Enter noun")
print(plural(noun))
print(plural('boy'))
print(plural('vacancy'))
print(plural('beer'))
print(plural('buzz'))
print(plural('brush'))
