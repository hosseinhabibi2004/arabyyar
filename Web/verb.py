import re
from pyarabic import araby
import libqutrub.conjugator


def split_shadda(word):
    regex = r"(ْ([ضصثقفغعهخحجشسیيبلاتنمکكظطزرذدءو]{1})ّ([َُِ]{1}))"
    matchs = re.findall(regex, word)

    for match in matchs:
        edit = "ْ" + match[1] + match[2] + match[1] + match[2]
        word = word.replace(match[0], edit)
    return word


def arabic_verb(word: str, future_type: int, pronoun: int) -> dict:
    """
        Arabic Verb
            Convert arabic verb to other tenses

        Example:
            >>> arabic_verb(word="کتب", future_type=2, pronoun=8)
            {
                'status': True, 
                'result': {
                    'word': 'كتب', 
                    'future_type': 2, 
                    'pronoun': 8, 
                    'known_past': 'كَتَبْتُم', 
                    'known_present': 'تَكْتُبُونَ', 
                    'imperative': 'اُكْتُبُوا', 
                    'unknown_past': 'كُتِبْتُم', 
                    'unknown_present': 'تُكْتَبُونَ', 
                    'passive_present': 'تَكْتُبُوا', 
                    'participle_present': 'تَكْتُبُوا', 
                    'unknown_passive_present': 'تُكْتَبُوا', 
                    'unknown_participle_present': 'تُكْتَبُوا', 
                }
            }

        :param word: Arabic verb in pronoun 0 (هو)
        :type : str
        :param future_type: The mark of the second letter in base of the verb (0:Fatha, 1:Kasra, 2:Damma)
        :type : int
        :param pronoun: Pronoun number between 0 to 13
        :type : int

        :return: A dictionary with keys (
            word, 
            future_type, 
            pronoun, 
            known_past, 
            known_present, 
            imperative, 
            unknown_past, 
            unknown_present, 
            passive_present, 
            participle_present, 
            unknown_passive_present, 
            unknown_participle_present, 
        )
        :rtype: dict

        :raises: Raise error codes: 101, 102
    """
    verbs_mode = {
        'الماضي المعلوم': 'known_past',
        'المضارع المعلوم': 'known_present',
        'الأمر': 'imperative',
        'الماضي المجهول': 'unknown_past',
        'المضارع المجهول': 'unknown_present',
        'المضارع المجزوم': 'passive_present',
        'المضارع المنصوب': 'participle_present',
        'المضارع المجهول المجزوم': 'unknown_passive_present',
        'المضارع المجهول المنصوب': 'unknown_participle_present',
    }

    future_type_list = {
        0: "فتحة",
        1: "كسرة",
        2: "ضمة"
    }

    pronoun_list = {
        0: 'هو',
        1: 'هما',
        2: 'هم',
        3: 'هي',
        4: 'هما مؤ',
        5: 'هن',
        6: 'أنت',
        7: 'أنتما',
        8: 'أنتم',
        9: 'أنتِ',
        10: 'أنتما مؤ',
        11: 'أنتن',
        12: 'أنا',
        13: 'نحن',
    }

    if not(pronoun in pronoun_list) or not(future_type in future_type_list):
        response = {
            "status": False,
            "result": {
                "error": 101,
                "word": word,
                "future_type": future_type,
                "pronoun": pronoun,
            }
        }
        return response

    word = word.replace('ک', 'ك').replace('ی', 'ي')

    table = libqutrub.conjugator.conjugate(
        word, future_type_list[future_type],
        transitive=True, display_format="DICT"
    )

    if table is None:
        response = {
            "status": False,
            "result": {
                "error": 102,
                "word": word,
                "future_type": future_type,
                "pronoun": pronoun,
            }
        }
        return response

    else:
        response = {
            "status": True,
            "result": {
                "word": word,
                "future_type": future_type,
                "pronoun": pronoun,
            }
        }
        for mode in verbs_mode:
            response['result'][verbs_mode[mode]] = table.get(mode).get(pronoun_list.get(pronoun))
        return response


