# Bonus Cypher

This cypher is quite the challenge as there are no clues as to where it is and what cypher it uses.

So i went back to the [ASD Webpage](https://www.asd.gov.au/75th-anniversary/events/2022-09-01-75th-anniversary-commemorative-coin) and noticed it had an Accessible text version.

Looking at that i noticed the inner and outer rings had some letters underlined, and some in bold. Taking a closer look at the image for the Front of the coin, these same characters are also marked similarly

## Outer Ring

The outer ring has characters in 3 states, Light, Shaded, and Dark. Lets make a few educated assumptions: Due to the pattern of Shaded, Light, and Dark, this is probably Morse Code, Shaded are spaces since they're least common, dark is a dot, and light is a dash.

If we convert each letter to a Dot, Dash, and Space to seperate words, it comes out as this:

```
.---- ----. ....- --... -.. ... -... .- .-.. -... . .-. - .--. .- .-. -.-
```

If we convert this to letters, it comes out as this:

```
1947DSBALBERTPARK
```

This looks correct as the Years 1947 and Albert Park stand out to me as relating to ASD

## Inner Ring

The inner ring only has 2 shadings, Dark, and Light, and from memory cypher 3 created 2 matrixes of 35 characters each, a total of 70 characters. Since ascii only uses 7 bits, this would mean this might be a binary representation of a 10 character string

Lets assume Dark are zeros (Light off) and Light are on (Light on), and lets space seperate each 7 bits for readability

```
1000001 1010011 1000100 1000011 1100010 1110010 0110010 0110000 0110010 0110010
```

If we convert this to ascii (As it was used earlier)

```
ASDCbr2022
```

This looks correct to me as ASD and the year 2022 Stand out to me
