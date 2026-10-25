# Bots

**BSidesNYC CTF · 2026**

Compare the timestamps on repeated CipherWiki talk-page threads. The same accounts appear almost immediately after a disinformation post, months apart.

[View the styled writeup on my website](https://codewithdaniel1.github.io/writeups/2026/bsidesnyc-ctf/bots/bots.html)

## The challenge

“Agent, a few of our disinformation bots have been... overzealous... in the speed of their replies in the talk pages, casting suspicion on their identities. Help us troubleshoot by identifying one of the usernames of the bots.”

Start at the [archived CipherWiki website](../classified/assets/original/cipher-wiki/index.html). This local copy preserves the challenge pages and their supporting files.

Original challenge URL: [ctf313.com/cipher-wiki/index.html](https://ctf313.com/cipher-wiki/index.html).

## Check the first thread

On the [*Zero Meridian* talk page](../classified/assets/original/cipher-wiki/talk/f09.html), find the thread titled **“THIS FILM IS BASED ON REAL EVENTS — READ THIS.”** The post by `RealDarkArchive` is timestamped **1 Mar 2024, 03:17**. Four accounts answer within two minutes:

- `CipherFan_88` — 03:18

- `WardForever` — 03:18

- `FilmBuffUK` — 03:19

- `MeridianMark` — 03:19

Later, `RealDarkArchive` explicitly calls attention to how quickly those replies arrived.

## Cross-check the second thread

The [*The Last Directorate* talk page](../classified/assets/original/cipher-wiki/talk/f15.html) repeats the pattern in a thread titled **“THIS IS ALL REAL — SECOND WARNING.”** `RealDarkArchive` posts at **28 Oct 2023, 02:44**. The same four usernames answer by 02:46, in the same order. A regular user does not join until 08:30.

The repeated, near-immediate replies across two separate discussions identify a coordinated group. The challenge asks for one username; `CipherFan_88` is the first account in both bursts.

**Answer:** `CipherFan_88`. The other accounts in the same rapid-response group are `WardForever`, `FilmBuffUK`, and `MeridianMark`.

## Flag

```
CipherFan_88
```

The username is the requested answer. The evidence is the same coordinated set of four accounts posting within minutes on both talk pages.
