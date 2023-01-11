from typing import Dict
from typing import Generic
from typing import Tuple
from typing import Type

from typing_extensions import get_args

from .exceptions import ContractAlreadyRegisteredException
from .exceptions import ContractNotFoundException
from .exceptions import InvalidContractClassException
from .exceptions import MapperServiceException
from .mapper_contract import DESTINATION
from .mapper_contract import MapperContract
from .mapper_contract import SOURCE


class Mapper(Generic[SOURCE, DESTINATION]):
    _contracts: Dict[str, MapperContract[SOURCE, DESTINATION]] = {}

    def create(self, source: SOURCE) -> DESTINATION:
        contract = self._try_get_contract()
        return contract.create(source)

    def update(self, target: DESTINATION, source: SOURCE) -> None:
        contract = self._try_get_contract()
        return contract.update(target, source)

    @classmethod
    def register_contract(cls, contract: Type[MapperContract[SOURCE, DESTINATION]]) -> None:
        if not issubclass(contract, MapperContract):
            raise InvalidContractClassException(f'{contract} is not a subclass of MapperContract')

        source_class, destination_class = cls._get_generic_classes(contract)
        contract_name = cls._get_contract_name(source_class, destination_class)

        if contract_name in cls._contracts:
            raise ContractAlreadyRegisteredException(f'Contract {contract} already registered')

        cls._contracts[contract_name] = contract()

    @classmethod
    def unregister_contract(cls, contract: Type[MapperContract[SOURCE, DESTINATION]]) -> None:
        source_class, destination_class = cls._get_generic_classes(contract)
        contract_name = cls._get_contract_name(source_class, destination_class)
        cls._contracts.pop(contract_name)

    @classmethod
    def has_registered_contract(cls, contract: Type[MapperContract[SOURCE, DESTINATION]]) -> bool:
        source_class, destination_class = cls._get_generic_classes(contract)
        contract_name = cls._get_contract_name(source_class, destination_class)

        return contract_name in cls._contracts

    @staticmethod
    def _get_contract_name(source_class: Type[SOURCE], target_class: Type[DESTINATION]) -> str:
        return f'{source_class.__module__}.{source_class.__name__}:{target_class.__module__}.{target_class.__name__}'

    @staticmethod
    def _get_generic_classes(contract: Type[MapperContract[SOURCE, DESTINATION]]) -> Tuple[Type[SOURCE], Type[DESTINATION]]:
        return get_args(contract.__orig_bases__[0])

    def _try_get_contract(self) -> MapperContract[SOURCE, DESTINATION]:
        if not hasattr(self, '__orig_class__'):
            raise MapperServiceException(
                'The instance of MapperService has to be created with Generic arguments explicitly.\n'
                'Example: mapper = MapperService[SOURCE, DESTINATION]()'
            )

        source_class, destination_class = get_args(self.__orig_class__)
        contract_name = Mapper._get_contract_name(source_class, destination_class)

        contract = self._contracts.get(contract_name)
        if contract is None:
            raise ContractNotFoundException(f'Contract for {contract_name} was not found')

        return contract
