from cod_ddd import DDD
from ddd_repository import DddRepository
from ddd_service import DddService
from user_interface import UserInterface


ddd_repository = DddRepository()

ddd_repository.append(DDD(68, "Rio Branco"))
ddd_repository.append(DDD(82, "Maceió"))
ddd_repository.append(DDD(96, "Macapá"))
ddd_repository.append(DDD(92, "Manaus"))
ddd_repository.append(DDD(71, "Salvador"))
ddd_repository.append(DDD(85, "Fortaleza"))

ddd_service = DddService(ddd_repository)
user_interface = UserInterface(ddd_service)

while True:
    
    result = user_interface.input_user_ddd()
    if result == "DDD não encontrado":
        print(result)
        break
    else:
         print(result)
