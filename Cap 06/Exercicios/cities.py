cities = {
    'sao paulo' : {
        'country' : 'brazil',
        'population' : 102546,
        'fact' : 'Muitos prédios'
    },

    'rio de janeiro' : {
        'country': 'brazil',
        'population': 145236,
        'fact': 'Praias bonitas'
    },

    'minas gerais': {
        'country': 'brazil',
        'population': 1125,
        'fact': 'Melhor pão de queijo'
    },
}

for city, info_city in cities.items():
    print("\nInformações sobre a cidade " + city.title() + ":")
    print("\tCountry: " + info_city['country'].title())
    print("\tPopulação: " + str(info_city['population']))
    print("\tFato: " + info_city['fact'].title())