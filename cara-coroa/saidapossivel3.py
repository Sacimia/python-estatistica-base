import numpy as np
from dataclasses import dataclass

@dataclass
class ResultadoSimulacao:
    prob_cara: float
    prob_coroa: float
    total_caras: int
    total_coroas: int
    resultados: list


def simular_moeda(p: float, nsim: int, seed: int | None = None) -> ResultadoSimulacao:
    """
    Simula lançamentos de moeda com probabilidade p de sair cara.
    
    Args:
        p (float): Probabilidade de sair cara (0 <= p <= 1)
        nsim (int): Número de simulações
        seed (int, optional): Semente para reprodutibilidade
        
    Returns:
        ResultadoSimulacao: Estatísticas da simulação
    """

    if not 0 <= p <= 1:
        raise ValueError("A probabilidade p deve estar entre 0 e 1.")
    
    if seed is not None:
        np.random.seed(seed)

    resultados_bool = np.random.random(nsim) < p
    resultados = resultados_bool.astype(int)

    total_caras = int(resultados.sum())
    total_coroas = nsim - total_caras

    prob_cara = total_caras / nsim
    prob_coroa = total_coroas / nsim

    return ResultadoSimulacao(
        prob_cara=prob_cara,
        prob_coroa=prob_coroa,
        total_caras=total_caras,
        total_coroas=total_coroas,
        resultados=resultados.tolist()
    )


# ---------------- USO ----------------
resultado = simular_moeda(
           p=0.6, 
           nsim=100, 
           seed=42)

print(resultado)