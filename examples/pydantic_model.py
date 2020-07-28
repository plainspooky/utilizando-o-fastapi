from datetime import datetime

from pydantic import BaseModel, validator


class Order(BaseModel):
    """
    Estrutura de exemplo para armazenar pedido.
    """

    id: int
    name: str


class ValidatedOrder(Order):
    """
    Estruturar de exemplo para armazenar o pedido (com validação)
    """

    value: float
    order_date: datetime

    @validator("order_date")
    def validate_order(cls, v: datetime, **kwargs) -> datetime:
        """
        Verifica se a ordem do pedido não está no futuro.
        """
        if v > datetime.now():
            raise ValueError("A data do pedido não pode estar no futuro!")

        return v

    @validator("value")
    def validate_value(cls, v: float, **kwargs) -> float:
        """
        Verifica se o valor do pedido não é menor ou igual a zero.
        """
        if v <= 0.0:
            raise ValueError(
                "Valor do pedido não pode ser menor ou igual a zero!"
            )

        return v
