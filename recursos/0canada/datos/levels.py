# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        8,
        _('Provinces'),
        ['lineasDepto'],
        [],
[
    (_('Yukon'), _('Is northwest')),
    (_('British Columbia'), _('Is west')),
    (_('Alberta'), _('Is southwest')),
    (_('Saskatchewan'), _('Is southwest')),
    (_('Manitoba'), _('Is south')),
    (_('Ontario'), _('Is southeast')),
    (_('Québec'), _('Is southeast')),
    (_('Newfoundland'), _('Is east')),
    (_('New Brunswick'), _('Is southeast')),
    (_('Northwest Territories'), _('Is northwest')),
    (_('Nova Scotia'), _('Is southeast'))
]
]

LEVEL2 = [
        2,
        _('Provincial capitals'),
        ['lineasDepto', 'capitales'],
        [],
[
    (_('Ottawa'), _('Is southeast')),
    (_('Charlottetown'), _('Is southeast')),
    (_('Edmonton'), _('Is southwest')),
    (_('Fredericton'), _('Is southeast')),
    (_('Halifax'), _('Is southeast')),
    (_('Québec'), _('Is southeast')),
    (_('Regina'), _('Is southwest')),
    (_("Saint John's"), _('Is east')),
    (_('Toronto'), _('Is southeast')),
    (_('Victoria'), _('Is southwest')),
    (_('Whitehorse'), _('Is northwest')),
    (_('Winnipeg'), _('Is south')),
    (_('Yellowknife'), _('Is northwest'))
]
]

LEVEL3 = [
        2,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('Ottawa'), _('Is southeast')),
    (_('Charlottetown'), _('Is southeast')),
    (_('Edmonton'), _('Is southwest')),
    (_('Fredericton'), _('Is southeast')),
    (_('Halifax'), _('Is southeast')),
    (_('Québec'), _('Is southeast')),
    (_('Regina'), _('Is southwest')),
    (_("Saint John's"), _('Is east')),
    (_('Toronto'), _('Is southeast')),
    (_('Victoria'), _('Is southwest')),
    (_('Whitehorse'), _('Is northwest')),
    (_('Winnipeg'), _('Is south')),
    (_('Yellowknife'), _('Is northwest')),
    (_('Alert'), _('Is north')),
    (_('Calgary'), _('Is southwest')),
    (_('Cambridge Bay'), _('Is north')),
    (_('Chibougamau'), _('Is southeast')),
    (_('Chisasibi'), _('Is southeast')),
    (_('Churchill'), _('Is in the center')),
    (_('Dawson'), _('Is northwest')),
    (_('Echo Bay'), _('Is northwest')),
    (_('Fort Smith'), _('Is west')),
    (_('Frobisher Bay'), _('Is northeast')),
    (_('Gander'), _('Is east')),
    (_('Goose Bay'), _('Is east')),
    (_('Hamilton'), _('Is southeast')),
    (_('Hay River'), _('Is west')),
    (_('Inuvik'), _('Is northwest')),
    (_('Lethbridge'), _('Is southwest')),
    (_('Montreal'), _('Is southeast')),
    (_('Moosonee'), _('Is southeast')),
    (_('Prince George'), _('Is west')),
    (_('Prince Rupert'), _('Is west')),
    (_('Rankin Inlet'), _('Is in the center')),
    (_('Resolute'), _('Is north')),
    (_('Saskatoon'), _('Is southwest')),
    (_('Schefferville'), _('Is east')),
    (_('Sudbury'), _('Is southeast')),
    (_('Sydney'), _('Is southeast')),
    (_('Thunder Bay'), _('Is south')),
    (_('Vancouver'), _('Is southwest')),
    (_('Watson Lake'), _('Is west')),
    (_('Windsor'), _('Is south'))
]
]

LEVEL4 = [
        4,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Yukon River'), _('Is northwest')),
    (_('Mackenzie River'), _('Is northwest')),
    (_('Saskatchewan River'), _('Is southwest')),
    (_('Nelson River'), _('Is south')),
    (_('Columbia River'), _('Is southwest')),
    (_('Lake Great Bear'), _('Is northwest')),
    (_('Lake Great Slave'), _('Is northwest')),
    (_('Lake Athabasca'), _('Is west')),
    (_('Lake Reindeer'), _('Is southwest')),
    (_('St. Lawrence River'), _('Is southeast')),
    (_('Lake Superior'), _('Is south')),
    (_('Lake Michigan'), _('Is south')),
    (_('Lake Huron'), _('Is southeast')),
    (_('Lake Erie'), _('Is southeast')),
    (_('Lake Ontario'), _('Is southeast')),
    (_('Lake Winnipeg'), _('Is south')),
    (_('Atlantic Ocean'), _('Is southeast')),
    (_('Pacific Ocean'), _('Is west')),
    (_('Beaufort Sea'), _('Is northwest')),
    (_('Chukchi Sea'), _('Is northwest')),
    (_('Greenland Sea'), _('Is northeast')),
    (_('Labrador Sea'), _('Is northeast')),
    (_('Baffin Bay'), _('Is northeast')),
    (_('Hudson Bay'), _('Is in the center')),
    (_('Arctic Ocean'), _('Is north')),
    (_('Norwegian Sea'), _('Is northeast'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