def process_chapter(base, chapter=0, pronoun=0):
    try:
        pronoun = int(pronoun)
        chapter = int(chapter)
    except:
        response = {
            "status": False,
            "result": {
                "error": 201,
                "base": base,
                "chapter": chapter,
                "pronoun": pronoun,
            }
        }
    
    tense_list = {
        'الماضي المعلوم': 'known_past',
        'المضارع المعلوم': 'known_present',
        'الأمر': 'imperative',
        'الماضي المجهول': 'unknown_past',
        'المضارع المجهول': 'unknown_present',
        'المضارع المجزوم': 'passive_present',
        'المضارع المنصوب': 'participle_present',
        'المضارع المجهول المجزوم': 'unknown_passive_present',
        'المضارع المجهول المنصوب': 'unknown_participle_present',
    }

    pronoun_list = {
        0: 'هو',
        1: 'هما',
        2: 'هم',
        3: 'هي',
        4: 'هما مؤ',
        5: 'هن',
        6: 'أنت',
        7: 'أنتما',
        8: 'أنتم',
        9: 'أنتِ',
        10: 'أنتما مؤ',
        11: 'أنتن',
        12: 'أنا',
        13: 'نحن',
    }

    chapters_list = {
        0: ('إِفْعال', 'أَفعَلَ'),
        1: ('تَفْعيل', 'فَعَّل'),
        2: ('مُفاعَلَة', 'فاعَل'),
        3: ('إِفْتِعال', 'اِفتَعَل'),
        4: ('إِنْفِعال', 'اِنفَعَل'),
        5: ('تَفاعُل', 'تَفاعَل'),
        6: ('تَفَعُّل', 'تَفَعَّل'),
        7: ('إِسْتِفْعال', 'اِستفعلَ'),
    }

    future_type_list = {
        0: "فتحة",
        1: "كسرة",
        2: "ضمة"
    }

    if (len(base) == 3) and (chapter in range(0, 7 + 1)) and (pronoun in range(0, 13 + 1)):
        base = base.replace('ک', 'ك').replace('ی', 'ي')
        word = chapters_list[chapter][1].replace('ف', 'x').replace('ع', 'y').replace('ل', 'z')
        word = word.replace('x', base[0]).replace('y', base[1]).replace('z', base[2])
        
        table = libqutrub.conjugator.conjugate(
            word, future_type_list[0],
            transitive=True, display_format="DICT"
        )
        
        if table is None:
            response = {
                "status": False,
                "result": {
                    "error": 102,
                    "base": base,
                    "chapter": chapter,
                    "pronoun": pronoun,
                }
            }
            return response

        else:
            response = {
                "status": True,
                "result": {
                    "base": base,
                    "chapter": chapter,
                    "pronoun": pronoun,
                }
            }
            for tense in tense_list:
                response['result'][tense_list[tense]] = table.get(tense).get(pronoun_list.get(pronoun))
            return response
    else:
        response = {
            "status": False,
            "result": {
                "error": 101,
                "base": base,
                "chapter": chapter,
                "pronoun": pronoun,
            }
        }
        return response


def reverse_chapter(word):
    word = word.replace('ک', 'ك').replace('ی', 'ي')
    
    tense_list = {
        'الماضي المعلوم': 'ماضی معلوم',
        'المضارع المعلوم': 'مضارع معلوم مرفوع',
        'الأمر': 'امر مخاطب',
        'الماضي المجهول': 'ماضی مجهول',
        'المضارع المجهول': 'مضارع مجهول مرفوع',
        'المضارع المجزوم': 'مضارع معلوم مجزوم',
        'المضارع المنصوب': 'مضارع معلوم منصوب',
        'المضارع المجهول المجزوم': 'مضارع مجهول مجزوم',
        'المضارع المجهول المنصوب': 'مضارع مجهول منصوب',
    }

    pronoun_list = {
        'هو': 'هُوَ',
        'هما': 'هُما',
        'هم': 'هُم',
        'هي': 'هِيَ',
        'هما مؤ': 'هُما مُؤَنَثْ',
        'هن': 'هُنَّ',
        'أنت': 'أَنْتَ',
        'أنتما': 'أَنْتُما',
        'أنتم': 'أَنْتُم',
        'أنتِ': 'أَنْتِ',
        'أنتما مؤ': 'أَنْتُما مُؤَنَث',
        'أنتن': 'أَنْتُنَّ',
        'أنا': 'أَنَا',
        'نحن': 'نَحْنُ',
    }

    future_type_list = {
        0: "فتحة",
        1: "كسرة",
        2: "ضمة"
    }

    chapters = {
        'إِفْعال': libqutrub.conjugator.conjugate(
            'أَفعَلَ', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'تَفْعيل': libqutrub.conjugator.conjugate(
            'فَعَّل', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'مُفاعَلَة': libqutrub.conjugator.conjugate(
            'فاعَل', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'إِفْتِعال': libqutrub.conjugator.conjugate(
            'اِفتَعَل', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'إِنْفِعال': libqutrub.conjugator.conjugate(
            'اِنفَعَل', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'تَفاعُل': libqutrub.conjugator.conjugate(
            'تَفاعَل', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'تَفَعُّل': libqutrub.conjugator.conjugate(
            'تَفَعَّل', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
        'إِسْتِفْعال': libqutrub.conjugator.conjugate(
            'اِستفعلَ', future_type_list[0],
            transitive=True, display_format="DICT"
        ),
    }

    output = list()
    for ch in chapters:
        for tense in chapters[ch]:
            if tense in tense_list:
                for pronoun in chapters[ch][tense]:
                    if araby.waznlike(word, chapters[ch][tense][pronoun]):
                        marks = araby.separate(chapters[ch][tense][pronoun])[1]
                        letters = araby.strip_harakat(word)
                        verb = araby.joint(letters, marks)
                        verb = split_shadda(verb)
                        if len(verb) > 0 and (araby.waznlike(verb, word)):
                            result_dict = {
                                "onchapter": ch,
                                "pronoun": pronoun_list[pronoun],
                                "tense": tense_list[tense],
                                "verb": verb
                            }
                            output.append(result_dict)
    if output:
        response = {
            "status": True,
            "result": {
                "word": word,
                "pairs" : output,
            }
        }
    else:
        response = {
            "status": False,
            "result": {
                "error": 102,
                "word": word,
            }
        }
    return response
