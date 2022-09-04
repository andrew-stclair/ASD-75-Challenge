# Cypher 3

The Inner String on the front of the coin is a string of characters, there is a few shapes at the bottom (Side note, this is `ASD` in their LetterHead), we can assume this denotes the start and end of this string

Using the clue from the previous cypher, `7 width x 5 depth` we can decode this

```
BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5
```
Splitting every 7 characters:
```
BGOAMVO
EIATSIR
LNGTTNE
OGRERGX
NTEAIFC
ECAIEOA
LEKFNR5
LWEFCHD
EEAEEE7
NMDRXX5
```
Splitting every 5 rows:
```
BGOAMVO
EIATSIR
LNGTTNE
OGRERGX
NTEAIFC

ECAIEOA
LEKFNR5
LWEFCHD
EEAEEE7
NMDRXX5
```

This gives us 2 matrixes, you read the message by reading each column in the first matrix from the top down, then the next column from left to right, then the same for the second matrix

E.G.
```
13
24

57
68
```
becomes
```
12345678
```

```
BELONGINGTOAGREATTEAMSTRIVINGFOREXCELLENCEWEMAKEADIFFERENCEXORHEXA5D75

BELONGING TO A GREAT TEAM STRIVING FOR EXCELLENCE WE MAKE A DIFFERENCE XOR HEX A5D75
```

That last bit is our clue for the next cypher
