from datetime import date, datetime
from pyarabic import araby, number
from ummalqura.hijri_date import HijriDate
from . import jalali


class Number:
    """
    A class for numbers in Arabic
    """

    def __init__(self):
        self.c_list = {
            '+': 'زائِدُ',
            '-': 'ناقِصُ',
            '*': 'ضَربٌ في',
            '/': 'تَقسیمٌ عَلَی'
        }

        self.n_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

    @staticmethod
    def __number2text(num):
        arabic_num = number.number2text(num)
        arabic_num = u" ".join(number.vocalize_number(araby.tokenize(arabic_num)))
        return arabic_num

    @staticmethod
    def __is_kabise(year):
        if year > 0:
            return (year - ((year//4)*4)) == 3
        return False

    def __math_tokenizer(self, text: str):
        token_list = []
        i = 0
        length = len(text)
        while i < length:
            if text[i] in self.c_list:
                if (i == 0) or (text[i - 1] in self.c_list):
                    if text[i] in ['+', '-']:
                        token_list.append('0')
                        token_list.append(text[i])
                    else:
                        token_list.append('1')
                        token_list.append(text[i])
                i += 1
            elif text[i] in self.n_list:
                token_list.append(text[i])
                i += 1
                while i < length:
                    if text[i] in self.n_list:
                        num = token_list[-1] + text[i]
                        token_list[-1] = num
                        i += 1
                    elif text[i] in self.c_list:
                        if i + 1 == length or i == length:
                            if text[i] in ['+', '-']:
                                token_list.append(text[i])
                                token_list.append('0')
                            else:
                                token_list.append(text[i])
                                token_list.append('1')
                        else:
                            token_list.append(text[i])
                        i += 1
                        break
            else:
                i += 1
        return token_list

    def __math2arabic(self, math_str: str):
        math_list = self.__math_tokenizer(math_str)
        arabic_str = ""
        for value in math_list:
            if value in self.c_list:
                arabic_str += ' ' + self.c_list.get(value) + ' '
            else:
                arabic_str += self.__number2text(value)
        return arabic_str

    def arabic_calculator(self, math_str: str) -> dict:
        """
        Arabic Calculator
            Convert math string to arabic words

        Example:
            >>> arabic_calculator("25.25/101")
            {
                'status': True,
                'result': {
                    'math': '25.25',
                    'math_eval': 25.25,
                    'arabic': 'خَمْسٌ وَ عِشْرُونَ فَاصلة خَمْسٌ وَ عِشْرُونَ',
                    'arabic_eval': 'خَمْسٌ وَ عِشْرُونَ فَاصلة خَمْسٌ وَ عِشْرُونَ'
                }
            }

        :param math_str: Math string to get be eval()
        :type math_str: str

        :return: A dictionary with keys (math, math_eval, arabic, arabic_eval)
        :rtype: dict

        :raises: Raise error codes: 101, 111
        """

        for i in math_str:
            if i not in list(self.c_list) + self.n_list:
                response = {
                    "status": False,
                    "result": {
                        "error": 101,
                        "math": math_str
                    }
                }
                return response

        if math_str == "":
            math_str = "0"
            math_eval = 0
            response = {
                "status": True,
                "result": {
                    "math": math_str,
                    "math_eval": math_eval,
                    "arabic": self.__math2arabic(math_str),
                    "arabic_eval": self.__number2text(math_eval)
                }
            }
            return response
        else:
            try:
                math_eval = round(eval("".join(self.__math_tokenizer(math_str))), 2)
                if 0 <= math_eval:
                    response = {
                        "status": True,
                        "result": {
                            "math": "".join(self.__math_tokenizer(math_str)),
                            "math_eval": math_eval,
                            "arabic": self.__math2arabic("".join(self.__math_tokenizer(math_str))),
                            "arabic_eval": self.__number2text(math_eval)
                        }
                    }
                else:
                    response = {
                        "status": False,
                        "result": {
                            "error": 111,
                            "math": "".join(self.__math_tokenizer(math_str))
                        }
                    }
            except:
                response = {
                    "status": False,
                    "result": {
                        "error": 101,
                        "math": "".join(self.__math_tokenizer(math_str))
                    }
                }
            return response

    def number_to_arabic(self, num: str) -> dict:
        """
        Convert Positive Integer Number To Arabic
            Convert integer number to arabic words

        Example:
            >>> number_to_arabic("523.25")
            {
                'status': True,
                'result': {
                    'number': '523',
                    'arabic': 'خَمْسُمِئَةٍ وَ ثَلاثٌ وَ عِشْرُونَ'
                }
            }

        :param num: Integer number to get be arabic words
        :type num: str

        :return: A dictionary with keys (number, arabic)
        :rtype: dict

        :raises: Raise error codes: 101, 111
        """

        for i in num:
            if i not in self.n_list:
                response = {
                    "status": False,
                    "result": {
                        "error": 101,
                        "number": num,
                    }
                }
                return response

        if 0 <= int(float(num)):
            arabic = self.__number2text(int(float(num)))
            response = {
                "status": True,
                "result": {
                    "number": int(float(num)),
                    "arabic": arabic
                }
            }
            return response
        else:
            response = {
                "status": False,
                "result": {
                    "error": 111,
                    "number": num,
                }
            }
            return response

    def clock(self, hour: int, minute: int, mode: bool) -> dict:
        """
        Arabic Clock
            Convert clock to arabic words

        Example:
            >>> clock(hour=12, minute=30, mode=False)
            {
                'status': True,
                'result': {
                    'hour': 12,
                    'minute': 30,
                    'mode': False,
                    'arabic_clock': 'السَّاعَةُ الثْانیَةُ عَشْرَةُ وَ النِّصْفُ مَساعاً'
                }
            }

        :param hour: Hour number between 1 to 12
        :type hour: int
        :param minute: Minute number between 0 to 60
        :type minute: int
        :param mode: Clock mode (a.m: True, p.m: False)
        :type mode: bool

        :return: A dictionary with keys (hour, minute, mode, arabic_clock)
        :rtype: dict

        :raises: Raise error codes: 112, 113
        """
        arabic_hour = "السَّاعَةُ "
        arabic_minute = ""
        hour_data = {
            1: "الْوَاحِدَةُ",
            2: "الثّانیَةُ",
            3: "الثّالِثَةُ",
            4: "الرّابِعَةُ",
            5: "الْخامِسَةُ",
            6: "السّادِسَةُ",
            7: "السّابِعَةُ",
            8: "الثّامِنَةُ",
            9: "التّاسِعَةُ",
            10: "الْعاشِرَةُ",
            11: "الْحادیَةُ عَشْرَةُ",
            12: "الثْانیَةُ عَشْرَةُ"
        }

        if hour not in hour_data:
            response = {
                "status": False,
                "result": {
                    "error": 112,
                    "hour": hour,
                    "minute": minute,
                    "mode": mode
                }
            }
            return response
        elif minute < 0 or 60 <= minute:
            response = {
                "status": False,
                "result": {
                    "error": 113,
                    "hour": hour,
                    "minute": minute,
                    "mode": mode
                }
            }
            return response
        else:
            if hour in hour_data:
                arabic_hour += hour_data.get(hour)

            if 0 <= minute < 60:
                if minute == 0:
                    arabic_minute = "تَماماً"
                elif minute == 15:
                    arabic_minute = "وَ الرُّبْعُ"
                elif minute == 30:
                    arabic_minute = "وَ النِّصْفُ"
                elif minute == 45:
                    arabic_minute = "إِلّا رُبْعاً"
                elif minute == 1:
                    arabic_minute = "وَ دَقیقَةٌ"
                elif minute == 2:
                    arabic_minute = "وَ دَقیقَتانِ"
                else:
                    arabic_minute = "وَ " + self.__number2text(str(minute)) + " "
                    if 3 <= minute <= 10:
                        arabic_minute += "دَقائِق"
                    else:
                        arabic_minute += "دَقیقَةً"

            arabic_mode = "صَباحاً" if mode else "مَساعاً"
            response = {
                "status": True,
                "result": {
                    "hour": f"{hour:02d}",
                    "minute": f"{minute:02d}",
                    "mode": mode,
                    "arabic_clock": arabic_hour + " " + arabic_minute + " " + arabic_mode,
                }
            }
            return response

    def jalali2hijri(self, jalali_year, jalali_month, jalali_day):
        """
        Jalali To Hijri Converter
            Convert Jalali Date to Hijri Ghamari Date

        Example:
            >>> jalali2hijri(jalali_year=1399, jalali_month=12, jalali_day=30)
            {   
                'status': True
                'result': {
                    'jalali_year': 1399, 
                    'jalali_month': 12, 
                    'jalali_day': 30, 
                    'jalali_week_day_string' : 'شنبه',
                    'hijri_year': 1442, 
                    'hijri_month': 8, 
                    'hijri_day': 7, 
                    'hijri_month_string': 'شعبان', 
                    'week_day_string': 'اَلسَّبْت'
                    'season': 4, 
                    'season_string': 'اَلشِّتاء', 
                }, 
            }

        :param jalali_year: Jalali Year number
        :type jalali_year: int
        :param jalali_month: Jalali Month number
        :type jalali_month: int
        :param jalali_day: Jalali Day number
        :type jalali_day: int

        :return: A dictionary with keys (
            jalali_year, 
            jalali_month, 
            jalali_day, 
            hijri_year, 
            hijri_month, 
            hijri_day, 
            hijri_month_string, 
            week_day_string, 
            season, 
            season_string
        )
        :rtype: dict

        :raises: Raise error codes: 101
        """
        hijri_day_string_dict = {
            'السبت': 'اَلسَّبْت',
            'الاحد': 'اَلْأَحَد',
            'الاثنين': 'اَلْإِثْنَینِ',
            'الثلاثاء': 'اَلثُّلاثاء',
            'الاربعاء': 'اَلْأَربِعاء',
            'الخميس': 'اَلْخَميس',
            'الجمعة': 'اَلْجُمُعَة',
        }
        week_pair = {
            'اَلسَّبْت' : 'شنبه',
            'اَلْأَحَد' : 'یکشنبه',
            'اَلْإِثْنَینِ' : 'دوشنبه',
            'اَلثُّلاثاء' : 'سه شنبه',
            'اَلْأَربِعاء' : 'چهارشنبه',
            'اَلْخَميس' : 'پنجشنبه',
            'اَلْجُمُعَة' : 'جمعه',
        }
        try:
            if jalali_month == 12 and jalali_day >= 30:
                if self.__is_kabise(jalali_year) == False:
                    response = {
                        'status': False,
                        'result':{
                            "error": 101,
                            'jalali_year': jalali_year,
                            'jalali_month': jalali_month,
                            'jalali_day': jalali_day,
                        }
                    }
                    return response
            year, month, day = jalali.Persian((jalali_year, jalali_month, jalali_day)).gregorian_tuple() # jalali to gregorian
            hijri = HijriDate(year, month, day, gr=True) # gregorian to hijri
            
            if 1 <= jalali_month <= 3:
                season = 1
                season_string = "اَلرَّبيع"
            elif 4 <= jalali_month <= 6:
                season = 2
                season_string = "اَلصَّيْف"
            elif 7 <= jalali_month <= 9:
                season = 3
                season_string = "الْخَریف"
            else:
                season = 4
                season_string = "اَلشِّتاء"
            
            response = {
                'status': True,
                'result':{
                    'jalali_year': f"{jalali_year:04d}",
                    'jalali_month': f"{jalali_month:02d}",
                    'jalali_day': f"{jalali_day:02d}",
                    'jalali_week_day_string': week_pair[hijri_day_string_dict.get(hijri.day_name)],
                    'hijri_year': f"{hijri.year:04d}",
                    'hijri_month': f"{hijri.month:02d}",
                    'hijri_day': f"{hijri.day:02d}",
                    'hijri_month_string': hijri.month_name,
                    'week_day_string': hijri_day_string_dict.get(hijri.day_name), 
                    'season': season,
                    'season_string': season_string
                }
            }
        except Exception as e:
            print(e)
            response = {
                'status': False,
                'result':{
                    "error": 101,
                    'jalali_year': jalali_year,
                    'jalali_month': jalali_month,
                    'jalali_day': jalali_day,
                }
            }
        return response


local_number = Number()
arabic_calculator = local_number.arabic_calculator
number_to_arabic = local_number.number_to_arabic
clock = local_number.clock
jalali2hijri = local_number.jalali2hijri