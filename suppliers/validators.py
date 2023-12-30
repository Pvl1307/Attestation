from rest_framework.exceptions import ValidationError


def forbidden_change_debt(new_debt, old_debt):
    """ Запрет на изменение поля 'задолженность перед поставщиком' """
    if old_debt is not None and old_debt != new_debt:
        raise ValidationError("Изменение поля 'Задолженность перед поставщиком' запрещено!")
