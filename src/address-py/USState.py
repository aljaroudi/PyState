from enum import Enum


class USState(Enum):
    AK = 0
    AL = 1
    AR = 2
    AS = 3
    AZ = 4
    CA = 5
    CO = 6
    CT = 7
    DC = 8
    DE = 9
    FL = 10
    GA = 11
    GU = 12
    HI = 13
    IA = 14
    ID = 15
    IL = 16
    IN = 17
    KS = 18
    KY = 19
    LA = 20
    MA = 21
    MD = 22
    ME = 23
    MI = 24
    MN = 25
    MO = 26
    MP = 27
    MS = 28
    MT = 29
    NC = 30
    ND = 31
    NE = 32
    NH = 33
    NJ = 34
    NM = 35
    NV = 36
    NY = 37
    OH = 38
    OK = 39
    OR = 40
    PA = 41
    PR = 42
    RI = 43
    SC = 44
    SD = 45
    TN = 46
    TX = 47
    UM = 48
    UT = 49
    VA = 50
    VI = 51
    VT = 52
    WA = 53
    WI = 54
    WV = 55
    WY = 56

    @property
    def str(self) -> str:
        return \
        ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN',
         'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
         'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA',
         'WI', 'WV', 'WY'][self.value]

    @property
    def str_full(self) -> str:
        return ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois',
                'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
                'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
                'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island',
                'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont',
                'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'][self.value]
