# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        _('Departments'),
        ['lineasDepto'],
        [],
[
    (_('Norte'), _('Is northeast')),
    (_('Noroeste'), _('Is north')),
    (_('Noreste'), _('Is northeast')),
    (_('Artibonite'), _('Is northeast')),
    (_('Oeste'), _('Is southeast')),
    (_('Sur'), _('Is southwest')),
    (_('Sudeste'), _('Is southeast')),
    (_("Grand'Anse"), _('Is southwest')),
    (_('Centro'), _('Is east'))
]
]

LEVEL2 = [
        _('Departmental capitals'),
        ['lineasDepto', 'capitales'],
        [],
[
    (_('Port-au-Prince'), _('Is southeast')),
    (_('Cap Haitien'), _('Is northeast')),
    (_('Fort Liberte'), _('Is northeast')),
    (_('Gonaives'), _('Is north')),
    (_('Hinche'), _('Is east')),
    (_('Jacmel'), _('Is south')),
    (_('Jeremie'), _('Is southwest')),
    (_('Les Cayes'), _('Is southwest')),
    (_('Port de Paix'), _('Is north'))
]
]

LEVEL3 = [
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (_('Port-au-Prince'), _('Is southeast')),
    (_('Cap Haitien'), _('Is northeast')),
    (_('Fort Liberte'), _('Is northeast')),
    (_('Gonaives'), _('Is north')),
    (_('Hinche'), _('Is east')),
    (_('Jacmel'), _('Is south')),
    (_('Jeremie'), _('Is southwest')),
    (_('Les Cayes'), _('Is southwest')),
    (_('Port de Paix'), _('Is north')),
    (_('Anse a Galets'), _('Is in the center')),
    (_("Anse d'Hainault"), _('Is southwest')),
    (_('Aquin'), _('Is southwest')),
    (_('Baie de Henne'), _('Is northwest')),
    (_('Bainet'), _('Is south')),
    (_('Belle Anse'), _('Is southeast')),
    (_('Cotes de Fer'), _('Is south')),
    (_('Croix des Bouquets'), _('Is southeast')),
    (_('Dame Marie'), _('Is southwest')),
    (_('Ennery'), _('Is northeast')),
    (_('Grande Riviere du Nord'), _('Is northeast')),
    (_('Kenscoff'), _('Is southeast')),
    (_('Lafond'), _('Is in the center')),
    (_('Le Borgne'), _('Is north')),
    (_('Leogane'), _('Is south')),
    (_('Les Anglais'), _('Is southwest')),
    (_('Limbé'), _('Is northeast')),
    (_('Manneville'), _('Is southeast')),
    (_('Marigot'), _('Is southeast')),
    (_('Miragoane'), _('Is south')),
    (_('Mirebalais'), _('Is east')),
    (_('Mole Saint Nicolas'), _('Is northwest')),
    (_('Montrouis'), _('Is in the center')),
    (_('Pestel'), _('Is southwest')),
    (_('Petionville'), _('Is southeast')),
    (_('Petit Goave'), _('Is south')),
    (_('Petit Trou de Nippes'), _('Is southwest')),
    (_('Port Salut'), _('Is southwest')),
    (_('Saint Marc'), _('Is in the center')),
    (_('Saint Raphael'), _('Is northeast')),
    (_('Trouin'), _('Is south')),
    (_('Verrettes'), _('Is in the center'))
]
]

LEVEL4 = [
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (_('Les Trois Rivières River'), _('Is north')),
    (_('Artibonito River'), _('Is east')),
    (_('Bouyaha River'), _('Is northeast')),
    (_('Guayamouc River'), _('Is east')),
    (_('Canot River'), _('Is northeast')),
    (_('Artibonite River'), _('Is in the center')),
    (_('Lake of Pélicre'), _('Is east')),
    (_('Lake Étang Saumâtre'), _('Is southeast')),
    (_('Jacmel Bay'), _('Is south')),
    (_('Port au Prince Bay'), _('Is southeast')),
    (_('Canal of Saint Marc'), _('Is in the center')),
    (_('Canal of the Gonâve'), _('Is southwest')),
    (_('Henne Bay'), _('Is northwest')),
    (_('Tortue Bay'), _('Is north')),
    (_('Grand Pierre Bay'), _('Is in the center')),
    (_('Mancenille Bay'), _('Is northeast')),
    (_('Canal of the Tortue'), _('Is north')),
    (_('Gulf of the Gonâve'), _('Is northwest')),
    (_('Windward Passage'), _('Is northwest')),
    (_('Caribbean Sea'), _('Is south')),
    (_('Atlantic Ocean'), _('Is north'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

