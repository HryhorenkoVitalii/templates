from .contracts.example_contract import ExampleMapper
from .facade import Mapper

Mapper.register_contract(ExampleMapper)
