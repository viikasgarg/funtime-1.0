#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#
#  Copyright 2012 vikas <vikas@vikas-ThinkPad>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
########################################################################




############    Public Functions #######################################
def LifePathValue(day,month,year):
    return SingleDigit(day+month+year,True)

def ExpressionValue(firstname, middlename, lastname):
    fvalue = NametoNumber(firstname,True)
    mvalue = NametoNumber(middlename,True)
    lvalue = NametoNumber(lastname,True)
    return SingleDigit(fvalue+mvalue+lvalue,True)

def ChallengeNumbers(day,month,year):
    subChallenge1 = abs(SingleDigit(day,False) - SingleDigit(month,False))
    subChallenge2 = abs(SingleDigit(day,False) - SingleDigit(year,False))
    finalChallenge = abs(subChallenge1 - subChallenge2)
    return {'sub1':subChallenge1,'sub2': subChallenge2,'final': finalChallenge}

def PersonalYearValue(day,month,year):
    return SingleDigit((SingleDigit(day,False)+SingleDigit(month,False) + SingleDigit (year,False)),False)

def SoulUrgeValue(firstname, middlename, lastname):
    fvalue = NameVoweltoNumber(firstname,True)
    mvalue = NameVoweltoNumber(middlename,True)
    lvalue = NameVoweltoNumber(lastname,True)
    return SingleDigit(fvalue+mvalue+lvalue,True)

def Essences(firstname,middlename,lastname,age_year):
    fvalue = EssenceNameValue(firstname,age_year)
    mvalue = EssenceNameValue(middlename,age_year)
    lvalue = EssenceNameValue(lastname,age_year)
    return SingleDigit(fvalue+mvalue+lvalue,False)

def PinnacleNumbers(day,month,year):
    firstpinnacle = SingleDigit(SingleDigit(day,True) + SingleDigit(month,True),True)
    secondpinnacle = SingleDigit(SingleDigit(day,True) + SingleDigit(year,True),True)
    thirdpinnacle = SingleDigit(firstpinnacle + secondpinnacle,True)
    fourthpinnacle = SingleDigit(SingleDigit(month,True) + SingleDigit(year,True),True)
    return {'first_pinnacle':firstpinnacle,'second_pinnacle': secondpinnacle,
            'third_pinnacle': thirdpinnacle,'fourth_pinnacle':fourthpinnacle}

########################################################################
####  Internal Functions    ############################################
def NameVoweltoNumber(name,WithMasters):
    value = 0
    prevCharIsVowel = False
    if name.isalpha():
        name = name.upper()
        for char in list(name):
            if char in ['A','E','I','O','U'] or (prevCharIsVowel and char in ['Y','W']):
                numChar = ord(char)-64
                value += (numChar - ((numChar-1)/9)*9)
                prevCharIsVowel = not prevCharIsVowel
        if value == 0:
            for char in list(name):
                if char == 'Y':
                    value += 7

        value = SingleDigit(value,WithMasters)
    return value

def NametoNumber(name,WithMasters):
    value = 0
    if name.isalpha():
        name = name.upper()
        for char in list(name):
            numChar = ord(char)-64
            value += (numChar - ((numChar-1)/9)*9)

        value = SingleDigit(value,WithMasters)
    return value

def SingleDigit(number,WithMasters):
    if number <= 0:
        return None
    if WithMasters:
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]
    else:
        number_list = range(0,10)
    value = 0;
    if number in number_list:
        value = number
    else:
        while number/10:
            value += number%10
            number /= 10

        value += number
        if value not in number_list:
            value = SingleDigit(value,WithMasters)

    return value

def EssenceNameValue(name,age_year):
    value = 0
    ret_val = 0
    if name.isalpha():
        name = name.upper()
        while value < age_year:
            for char in list(name):
                numChar = ord(char)-64
                ret_val = (numChar - ((numChar-1)/9)*9)
                value += ret_val
                if value >= age_year:
                    break;
    return ret_val

########################################################################
###  Test Functions ####################################################

def testSingleDigit():
    num=1993
    if 22 != SingleDigit(int(num),True):
        assert False
    if 4 != SingleDigit(int(num),False):
        assert False
    return 0

def testLifePath():
    if 9 != LifePathValue(13,6,1988):
        assert False

