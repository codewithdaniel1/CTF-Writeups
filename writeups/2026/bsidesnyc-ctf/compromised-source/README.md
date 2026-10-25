# Compromised Source

**BSidesNYC CTF · 2026**

A Sentinel talk-page discussion contains a user whose expertise goes beyond ordinary fan knowledge. Inspect the post markup to uncover the hidden flag.

[View the styled writeup on my website](https://codewithdaniel1.github.io/writeups/2026/bsidesnyc-ctf/compromised-source/compromised-source.html)

## The challenge

“Agent,

Someone is letting on more than they should.

They are talking about Sentinel.

Find the source.”

Start at the [archived CipherWiki website](../classified/assets/original/cipher-wiki/index.html). This local copy preserves the challenge pages and their supporting files.

Original challenge URL: [ctf313.com/cipher-wiki/index.html](https://ctf313.com/cipher-wiki/index.html).

## Find the source of the leak

Open the [Sentinel article](../classified/assets/original/cipher-wiki/org/sentinel.html) and follow its Talk tab to the [Sentinel talk page](../classified/assets/original/cipher-wiki/talk/org_sentinel.html). Review the discussion about the numbering of Section 13. In the post explaining how real intelligence sections are organized, `Morthwaite` speaks with oddly specific confidence about how intelligence functions are divided and why a technical section might sit outside the usual numbering.

That knowledge is the tell. The poster is not just speculating about the fictional organization; the post contains a second clue in an element that is hidden from the rendered page with the CSS class `null`.

```
<div class="null">RkxBR3syMjFCfQ==</div>
```

Decode the Base64 text:

```
python3 -c 'import base64; print(base64.b64decode("RkxBR3syMjFCfQ==").decode())'
```

The decoded text is `FLAG{221B}`. The suspicious source is `Morthwaite`, and the encoded string in that post provides the flag.

## Flag

```
FLAG{221B}
```

The source is identified by the post’s unusually specific knowledge; the hidden Base64 clue decodes directly to the flag above.
