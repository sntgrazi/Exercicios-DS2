from ddd_service import DddService

class UserInterface():
    def __init__(self, ddd_service: DddService) -> None:
        self.ddd_service = ddd_service
        
    def input_user_ddd(self) -> None:   
        cod = input("Digite o DDD → ")
        
        resultado = self.ddd_service.encontrarCidade(int(cod))
        
        return resultado