def testNametoNumber():
    if 8 != NametoNumber('vikas',True):
        assert False
    if 8 != NametoNumber('vikas',False):
        assert False

def testExpressionValue():
    if 5 != ExpressionValue('vikas','','Garg'):
        assert False

def testSoulUrgeValue():
    if 5 != SoulUrgeValue('Eidward','Gibbon','WakeField'):
        assert False

def testPersonalYearValue():
    if 9 != PersonalYearValue(13,6,1988):
        assert False

def testChallengeNumbers():
    num =  ChallengeNumbers(13,6,1988)
    if (num['sub1'] != 2 and  num['sub2'] != 4 and num['final'] != 2):
        assert False
def testEssences():
    if 2 != Essences('vikas','kumar','garg',25):
        assert False

def testPinnacleNumbers():
    pnum = PinnacleNumbers(13,6,1988)
    if pnum['first_pinnacle']!= 1 and pnum['second_pinnacle']!= 3 and pnum['third_pinnacle'] != 4  and pnum['fourth_pinnacle']!= 5:
        assert False
########################################################################
from datetime import date
import os

def get_data(path, prefix, value):
    file_path = os.path.join('numkundli','data', path, prefix+str(value))
    data ='Please check file path %s'%file_path
    with open(file_path) as f:
         data = f.read()
    return data

def NumKundliInfo(birthday, first_name='', middle_name='', last_name=''):
    info = {}
    day = birthday.day
    month = birthday.month
    year = birthday.year
    info['lifepath'] = get_data('LifePath', 'LifePath', LifePathValue(day, month, year))
    info['exp_num'] =  get_data('ExpNum', 'ExpNum', ExpressionValue(first_name, middle_name, last_name))
    info['soul_urge'] =  get_data('SoulUrge', 'SoulUrge', SoulUrgeValue(first_name, middle_name, last_name))
    info['personal_nums'] = get_data('PersonalYear', 'PersonalYear', PersonalYearValue(day, month, year))

    challenge_nums = ChallengeNumbers(day, month, year)
    sub1 = get_data('ChallengeNum', 'ChallengeNum', challenge_nums['sub1'])
    sub2 = get_data('ChallengeNum', 'ChallengeNum', challenge_nums['sub2'])
    final = get_data('ChallengeNum', 'ChallengeNum', challenge_nums['final'])
    info['challenge_nums'] = {'sub1':sub1, 'sub2': sub2, 'final': final }

    pinnacle_nums = PinnacleNumbers(day, month, year)
    first_pinnacle = get_data('Pinnacle/com', 'pinnacle', pinnacle_nums['first_pinnacle']) + \
            get_data('Pinnacle/first', 'pinnacle', pinnacle_nums['first_pinnacle'])

    second_pinnacle = get_data('Pinnacle/com', 'pinnacle', pinnacle_nums['second_pinnacle']) + \
            get_data('Pinnacle/sec_third', 'pinnacle', pinnacle_nums['second_pinnacle'])

    third_pinnacle = get_data('Pinnacle/com', 'pinnacle', pinnacle_nums['third_pinnacle']) + \
            get_data('Pinnacle/sec_third', 'pinnacle', pinnacle_nums['third_pinnacle'])

    fourth_pinnacle = get_data('Pinnacle/com', 'pinnacle', pinnacle_nums['fourth_pinnacle']) + \
            get_data('Pinnacle/final', 'pinnacle', pinnacle_nums['fourth_pinnacle'])

    info['pinnacle_nums'] = {'first_pinnacle':first_pinnacle ,
                            'second_pinnacle': second_pinnacle,
                            'third_pinnacle': third_pinnacle,
                            'fourth_pinnacle': fourth_pinnacle,
                        }
    today = date.today()
    age =  today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    essence = Essences(first_name, middle_name, last_name, age)
    info['essences'] = get_data('Essences/com', 'Essences', essence) + \
            get_data('Essences/per', 'Essences', essence)

    return info

def main():
    testSingleDigit()
    testLifePath()
    testNametoNumber()
    testExpressionValue()
    testSoulUrgeValue()
    testPersonalYearValue()
    testChallengeNumbers()
    testEssences()
    testPinnacleNumbers()

if __name__ == '__main__':
    main()
