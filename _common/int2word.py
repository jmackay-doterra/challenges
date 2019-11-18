class IntToWord():
    def int_to_word(num):
        d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty',
             30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
             70: 'seventy', 80: 'eighty', 90: 'ninety'}
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert (0 <= num)

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0:
                return d[num]
            else:
                return d[num // 10 * 10] + '-' + d[num % 10]

        if (num < k):
            if num % 100 == 0:
                return d[num // 100] + ' hundred'
            else:
                return d[num // 100] + ' hundred and ' + IntToWord.int_to_word(num % 100)

        if (num < m):
            if num % k == 0:
                return IntToWord.int_to_word(num // k) + ' thousand'
            else:
                return IntToWord.int_to_word(num // k) + ' thousand ' + IntToWord.int_to_word(num % k)

        if (num < b):
            if (num % m) == 0:
                return IntToWord.int_to_word(num // m) + ' million'
            else:
                return IntToWord.int_to_word(num // m) + ' million ' + IntToWord.int_to_word(num % m)

        if (num < t):
            if (num % b) == 0:
                return IntToWord.int_to_word(num // b) + ' billion'
            else:
                return IntToWord.int_to_word(num // b) + ' billion ' + IntToWord.int_to_word(num % b)

        if (num % t == 0):
            return IntToWord.int_to_word(num // t) + ' trillion'
        else:
            return IntToWord.int_to_word(num // t) + ' trillion ' + IntToWord.int_to_word(num % t)

    def convertToString(num):
        if num >= 100:
            return 'hundred' + IntToWord.convertToString(num - 100)
        if num >= 90:
            return 'ninety' + IntToWord.convertToString(num - 90)
        if num >= 80:
            return 'eighty' + IntToWord.convertToString(num - 80)
        if num >= 70:
            return 'seventy' + IntToWord.convertToString(num - 70)
        if num >= 60:
            return 'sixty' + IntToWord.convertToString(num - 60)
        if num >= 50:
            return 'fifty' + IntToWord.convertToString(num - 50)
        if num >= 40:
            return 'forty' + IntToWord.convertToString(num - 40)
        if num >= 30:
            return 'thirty' + IntToWord.convertToString(num - 30)
        if num >= 20:
            return 'twenty' + IntToWord.convertToString(num - 20)
        else:
            if num == 0:
                return 'zero'
            if num == 1:
                return 'one'
            if num == 2:
                return 'two'
            if num == 3:
                return 'three'
            if num == 4:
                return 'four'
            if num == 5:
                return 'five'
            if num == 6:
                return 'six'
            if num == 7:
                return 'seven'
            if num == 8:
                return 'eight'
            if num == 9:
                return 'nine'
            if num == 10:
                return 'ten'
            if num == 11:
                return 'eleven'
            if num == 12:
                return 'twelve'
            if num == 13:
                return 'thirteen'
            if num == 14:
                return 'fourteen'
            if num == 15:
                return'fifteen'
            if num == 16:
                return'sixteen'
            if num == 17:
                return'seventeen'
            if num == 18:
                return'eighteen'