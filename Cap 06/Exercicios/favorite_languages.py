favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

names = ('jen', 'maria', 'john', 'edward', 'phil', 'sarah')

for name in names:
    if name in favorite_languages.keys():
        print('Obrigado ' + name)
    else:
        print('Responde ' + name)