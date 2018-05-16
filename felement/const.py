import enum


class Resistance(enum.IntEnum):
    bad = 0
    average = 1
    good = 2
    excellent = 3


class Availability(enum.IntEnum):
    default = 0
    available = 1
    on_request = 2


Resistance_TEXT = {
    Resistance.bad: '&#183;' * 2,
    Resistance.average: '&#183;' * 3,
    Resistance.good: '&#183;' * 4,
    Resistance.excellent: '&#183;' * 5,
}


Availability_TEXT = {
    Availability.available: 'x',
    Availability.on_request: '0',
    Resistance.good: '',
}
