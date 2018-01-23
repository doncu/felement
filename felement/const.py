import enum


class Resistance(enum.IntEnum):
    bad = 0
    average = 1
    good = 2


class Availability(enum.IntEnum):
    default = 0
    available = 1
    on_request = 2


Resistance_TEXT = {
    Resistance.bad: 'плохо',
    Resistance.average: 'средне',
    Resistance.good: 'хорошо',
}


Availability_TEXT = {
    Availability.available: 'x',
    Availability.on_request: '0',
    Resistance.good: '',
}
