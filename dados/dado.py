import numpy as np

def simular_dado(nsim: int, seed: int| None = None):
    if seed is not None: 
        np.random.seed(seed)

    #lançamentos de dados de 1 a 6
    resultados = np.random.randint(1, 7, size = nsim)

    #frequencia de cada face 
    valores, contagens = np.unique(resultados, return_counts=True)

    probabilidades = contagens/nsim

    print("Resultados: ", resultados.tolist())

    print("\nFrequências:")
    for valor, contagens, prob in zip(valores, contagens, probabilidades):
        print(f"Face {valor}: contagens vezes | Prob = {prob:.3f}")

        print("\nMédia experimenta:", np.mean(resultados))

        print("Média teórica: 3.5")

        return resultados
    
simular_dado(nsim=100, seed=42)