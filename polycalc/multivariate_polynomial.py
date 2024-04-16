from polynomial import Polynomial

class MultivariatePolynomial(Polynomial):
    
    def __init__(self, coefficients: list[list[float]]) -> None:
        self.co = coefficients
        
    def evaluate(self, inputs: list[float]) -> float:
        return sum([sum([(input**i)*co for i, co in enumerate(self.co[i])]) for i, input in enumerate(inputs)])