from typing import Generic
from typing import TypeVar

from .exceptions import ContractMethodIsNotSupported

SOURCE = TypeVar('SOURCE')
DESTINATION = TypeVar('DESTINATION')


class MapperContract(Generic[SOURCE, DESTINATION]):
    def create(self, source: SOURCE) -> DESTINATION:
        raise ContractMethodIsNotSupported('Method is not supported')

    def update(self, target: DESTINATION, source: SOURCE) -> None:
        raise ContractMethodIsNotSupported('Method is not supported')
