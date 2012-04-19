# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Costa Rica')

STATES = [
    (_('Guanacaste'), 254, 148, 324, 0),
    (_('Alajuela'), 253, 324, 281, 0),
    (_('Heredia'), 252, 447, 318, 90),
    (_('San José'), 251, 459, 521, -45),
    (_('Cartago'), 250, 517, 470, 0),
    (_('Limón'), 249, 636, 505, 0),
    (_('Puntarenas'), 248, 622, 661, 0),
    (_('Nicaragua'), 247, 357, 95, 0),
    (_('Panamá'), 246, 757, 665, 90)
]

CAPITALS = [
    (_('San José'), 432, 441, 0, -20, 14),
    (_('Alajuela'), 403, 422, 1, -48, 0),
    (_('Cartago'), 468, 459, 1, 40, 7),
    (_('Heredia'), 426, 426, 1, 20, -14),
    (_('Liberia'), 135, 285, 1, 35, 0),
    (_('Puerto Limón'), 661, 430, 1, 50, -14),
    (_('Puntarenas'), 268, 432, 1, -40, -14)
]

CITIES = [
    (_('Bagaces'), 176, 312, 2, -15, 14),
    (_('Bomba'), 656, 446, 2, 40, 0),
    (_('Boruca'), 602, 650, 2, -10, 14),
    (_('Bratsi'), 689, 534, 2, 0, 14),
    (_('Buena Vista'), 524, 538, 2, 15, -14),
    (_('Buenos Aires'), 598, 612, 2, 30, -14),
    (_('Caño Negro'), 279, 224, 2, 60, 0),
    (_('Cabuya'), 210, 513, 2, 0, 14),
    (_('Cahuita'), 703, 486, 2, 20, -14),
    (_('Canas'), 209, 330, 2, -10, 14),
    (_('Cariblanco'), 411, 366, 2, 0, -14),
    (_('Carmona'), 175, 430, 2, 30, 14),
    (_('Castilla'), 140, 265, 2, 0, -14),
    (_('Chaparrón'), 407, 299, 2, 45, 0),
    (_('Cocles'), 726, 509, 2, 20, 14),
    (_('Colorado'), 540, 248, 2, 0, -14),
    (_('Corina'), 601, 427, 2, 5, 14),
    (_('Coronado'), 536, 639, 2, -55, 0),
    (_('Cuajiniquil'), 83, 217, 2, 0, 14),
    (_('Delta del San Juan'), 505, 258, 2, 60, 14),
    (_('Dominical'), 482, 591, 2, -50, 7),
    (_('Drake'), 535, 710, 2, -40, 0),
    (_('Esparza'), 305, 431, 2, 10, 14),
    (_('Filadelfia'), 108, 328, 2, 15, 14),
    (_('Frailes'), 437, 482, 2, 40, 0),
    (_('Garza'), 90, 455, 2, -15, 14),
    (_('Golfito'), 639, 729, 2, -40, 0),
    (_('Guacimo'), 509, 380, 2, 45, 0),
    (_('Guapiles'), 496, 377, 2, 0, -14),
    (_('Guatuzo'), 271, 274, 2, 45, 0),
    (_('Guayabos'), 180, 265, 2, 45, -7),
    (_('Hacienda Porvenir'), 471, 272, 2, -60, -14),
    (_('Hacienda Trancas'), 99, 299, 2, -15, 14),
    (_('Hatillo'), 473, 582, 2, -40, -7),
    (_('Herradura'), 535, 545, 2, 45, 0),
    (_('Hojancha'), 139, 414, 2, -20, 14),
    (_('Jaco'), 313, 511, 2, -20, 14),
    (_('La Cruz'), 92, 188, 2, -35, -14),
    (_('Lapita'), 249, 388, 2, -10, 14),
    (_('Limonal'), 228, 373, 2, 0, -14),
    (_('Los Chiles'), 292, 198, 2, 0, -14),
    (_('Mal País'), 200, 510, 2, -30, -14),
    (_('Matina'), 595, 407, 2, 15, -14),
    (_('Mesas'), 539, 605, 2, 0, 14),
    (_('Naranjo'), 365, 387, 2, 40, 0),
    (_('Neily'), 683, 728, 2, 40, 0),
    (_('Nicoya'), 131, 392, 2, 35, 0),
    (_('Pandora'), 678, 485, 2, -45, 0),
    (_('Paquera'), 245, 467, 2, 0, -14),
    (_('Paraiso'), 55, 389, 2, -15, 14),
    (_('Piedras Blancas'), 620, 698, 2, -40, -14),
    (_('Pilas'), 575, 631, 2, 0, 14),
    (_('Pital'), 389, 325, 2, 0, 14),
    (_('Platanal'), 345, 333, 2, -25, -14),
    (_('Portegolpe'), 70, 346, 2, -20, -14),
    (_('Puerto Cortés'), 555, 659, 2, -65, 0),
    (_('Puerto Culebra'), 90, 279, 2, -20, -14),
    (_('Puerto Jimenez'), 602, 758, 2, 0, 14),
    (_('Puerto Quepos'), 417, 555, 2, -70, 0),
    (_('Puerto Soley'), 88, 194, 2, -30, 10),
    (_('Puerto Viejo'), 450, 326, 2, 30, 14),
    (_('Puriscal'), 374, 467, 2, 0, 14),
    (_('Quesada'), 356, 354, 2, -45, 0),
    (_('Quina'), 337, 519, 2, 0, 14),
    (_('Sabanilla'), 661, 683, 2, 25, -14),
    (_('San Francisco'), 175, 470, 2, -20, -14),
    (_('San Isidro'), 513, 568, 2, -25, -14),
    (_('San José'), 203, 208, 2, 0, -14),
    (_('San Marcos'), 447, 505, 2, -25, 14),
    (_('San Pedro'), 550, 586, 2, 28, -14),
    (_('San Ramón'), 350, 409, 2, -30, -14),
    (_('San Vito'), 680, 691, 2, 45, 0),
    (_('Santa Cruz'), 100, 367, 2, 45, 0),
    (_('Santa Teresa'), 352, 303, 2, -20, -14),
    (_('Siquirres'), 558, 403, 2, -10, 14),
    (_('Sirena'), 554, 754, 2, -20, -14),
    (_('Santa Cecilia'), 140, 179, 2, 20, -14),
    (_('Suerre'), 583, 362, 2, 0, -14),
    (_('Tambor'), 224, 489, 2, 20, 14),
    (_('Tarcoles'), 316, 478, 2, 0, 14),
    (_('Tenorio'), 213, 287, 2, 15, 14),
    (_('Terraba'), 609, 635, 2, 35, 0),
    (_('Tilaran'), 238, 324, 2, 20, 14),
    (_('Tortuguero'), 555, 296, 2, 15, 14),
    (_('Tres de Junio'), 483, 500, 2, 55, 0),
    (_('Turrialba'), 519, 447, 2, 0, -14),
    (_('Uatsi'), 700, 511, 2, -30, 0),
    (_('Unión'), 660, 739, 2, 0, 14),
    (_('Upala'), 227, 225, 2, 0, 14),
    (_('Uvita'), 507, 615, 2, -38, 0),
    (_('Vueltas'), 635, 657, 2, 35, 0),
    (_('Zarcero'), 357, 375, 2, -45, 0)
]

