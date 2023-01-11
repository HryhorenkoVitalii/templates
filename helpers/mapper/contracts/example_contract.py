from ..mapper_contract import MapperContract


class ExampleMapper(MapperContract[Example1, Example2]):
    def create(self, source: list[Example1]) -> list[Example12]:
        result = []
        for item in source:
            result.append(Example2(
                            id=item.id,
                            name=item.name,
                            )   
                        )
        return result