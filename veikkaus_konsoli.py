

# class LuoOttelu:
#
#     def __init__(self, ottelupari):
#         self.ottelupari = ottelupari
#
#     class Inner:
#
#         def __init__(self, pvm, klo):
#             self.pvm = pvm
#             self.klo = klo
#             self.tulos_koti = None
#             self.tulos_vieras = None
#             self.tulos_yksiristikaksi = None
#             self.pelattu = False
#
#         def lisaa_tulos(self, tulos_koti, tulos_vieras):
#             self.tulos_koti = tulos_koti
#             self.tulos_vieras = tulos_vieras
#             self.pelattu = True
#
#         def yksiristikaksi(self):
#             if self.tulos_koti > self.tulos_vieras:
#                 self.tulos_yksiristikaksi = "1"
#             elif self.tulos_vieras > self.tulos_koti:
#                 self.tulos_yksiristikaksi = "2"
#             else:
#                 self.tulos_yksiristikaksi = "x"
#
#
# ottelutiedot = LuoOttelu("rus-sau")


Ottelutiedot = {
    "ottelupari": {
        "rus-sau": {
            "pvm": "16.7",
            "klo": "14.00",
            "tulos": "0-2",
            "yksiristikaksi": None,
            "pelattu": False
        },
        "egt-uru": {
            "pvm": "16.7",
            "klo": "17.00",
            "tulos": "1-0",
            "yksiristikaksi": None,
            "pelattu": False
        },
        "mor-ira": {
            "pvm": "16.7",
            "klo": "20.00",
            "tulos": None,
            "yksiristikaksi": None,
            "pelattu": False
            }
    }
}

Osallistujat = {
        "Jani": {
            "ottelupari":   {
                    "rus-sau":  {
                        "veikkaus": "1-2"
                                },
                    "egt-uru":  {
                        "veikkaus": "1-0"
                                },
                    "mor-ira":  {
                        "veikkaus": "1-1"
                                }
                            },
            "pisteet": 0
                },

        "Matti": {
            "ottelupari":   {
                    "rus-sau":  {
                        "veikkaus": "0-0"
                                },
                    "egt-uru":  {
                        "veikkaus": "1-2"
                                },
                    "mor-ira":  {
                        "veikkaus": "1-2"
                                }
                            },
            "pisteet": 0
                },
        "Jussi": {
                "ottelupari": {
                    "rus-sau": {
                        "veikkaus": "1-1"
                    },
                    "egt-uru": {
                        "veikkaus": "3-2"
                    },
                    "mor-ira": {
                        "veikkaus": "1-1"
                    }
                },
                "pisteet": 0
            },
                }


def laske_pisteet(Ottelutiedot, Osallistujat):

    for i in range(len(Ottelutiedot["ottelupari"])):
        print(Ottelutiedot["ottelupari"]["tulos"].get("tulos"))


laske_pisteet(Ottelutiedot, Osallistujat)

#SELVITÄ MITEN LUOT ottelutiedot OBJEKTIN JONKA SISÄLLÄ ON MATSIT JONKA SISÄLLÄ ON MATSIN TIEDOT
# Aloita https://www.datacamp.com/community/tutorials/inner-classes-python

#ottelutiedot."rus-sau".Inner("10.6", "17.00")
