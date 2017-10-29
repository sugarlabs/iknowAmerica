# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Chile')

STATES = [
    (_('Tarapacá'), 254, 165, 151, 0),
    (_('Antofagasta'), 253, 209, 298, 0),
    (_('Atacama'), 252, 167, 470, 0),
    (_('Coquimbo'), 251, 134, 604, 0),
    (_('Valparaíso'), 250, 140, 683, 0),
    (_('Metropolitana'), 249, 154, 728, 0),
    (_("Libertador General Bernardo O'Higgins"), 248, 158, 768, 0),
    (_('Maule'), 247, 118, 824, 0),
    (_('Bío-Bío'), 246, 510, 57, 0),
    (_('La Araucanía'), 245, 511, 133, 0),
    (_('Los Lagos'), 244, 496, 283, 0),
    (_('Aysén'), 243, 553, 481, 0),
    (_('Magallanes'), 242, 513, 699, 0),
    (_('Arica Parinacota'), 241, 185, 81, 0),
    (_('Los Rios'), 240, 505, 188, 0),
    (_('Argentina'), 239, 667, 163, 90),
    (_('Perú'), 238, 152, 25, 0)
]

CAPITALS = [
    (_('Santiago'), 151, 720, 0, 0, 14),
    (_('Iquique'), 171, 138, 1, 0, 14),
    (_('Antofagasta'), 157, 297, 1, 0, 14),
    (_('Copiapó'), 166, 451, 1, 0, 14),
    (_('La Serena'), 126, 569, 1, 0, 14),
    (_('Valparaíso'), 117, 704, 1, 0, -14),
    (_('Rancagua'), 138, 757, 1, 0, 14),
    (_('Talca'), 116, 805, 1, 0, 14),
    (_('Concepción'), 486, 39, 1, 0, 14),
    (_('Temuco'), 506, 140, 1, 0, 14),
    (_('Puerto Montt'), 498, 247, 1, 0, 14),
    (_('Coihaique'), 538, 423, 1, 0, 14),
    (_('Punta Arenas'), 559, 763, 1, 0, 14),
    (_('Arica'), 162, 71, 1, 0, 14),
    (_('Valdivia'), 482, 182, 1, 0, 14)
]

STATS = [
    (_('Capital:'), _('Santiago') + _("(33º26' S - 70º39' W)")),
    (_('Language:'), _('Spanish')),
    (_('Government:'), _('Presidential republic')),
    (_('President:'), _('Michelle Bachelet Jeria')),
    (_('Independence:'), _('from Spain')),
    ('', _('declared: %s') % _('February 12, 1818')),
    ('', _('recognized: %s') % _('February 24, 1844')),
    (_('Area:'), '%(sup)s %(u)s (%(p)s)' % {'sup': _('756.096'), 'u': _('km²'), 'p': _('38th')}),
    (_('Population:'), '%(v)s (%(p)s)' % {'v': _('18.006.407'), 'p': _('62nd')}),
    (_('GDP:'), '%(c)s %(v)s %(u)s (%(p)s)' % {'c': _('USD'), 'v': _('410.277'), 'u': _('billion'), 'p': _('42nd')}),
    (_('HDI:'), '%(l)s - %(v)s (%(p)s)' % {'l': _('Very High'), 'v': _('0,832'), 'p': _('42th')}),
    (_('Currency:'), _('Peso')),
    (_('Updated:'), _('April 5, 2016'))
]


