class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._arvot = [arvo]

    def miinus(self, operandi):
        self._arvot.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvot.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvot.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvot.append(self._arvo)
        self._arvo = arvo
        
    def kumoa(self):
        if len(self._arvot) > 0:
            self._arvo = self._arvot.pop()

    def arvo(self):
        return self._arvo