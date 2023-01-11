class MapperServiceException(Exception):
    pass


class ContractNotFoundException(MapperServiceException):
    pass


class ContractAlreadyRegisteredException(MapperServiceException):
    pass


class InvalidContractClassException(MapperServiceException):
    pass


class ContractMethodIsNotSupported(MapperServiceException):
    pass
