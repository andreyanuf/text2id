# Text converter for text to speech tasks.

This script is designed to convert text representation to ordinal numbers in 
the sequence of symbols:
```
'_', '-', '!', "'", '(', ')', ',', '.', ':', ';', '?', ' ', 'A', 'B', 'C', 'D', 'E',
'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@AA', '@AA0', '@AA1',
'@AA2', '@AE', '@AE0', '@AE1', '@AE2', '@AH', '@AH0', '@AH1', '@AH2', '@AO', '@AO0',
'@AO1', '@AO2', '@AW', '@AW0', '@AW1', '@AW2', '@AY', '@AY0', '@AY1', '@AY2', '@B',
'@CH', '@D', '@DH', '@EH', '@EH0', '@EH1', '@EH2', '@ER', '@ER0', '@ER1', '@ER2',
'@EY', '@EY0', '@EY1', '@EY2', '@F', '@G', '@HH', '@IH', '@IH0', '@IH1', '@IH2',
'@IY', '@IY0', '@IY1', '@IY2', '@JH', '@K', '@L', '@M', '@N', '@NG', '@OW', '@OW0',
'@OW1', '@OW2', '@OY', '@OY0', '@OY1', '@OY2', '@P', '@R', '@S', '@SH', '@T', '@TH',
'@UH', '@UH0', '@UH1', '@UH2', '@UW', '@UW0', '@UW1', '@UW2', '@V', '@W', '@Y', '@Z',
'@ZH'
```

The sequence of symbols is union of English alphabet, arphabet and punctuation symbols.
This script based on https://github.com/keithito/tacotron and supports following
preprocessing steps:
1. Convert input text to ascii symbols. We use internal converter which support 
restricted set of symbols from German, French, Spanish and Russian alphabets.
```
Müller -> Mueller
```
2. Lower case conversion.
```
Mueller -> mueller
```
3. Expand numbers.
```
1234 -> twelve thirty-four
```
4. Expand restricted set of abbreviations.
```
ltd -> limited
```
5. Collate whitespaces.
```
My   name -> My name
```

## Example
```python
from text2id import Text2Id

def run_sample(t2i, text):
    print(t2i.text_to_sequence(text))
    print(t2i.sequence_to_text(t2i.text_to_sequence(text)))
    print(t2i.text_to_sequence(text, use_dict=False))
    print(t2i.sequence_to_text(t2i.text_to_sequence(text, use_dict=False)))

if __name__ == "__main__":
    t2i = Text2Id()
    print("Supported symbols: ", t2i.get_symbols())
    text = "Müller said 11 12 13"
    run_sample(t2i, text)

    text = "Hello 1234."
    run_sample(t2i, text)
```
