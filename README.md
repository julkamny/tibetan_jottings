# tibetan_jottings

Both headers have been checked countless times with the [sorting algorithm] to weed out mistakes (either due to my negligence or typos in the dictionary). In their current state they respect the alphabetical order.

## Jäschke

In the file containg Jäschke's headers, the symbol "–" was appended to all headers for which the transcription might be erroneous, either because they contain consonants between parentheses or because they contain Sanskrit words which I was not able to reproduce.

In a few cases, the heading of a page does not correspond to the actual printed entry. Here is a list of these typos – had there been more, I believe they should have been detected by the [sorting algorithm](https://github.com/Esukhia/tibetan-sort-python) of the BDRC:
- p. 112, instead of རྒྱད་པ་ read རྒྱུད་པ་
- p. 361, instead of འཕྲང་བ་ read འཕྲེང་བ་
- p. 430, instead of ཅ་དར་ read ཙ་དར་
- p. 433, instead of གཅང་བ་ read གཙང་བ་
- p. 447, instead of ཆབ་ཆབ་ read ཚབ་ཚབ་

In one case, Jäschke does not seem to respect his own sorting order:
- p. 454, མཚའ་ལུ་ | མཚགས་ is not consistent with p. 82 for instance དགག་པ་ | […] | དགབ་པ་ | དགའ་བ་

## Das

- There are a few pages where some words seem misplaced (for instance རབ་འོག་ p. 1168), you might sometimes have to look in the vicinity of the page you landed on.
- There is a cluster of four pages where Das doesn't seem to respect a certain collation rule : 468. བརྗེ་ | 469. བརྗོད་དོ་ | 470. ལྗང་པ་ | 471. ལྗོངས་གསུམ་. བ + superscripted consonant should go last, according to Tournadre.
- In a few cases, the list of compounds after a word introduces irregularities in the expected alphabetical order, ex. :

21. ཀུན་
	22. ཀུན་གྱིས་བཀུར་བ་
	23. ཀུན་བཅོམ་
	24. ཀུན་ཏུ་རྒྱས་པར་བྱེད་པ་
	25. ཀུན་ཏུ་རྨོངས་
	26. ཀུན་བརྟགས་
	27. ཀུན་ནས་ཉོན་མོངས་པ་
	28. ཀུན་སྤྱོད་ངན་པ་
	29. ཀུན་རིག་
and then 30. ཀུན་ད་

To make it simpler, headers that are compounds that would have disrupted the alphabetical flow have been indented ; they are not taken into account by the script.
- On many occasions I have selected another word on the page than the actual header, either because it was shorter and thus faster to type, or to avoid marring the alphabetical order (due to compounds, misplaced words).
