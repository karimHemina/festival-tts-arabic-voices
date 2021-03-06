#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os

buckwalter = { #mapping from Arabic script to Buckwalter
	u'\u0628': u'b' , u'\u0630': u'*' , u'\u0637': u'T' , u'\u0645': u'm',
	u'\u062a': u't' , u'\u0631': u'r' , u'\u0638': u'Z' , u'\u0646': u'n',
	u'\u062b': u'^' , u'\u0632': u'z' , u'\u0639': u'E' , u'\u0647': u'h',
	u'\u062c': u'j' , u'\u0633': u's' , u'\u063a': u'g' , u'\u062d': u'H',
	u'\u0642': u'q' , u'\u0641': u'f' , u'\u062e': u'x' , u'\u0635': u'S',
	u'\u0634': u'$' , u'\u062f': u'd' , u'\u0636': u'D' , u'\u0643': u'k',
	u'\u0623': u'>' , u'\u0621': u'\'', u'\u0626': u'}' , u'\u0624': u'&',
	u'\u0625': u'<' , u'\u0622': u'|' , u'\u0627': u'A' , u'\u0649': u'Y',
	u'\u0629': u'p' , u'\u064a': u'y' , u'\u0644': u'l' , u'\u0648': u'w',
	u'\u064b': u'F' , u'\u064c': u'N' , u'\u064d': u'K' , u'\u064e': u'a',
	u'\u064f': u'u' , u'\u0650': u'i' , u'\u0651': u'~' , u'\u0652': u'o', ',':' sil ', ';':' sil ', '.':' sil sil ', '!':' sil sil ', '?':' sil sil ', '/':' sil ', ':':' sil ', '-':' sil ', '،':' sil '
}

def arabicToBuckwalter(word): #Convert input string to Buckwalter
	res = u''
	for letter in word:
		if(letter in buckwalter):
			res += buckwalter[letter]
		else:
			res += letter
	return res

def phonetise(text):
	utterances = text.splitlines()
	for utterance in utterances:
		utterance = arabicToBuckwalter(utterance)
		print(utterance)
if __name__ == "__main__":
	texts = u"""وَفِي الشَّوْطِ الثَّانِي اسْتَعَادَ بَارِيسُ سَانْ جِيْرَمانُ مُسْتَوَاهُ وَحَقَّقَ التَّعَادُلَ عَنْ طَرِيقِ ابْرَاهِيمُوفِيتْش - مِنْ تَسْدِيدَةٍ اسْتَعْصَتْ عَلَى الْحَارِسْ
	يَتَمَثَّلُ الْإِبْدَاعُ الْفَنِّيُّ وَالْحَضَارِيُّ الَّذِي يَكْشِفُ عَنْهُ الْمَعْرِضُ فِي تُحَفٍ كَثِيرَةٍ - مُتَنَوِّعَةٍ شَمِلَتْ عَشَرَاتِ الْأَزْيَاءِ الَّتِي نُسِجَتْ بِأَنَامِلَ ذَهَبِيَّةٍ - عَكَسَتْ سِحْرَ وَبَهَاءَ التَّطْرِيزِ بِالْحَرِيرِ وَمَوَادَّ أُخْرَى
	إِضَافَةً إِلَى عَرْضِ أَنْوَاعٍ عَدِيدَةٍ مِنَ الْأَثَاثِ الْمُزَخْرَفِ وَالصَّنَادِيقِ وَالْأَوَانِي وَالْأَدَوَاتِ - وَالْأَغْطِيَةِ وَاللَّوْحَاتِ الْفَنِّيَّةِ الْعَاكِسَةِ لِتِقْنِيَّاتٍ مُدْهِشَةٍ - تُجَسِّدُ مَهَارَاتٍ حِرَفِيَّةً عَرَفَتْهَا الْأَنْدُلُسْ
	يَخْتَلِفُ الْهَاتِفُ الزَّكِيُّ عَنِ الْهَاتِفِ التَّقْلِيدِيِّ فِي أَنَّهُ يُقَدِّمُ عَدَداً مِنْ وَظَائِفِ الْحَوْسَبَةِ الْمُتَطَوِّرَةِ - وَقُدُرَاتِ الْإِتِّصَالِ الْمُتَقَدِّمَةِ - إِلَى جَانِبِ وَظَائِفِ الْهَاتِفِ التَّقْلِيدِيَّةِ الْأُخْرَى
	وَكَامِرَاتِ التَّصْوِيرِ الْمُدْمَجَةِ ذَاتِ الدِّقَّةِ الْعَالِيَةِ"""
	for l in texts.split("\n"):
		print(phonetise(l))

