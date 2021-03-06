class Rakutan:
    lecID = None
    facultyName = None
    lectureName = None
    groups = None
    credits = None
    accepted = []
    total = []
    url = None

    def __init__(self, lecID, fN, lN, g, c, a, t, u):
        self.lecID: int = lecID
        self.facultyName: str = fN
        self.lectureName: str = lN
        self.groups: str = g
        self.credits: int = c
        self.accepted: list = a
        self.total: list = t
        self.url: str = u

    @classmethod
    def from_dict(cls, dbRakutanDict: dict):
        return Rakutan(
            lecID=dbRakutanDict['id'],
            fN=dbRakutanDict['facultyname'],
            lN=dbRakutanDict['lecturename'],
            g=dbRakutanDict['groups'],
            c=dbRakutanDict['credits'],
            a=[dbRakutanDict['accept_prev'], dbRakutanDict['accept_prev2'], dbRakutanDict['accept_prev3']],
            t=[dbRakutanDict['total_prev'], dbRakutanDict['total_prev2'], dbRakutanDict['total_prev3']],
            u=dbRakutanDict['url']
        )

    @classmethod
    def from_list(cls, dbRakutanList: list):
        rakutanList = []
        for rakutan in dbRakutanList:
            rakutanList.append(cls.from_dict(rakutan))
        return rakutanList

    def to_dict(self):
        return {
            'lecID': self.lecID,
            'facultyName': self.facultyName,
            'lectureName': self.lectureName,
            'groups': self.groups,
            'credits': self.credits,
            'accepted': self.accepted,
            'total': self.total,
            'url': self.url
        }
