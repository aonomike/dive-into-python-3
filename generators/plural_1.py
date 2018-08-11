import re


def plural(noun):

        if re.search('[sxz]$', noun):
                return re.sub('$', 'es', noun)
        elif re.search('[^aeioudgkprt]h', noun):
                return re.sub('$', 'es', noun)
        elif re.search('[^aeiou]y$', noun):
            return re.sub('y$', 'ies', noun)
        else:
            return '{}s'.format(noun)


print(plural('boy'))
print(plural('vacancy'))
print(plural('beer'))
print(plural('buzz'))
print(plural('brush'))
