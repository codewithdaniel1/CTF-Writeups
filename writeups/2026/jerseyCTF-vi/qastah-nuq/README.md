# qaStaH nuq

**JerseyCTF VI · 2026**

Filter a noisy packet capture down to one HTTP exchange, then decode the response body to recover the flag.

[View the styled writeup on my website](https://codewithdaniel1.github.io/writeups/2026/jerseyCTF-vi/qastah-nuq/qastah-nuq.html)

## The challenge

The USS Enterprise is conducting an intelligence gathering mission near the neutral zone. During the mission, Spock intercepted some network traffic and handed you the resulting PCAP file for analysis. Upon preliminary examination Spock believes the Klingon Empire may be concealing encoded messages within otherwise routine network traffic. Your task is to analyze and uncover any hidden transmissions.

- [Original challenge PCAP](assets/original/qaStaH_nuq.pcap)

## Follow the HTTP exchange

The request identifies the host and resource:

```
GET /plans.html HTTP/1.1
Host: klingon/empire.kl
```

The corresponding response returns a text attachment named `flag.txt`. Its body is Base64 text:

```
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 36
Content-Disposition: attachment; filename=flag.txt

amN0ZntBdHRhY2tfVGhlX0VudGVycHJpc2V9
```

After extracting the body, decode it with:

```
echo 'amN0ZntBdHRhY2tfVGhlX0VudGVycHJpc2V9' | base64 -d
```

```
jctf{Attack_The_Enterprise}
```

- [Recovered HTTP response](assets/recovered/qaStaH-http-response.txt)

- [Recovered flag file](assets/recovered/qaStaH-flag.txt)

## Takeaway

The capture is intentionally busy, but the payload is not hidden by encryption. Filtering for the requested URI reveals the HTTP response, and decoding its body completes the solve.

```
jctf{Attack_The_Enterprise}
```
