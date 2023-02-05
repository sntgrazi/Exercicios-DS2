from cod_ddd import DDD
from ddd_repository import DddRepository
from ddd_service import DddService
from user_interface import UserInterface


ddd_repository = DddRepository()

ddd_repository.append(DDD(75, "Feira de Santana"))
ddd_repository.append(DDD(71, "Salvador"))

ddd_service = DddService(ddd_repository)
user_interface = UserInterface(ddd_service)

while True:
    
    result = user_interface.input_user_ddd()
    if result == "DDD não encontrado":
        print(result)
        break
    else:
         print(result)