RIVERS = [
    (_('San Juan River'), 254, 343, 213, -30),
    (_('San Carlos River'), 253, 329, 296, 30),
    (_('Frio River'), 252, 296, 250, 50),
    (_('Tempisque River'), 251, 123, 354, -40),
    (_('Sixaola River'), 250, 671, 513, 0),
    (_('Pirris River'), 249, 409, 529, 30),
    (_('Reventazón River'), 248, 538, 409, 60),
    (_('Chirripó River'), 247, 504, 305, 50),
    (_('General River'), 246, 572, 603, -35),
    (_('Grande of Terraba River'), 245, 599, 671, -10),
    (_('Corobicí River'), 244, 186, 321, 70),
    (_('Savegre River'), 243, 474, 556, 40),
    (_('Gulf of Papagayo'), 242, 25, 249, 90),
    (_('Gulf of Nicoya'), 241, 259, 511, 45),
    (_('Coronado Bay'), 240, 398, 613, -40),
    (_('Dulce Gulf'), 239, 635, 825, -40),
    (_('Caribbean Sea'), 238, 647, 173, 0),
    (_('Pacific Ocean'), 237, 226, 704, 0)
]

ROUTES = []

STATS = [
    (_('Capital:'), _('San José') + _("(9º56'N - 84º5'W)")),
    (_('Language:'), _('Spanish')),
    (_('Government:'), _('Presidential republic')),
    (_('President:'), _('Laura Chinchilla Miranda')),
    (_('Vice President:'), _('Alfio Piva Mesén')),
    ('', _('Luis Liberman Ginsburg')),
    (_('Independence:'), _('from Spain')),
    ('', _('15 of september of 1821')),
    (_('Area:'), _('51.100 km² (129th)')),
    (_('Population:'), _('4.615.518 (115th)')),
    (_('GDP:'), _('USD 52.885 billion (84th)')),
    (_('HDI:'), _('High - 0,725 (62th)')),
    (_('Currency:'), _('Costa Rica Colon'))
]


