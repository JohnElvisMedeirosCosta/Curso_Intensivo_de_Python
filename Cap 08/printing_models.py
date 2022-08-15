def print_models(unprinted_design, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    while unprinted_design:
        current_design = unprinted_design.pop()

        #Simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Mostra todos os modeles impressos.
    """
    print("\nThe following models have been printed:")

    for completed_model in completed_models:
        print(completed_model)

unprited_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprited_designs, completed_models)
show_completed_models(completed_models)