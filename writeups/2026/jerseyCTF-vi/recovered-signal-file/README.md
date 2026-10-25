# Recovered Signal File

**JerseyCTF VI · 2026**

A short encoded transmission resolves into a flag after two simple transformations: Base64 decoding and a Caesar shift.

[View the styled writeup on my website](https://codewithdaniel1.github.io/writeups/2026/jerseyCTF-vi/recovered-signal-file/recovered-signal-file.html)

## The challenge

This signal was recovered from a Cold War-era satellite. The encryption doesn't appear very advanced, but it was enough to avoid detection at the time. With the right approach, the message should be recoverable.

Flag format for this challenge is `flag{}`.

- [Original challenge file · signal.log](assets/original/signal.log)

## Decode the transmission

Decode the Base64 string to expose the intermediate text:

```
echo 'aW9kant2ZHdob29sd2hfdmxqcWRvX2doZnJnaGd9' | base64 -d
```

```
iodj{vdwhoolwh_vljqdo_ghfrghg}
```

The result still looks transformed. Shifting each letter backward by three positions gives a readable flag. The substitution wraps around the alphabet, so `d` becomes `a`; punctuation and underscores remain unchanged.

```
echo 'iodj{vdwhoolwh_vljqdo_ghfrghg}' | tr 'A-Za-z' 'X-ZA-Wx-za-w'
```

```
flag{satellite_signal_decoded}
```

- [Recovered intermediate text](assets/recovered/signal-base64-decoded.txt)

- [Recovered flag file](assets/recovered/signal-flag.txt)

## Takeaway

The transmission uses two layers: Base64 followed by a Caesar substitution with a shift of three. Checking the output after each step makes the transformations easy to verify.

```
flag{satellite_signal_decoded}
```
