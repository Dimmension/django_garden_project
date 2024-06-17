"""Module that provides validators."""
from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.timezone import timezone
from garden_app import consts


def get_datetime() -> datetime:
    """Return current datetime in UTC timezone.

    Returns:
        datetime: Current datetime in UTC timezone.
    """
    return datetime.now(timezone.utc)


def check_date(dt: datetime) -> None:
    """Validate given datetime is not in the future.

    Args:
        dt (datetime): Datetime to validate.

    Raises:
        ValidationError: If the datetime is in the future.
    """
    if dt > get_datetime():
        raise ValidationError(
            'Date and time is bigger than current!',
            params={'created': dt},
        )


def check_positive_height(coord: float) -> None:
    """Validate given coordinate value is positive or zero.

    Args:
        coord (float): Coordinate value to validate.

    Raises:
        ValidationError: If the coordinate value is negative.
    """
    if coord < 0:
        raise ValidationError('Value should be equal or greater than zero')


def check_coords(coord: float) -> None:
    """Validate given coordinate value is within the valid range.

    Args:
        coord (float): Coordinate value to validate.

    Raises:
        ValidationError: If the coordinate value is outside the valid range.
    """
    if coord < consts.MAX_NEGATIVE_DEGREE or coord > consts.MAX_POSITIVE_DEGREE:
        raise ValidationError('Value should be equal or greater than zero')
