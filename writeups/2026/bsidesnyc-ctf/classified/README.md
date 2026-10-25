# Classified

**BSidesNYC CTF · 2026**

A mole is using CipherWiki talk pages to leak information about “retired” Agent Poole. The trail leads from an archived discussion to a hex-encoded document path and a hidden flag in a classified memo.

[View the styled writeup on my website](https://codewithdaniel1.github.io/writeups/2026/bsidesnyc-ctf/classified/classified.html)

CipherWiki links in this writeup open the rendered archive on my website. The original HTML source remains in this repository.

## The challenge

The prompt says a persistent mole is using the talk pages of CipherWiki to exfiltrate information about “retired” Agent Poole. It asks us to find the flag in the information being leaked.

Start at the [archived CipherWiki website](https://codewithdaniel1.github.io/writeups/2026/bsidesnyc-ctf/classified/assets/original/cipher-wiki/index.html). This local copy preserves the challenge pages and their supporting files.

Original challenge URL: [ctf313.com/cipher-wiki/index.html](https://ctf313.com/cipher-wiki/index.html).

## Find the Poole discussion

From the wiki homepage, open *The Lisbon Frequency* and select its [Talk page](https://codewithdaniel1.github.io/writeups/2026/bsidesnyc-ctf/classified/assets/original/cipher-wiki/talk/f02.html). The discussion describes Derek Poole as an unusual figure in the film’s production history: he had no film credits before or after this movie and was brought in specifically for second-unit dialogue.

That detail makes the word “retired” feel like a clue rather than background flavor. An archive notice on the page adds a direction: earlier discussion about Poole was moved to the Canon Disputes board. The talk page is not the final destination; it tells us that relevant information has been filed elsewhere.

**Clue to carry forward:** Poole’s discussion was moved to an archive. While inspecting the current page, its source also contains a document reference that is not presented as an ordinary link.

## Inspect the page source

Viewing the HTML reveals an unusual rule associated with the `docref` class:

```
.docref { #2f636c61737369666965642f6f63372e68746d6c; }
```

This is not a normal CSS declaration: there is no property name before the value. The sequence after the hash is made up of hexadecimal characters, so treat it as encoded data rather than a color or a usable style.

Convert each pair of hex digits to a byte, then decode those bytes as ASCII:

```
python3 -c 'print(bytes.fromhex("2f636c61737369666965642f6f63372e68746d6c").decode())'
```

The output is a path:

```
/classified/oc7.html
```

The readable filename points to the OC-7 memo. Resolve this path from the CipherWiki directory: on the original host, the document is at `/cipher-wiki/classified/oc7.html`.

## Read the OC-7 memo

Open the decoded path in the [archived OC-7 memo](https://codewithdaniel1.github.io/writeups/2026/bsidesnyc-ctf/classified/assets/original/cipher-wiki/classified/oc7.html). The memo discusses the CIPHER production series and includes a section about the Poole incident.

The flag is present in the document’s HTML inside an element with the `ghost-text` class:

```
<div class="ghost-text">FLAG = C321A</div>
```

When a page includes content that is hidden or styled unusually, inspect the document source as well as the visible page. Here the flag is directly readable in the markup once the memo has been found.

## Flag

The archived discussion identifies the trail, the malformed CSS rule carries a hex-encoded path, and the memo’s source reveals the flag:

```
C321A
```

<table class="writeup-table">
            <thead><tr><th>Step</th><th>Evidence</th><th>What it tells us</th></tr></thead>
            <tbody>
              <tr><td>1</td><td><em>The Lisbon Frequency</em> talk page</td><td>Poole’s discussion was moved to the Canon Disputes archive.</td></tr>
              <tr><td>2</td><td><code>.docref</code> rule with hex data</td><td>Decoding the value reveals <code>/classified/oc7.html</code>.</td></tr>
              <tr><td>3</td><td>OC-7 memo source</td><td>The <code>ghost-text</code> element contains <code>FLAG = C321A</code>.</td></tr>
            </tbody>
          </table>
        

The main lesson is to follow the information trail the challenge gives you. Talk pages can contain leads, archive notices can point to the next location, and an odd source-code value may be a path encoded in plain sight.
